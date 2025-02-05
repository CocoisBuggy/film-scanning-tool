import asyncio
import ctypes
import logging
from typing import AsyncGenerator

import cv2

from src.core import eospy
from src.core.property import EosPropID, PropertyEvent
from src.core.tools import callback


class DeviceInfo(ctypes.Structure):
    _fields_ = [
        ("szPortName", ctypes.c_char * 256),
        ("szDeviceDescription", ctypes.c_char * 256),
        ("deviceSubType", ctypes.c_uint32),
        ("reserved", ctypes.c_uint32),
    ]


class Image:
    pass


class Camera:
    reference: ctypes.c_ulong
    name: str
    port: str
    queue: asyncio.Queue[EosPropID]

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

    async def send_command(self):
        pass

    async def snap(self) -> Image:
        return Image()

    async def stream(self) -> AsyncGenerator[bytes, None]:
        device = await self.get_property(EosPropID.Evf_OutputDevice)
        device |= 2  # we are specifying that we want the live feed diverted to the PC

        await self.set_property(EosPropID.Evf_OutputDevice, device)

        stream_ref = ctypes.c_voidp()
        evf_image = ctypes.c_voidp()

        eospy.create_memory_stream(0, ctypes.byref(stream_ref))
        eospy.create_evf_image_ref(stream_ref, ctypes.byref(evf_image))

        await asyncio.sleep(1)

        # Set the live view property
        while True:
            eospy.download_evf_image(self.reference, evf_image)

            if stream_ref.value is not None:
                # Find number of bytes required
                size = (stream_ref.value.bit_length() + 7) // 8
                yield stream_ref.value.to_bytes(size, "big")

            await asyncio.sleep(0.1)

    def __enter__(self, *args):
        @callback(ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_voidp)
        def __property_event_handler(evt, prop_id, inparam, _):
            [evt_type] = [t for t in PropertyEvent if t.value == evt]
            [prop] = [p for p in EosPropID if p.value == prop_id]
            self.log.debug(f"property change event, {evt_type} {prop}")
            self.queue.put_nowait(prop)

        self.log.debug("Opening session to camera")
        eospy.open_session(self.reference)
        # We listen to notifications of property change.
        eospy.set_property_event_handler(
            self.reference,
            ctypes.c_uint32(PropertyEvent._All.value),
            __property_event_handler,
            None,
        )

        self.__property_event_handler = __property_event_handler
        return self

    def __exit__(self, *args):
        self.log.debug("Closing session with camera")
        eospy.close_session(self.reference)
        cv2.destroyAllWindows()

        try:
            while self.queue.get_nowait():
                self.queue.task_done()
        except asyncio.queues.QueueEmpty:
            self.queue.put_nowait(EosPropID.Unknown)
