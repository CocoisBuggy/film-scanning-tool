import asyncio
import ctypes
import logging
import signal

import src.core.eospy as edsdk
from src.core.camera import Camera
from src.core.tools import callback

log = logging.getLogger(__name__)
camera_added_evt = asyncio.Event()


@callback(ctypes.c_ulong, ctypes.c_voidp)
def camera_added_evt_handler(*_):
    camera_added_evt.set()


class EosSession:
    cameras = []
    handlers = {"camera_added": []}

    def __init__(self):
        signal.signal(signal.SIGINT, self.disconnect)
        self.loop = asyncio.get_event_loop()

    def __enter__(self):
        edsdk.initialize_sdk()
        self.loop.create_task(self.__camera_added_manager())
        return self

    def __exit__(self, *args):
        log.debug("...cleaning up")
        edsdk.terminate_sdk()

    async def get_cameras(self):
        self.cameras_ref = ctypes.c_ulong()
        self.child_count = ctypes.c_ulong()

        edsdk.get_camera_list(ctypes.byref(self.cameras_ref))
        edsdk.get_child_count(self.cameras_ref, ctypes.byref(self.child_count))

        cameras = []
        for idx in range(self.child_count.value):
            camera_ref = ctypes.c_ulong()
            edsdk.get_child_at_index(self.cameras_ref, idx, ctypes.byref(camera_ref))
            cameras.append(Camera(camera_ref))

        return cameras

    async def __camera_added_manager(self):
        while True:
            await camera_added_evt.wait()
            camera_added_evt.clear()

            cameras = await self.get_cameras()

            for handler in self.handlers["camera_added"]:
                for camera in cameras:
                    if camera not in self.cameras:
                        handler(camera)

            self.cameras = cameras

    def on(self, func):
        log.debug(f"registering {func.__name__} function callback")
        self.handlers[func.__name__].append(func)

    def disconnect(self, signal, _):
        log.debug(f"recieved sys signal {signal}")
        self.connected = False

    async def run(self):
        self.connected = True
        self.cameras = await self.get_cameras()
        edsdk.set_camera_added_handler(camera_added_evt_handler, None)

        while self.connected:
            edsdk.get_event()
            await asyncio.sleep(0.01)
