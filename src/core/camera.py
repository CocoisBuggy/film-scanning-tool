import asyncio
import ctypes
import logging
from typing import AsyncGenerator

import cv2
import matplotlib.pyplot as plt
import numpy as np

from src.core import eospy
from src.core.property import EosPropID, PropertyEvent
from src.core.tools import callback

from .command import (EdsCameraCommand, EdsCameraStatusCommand,
                      EdsShutterButton, StateEvent)
from .image import EdsSize, Image

opened = 0


class DeviceInfo(ctypes.Structure):
    _fields_ = [
        ("szPortName", ctypes.c_char * 256),
        ("szDeviceDescription", ctypes.c_char * 256),
        ("deviceSubType", ctypes.c_uint32),
        ("reserved", ctypes.c_uint32),
    ]


class Camera:
    reference: ctypes.c_ulong
    name: str
    port: str
    queue: asyncio.Queue[EosPropID]
    status: asyncio.Queue[StateEvent]

    def __init__(self, reference: ctypes.c_ulong):
        self.reference = reference
        self.queue = asyncio.Queue()

        info = DeviceInfo()
        eospy.get_device_info(self.reference, ctypes.byref(info))

        self.name = str(info.szDeviceDescription.decode("utf8"))
        self.port = str(info.szPortName.decode("utf8"))
        self.log = logging.getLogger(f"{__name__}:{self.name}")
        cv2.namedWindow(f"{self.name} Viewfinder", cv2.WINDOW_NORMAL)
        self.viewfinder = f"{self.name} Viewfinder"

        # Each camera will have its own figure references.
        self.fig, self.axes = plt.subplots(nrows=2, ncols=2)

    async def get_property(self, property: EosPropID):
        prop_output = ctypes.c_uint32()
        eospy.get_property_data(
            self.reference,
            ctypes.c_uint32(property.value),
            ctypes.c_uint32(0),
            ctypes.c_uint(4),
            ctypes.byref(prop_output),
        )

        return prop_output.value

    async def set_property(self, property: EosPropID, value):
        eospy.set_property_data(
            self.reference,
            ctypes.c_uint32(property.value),
            ctypes.c_uint32(0),
            ctypes.c_uint32(4),
            ctypes.byref(ctypes.c_uint32(value)),
        )

        # wait until the property we care about lands on the stream
        while True:
            item = await self.queue.get()
            if item == EosPropID.Unknown:
                raise Exception("Bad signal, shutting down")

            if item == property:
                self.queue.task_done()
                break

    async def send_command(
        self,
        cmd: EdsCameraCommand | EdsShutterButton | EdsCameraStatusCommand,
        param: int = 0,
    ):
        self.log.debug(f"Will dispatch command {cmd} ({cmd.value})")

        if isinstance(cmd, EdsCameraStatusCommand):
            eospy.send_status_command(
                self.reference,
                ctypes.c_uint32(cmd.value),
                ctypes.c_uint32(param),
            )
        elif isinstance(cmd, EdsCameraCommand):
            eospy.send_command(
                self.reference, ctypes.c_uint32(cmd.value), ctypes.c_uint32(param)
            )

    async def snap(self) -> Image:
        return Image()

    async def stream(self) -> AsyncGenerator[bytes, None]:
        device = await self.get_property(EosPropID.Evf_OutputDevice)
        await self.set_property(EosPropID.Evf_OutputDevice, device | 2)
        assert await self.get_property(EosPropID.Evf_OutputDevice) & 2 == 2

        # Set the live view property
        while True:
            try:
                stream_ref = ctypes.c_voidp()
                evf_image = ctypes.c_voidp()
                stream_length = ctypes.c_uint32()
                data_p = ctypes.c_voidp()

                eospy.create_memory_stream(ctypes.c_uint32(0), ctypes.byref(stream_ref))
                eospy.create_evf_image_ref(stream_ref, ctypes.byref(evf_image))
                eospy.download_evf_image(self.reference, evf_image)
                eospy.get_pointer(stream_ref, ctypes.byref(data_p))
                eospy.get_length(stream_ref, ctypes.byref(stream_length))

                if evf_image.value is not None:
                    data = ctypes.string_at(data_p, stream_length.value)
                    assert len(data) == stream_length.value
                    assert len(data) > 128_00  # I chose this number arbitrarily

                    image_data = np.ctypeslib.as_array(
                        ctypes.cast(data_p, ctypes.POINTER(ctypes.c_ubyte)),
                        shape=(stream_length.value,),
                    )
                    image_bytes = bytes(image_data)
                    assert len(image_bytes) == len(data)

                    eospy.release(stream_ref)
                    eospy.release(evf_image)
                    yield data

                # We wanna plop the frame into the frame data
                plt.pause(0.001)

            except Exception as e:
                self.log.error(e)

            await asyncio.sleep(0.1)

    async def __aenter__(self, *args):
        @callback(ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_voidp)
        def __property_event_handler(evt, prop_id, inparam, _):
            [evt_type] = [t for t in PropertyEvent if t.value == evt]
            [prop] = [p for p in EosPropID if p.value == prop_id]
            self.log.debug(f"property change event, {evt_type} {prop}")
            self.queue.put_nowait(prop)

        @callback(ctypes.c_uint, ctypes.c_uint, ctypes.c_voidp)
        def __status_event_handler(evt, data):
            [evt_type] = [t for t in PropertyEvent if t.value == evt]
            self.log.debug(f"camera status changed: {evt_type} {data}")

        self.log.debug("Opening session to camera")
        eospy.open_session(self.reference)

        # We listen to notifications of property change
        eospy.set_property_event_handler(
            self.reference,
            ctypes.c_uint32(PropertyEvent._All.value),
            __property_event_handler,
            None,
        )

        eospy.set_camera_state_event_handler(
            self.reference,
            ctypes.c_uint32(StateEvent.All.value),
            __status_event_handler,
            None,
        )

        self.__status_event_handler = __status_event_handler
        self.__property_event_handler = __property_event_handler

        await self.send_command(EdsCameraCommand.DoEvfAf)

        return self

    async def __aexit__(self, *args):
        self.log.debug("Closing session with camera")
        eospy.close_session(self.reference)
        cv2.destroyWindow(self.viewfinder)
        plt.close(self.fig)  # close plot

        try:
            while self.queue.get_nowait():
                self.queue.task_done()
        except asyncio.queues.QueueEmpty:
            self.queue.put_nowait(EosPropID.Unknown)
