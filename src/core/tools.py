import ctypes
import functools


def callback(*cb_args):
    def decorator(func):
        # Define the callback function type (takes an int, returns None)
        if cb_args:
            CALLBACK = ctypes.CFUNCTYPE(None, *cb_args)
        else:
            CALLBACK = ctypes.CFUNCTYPE(ctypes.c_ulong, ctypes.c_voidp)

        @functools.wraps(func)
        def wrapped(*args):
            return func(*args)

        return CALLBACK(wrapped)

    return decorator
