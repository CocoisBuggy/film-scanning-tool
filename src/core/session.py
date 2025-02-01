import ctypes
import signal
import time

import edsdk

from src.core.exception import intercept

# Define the types
EdsBaseRef = ctypes.c_void_p  # This is the base reference type
EdsCameraListRef = ctypes.POINTER(EdsBaseRef)  # Pointer to EdsBaseRef

CALLBACK_TYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p)


class EosSession:
    def __init__(self):
        edsdk.EdsInitializeSDK = intercept(edsdk.EdsInitializeSDK)
        edsdk.EdsTerminateSDK = intercept(edsdk.EdsTerminateSDK)
        signal.signal(signal.SIGINT, self.disconnect)

    def __enter__(self):
        edsdk.EdsInitializeSDK()

        return self

    def __exit__(self, *args):
        print("...cleaning up")
        edsdk.EdsTerminateSDK()

    def on(self, func):

        print(f"registering {func.__name__} function callback")
        pass

    def disconnect(self, signal, frame):
        print(f"recieved sys signal {signal} {frame}")
        self.connected = False

    def __evt(self, ctx):
        print(ctx)

    def connect(self):
        self.connected = True
        while self.connected:
            time.sleep(0.1)
            edsdk.EdsGetEvent()
            edsdk.EdsSetCameraAddedHandler(None, None)
