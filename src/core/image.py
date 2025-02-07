import asyncio
import ctypes
from typing import AsyncGenerator

import numpy as np

from . import eospy


class EdsSize(ctypes.Structure):
    _fields_ = [
        ("width", ctypes.c_uint32),
        ("height", ctypes.c_uint32),
    ]


class Image:
    def __init__(self):
        self.stream_ref = ctypes.c_voidp()
        self.evf_image = ctypes.c_voidp()
        self.stream_length = ctypes.c_uint32()
        eospy.create_memory_stream(ctypes.c_uint32(0), ctypes.byref(stream_ref))
        eospy.create_evf_image_ref(stream_ref, ctypes.byref(evf_image))

    @property
    def raw(self) -> bytes:
        if hasattr(self, "_raw"):
            return self._raw

        stream_ref = ctypes.c_voidp()
        evf_image = ctypes.c_voidp()
        stream_length = ctypes.c_uint32()

        eospy.create_memory_stream(ctypes.c_uint32(0), ctypes.byref(stream_ref))
        eospy.create_evf_image_ref(stream_ref, ctypes.byref(evf_image))
        eospy.download_evf_image(self.reference, evf_image)
        eospy.get_length(stream_ref, ctypes.byref(stream_length))
        self._raw = ctypes.string_at(stream_ref, stream_length.value)
        return self._raw
