import asyncio
import ctypes

import cv2

from src.core import eospy


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

    def __init__(self, reference: ctypes.c_ulong):
        self.reference = reference

        info = DeviceInfo()
        eospy.get_device_info(self.reference, ctypes.byref(info))

        self.name = str(info.szDeviceDescription.decode("utf8"))
        self.port = str(info.szPortName.decode("utf8"))
        self.viewfinder = cv2.namedWindow(f"{self.name} Viewfinder", cv2.WINDOW_NORMAL)

    def snap(self) -> Image:
        pass

    async def stream(self):
        while True:
            yield
            await asyncio.sleep(0.1)

    def __enter__(self, *args):
        eospy.open_session()
        return self

    def __exit__(self, *args):
        pass
