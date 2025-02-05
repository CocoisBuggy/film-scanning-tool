import ctypes
import functools
import logging

import inflection
from cffi import FFI

from src.core.exception import intercept

log = logging.getLogger(__name__)

ffi = FFI()
with open("./include/EDSDK_preprocessed.h") as f:
    c_header = f.read()
    ffi.cdef(c_header)

clib = ffi.dlopen("./lib/libEDSDK.so")


wrapped = """
# DO NOT EDIT THIS, IT IS CODE-GENERATED AT RUNTIME
# FOR STATIC TYPE EVALUATION
import ctypes
from src.core.exception import intercept

clib = ctypes.CDLL("./lib/libEDSDK.so") 

"""


def make_def(name: str, ctype):
    return f"""

@intercept
def {inflection.underscore(name).replace('eds_', '')}(*args):
    \"\"\"
    {ctype}
    \"\"\"
    return clib.{name}(*args)
"""


# Now, as far as I can tell, the edsdk has only got function definitions that return error types.
# As a result, I will intercept all return values such that they become raised
for func in dir(clib):
    name = func
    func = getattr(clib, name)

    if not callable(func):
        continue

    wrapped += make_def(name, ffi.typeof(func))  # pyright: ignore


# Everytime we run this application we will write a wrapped python
# library that we can use for static analysis BASED on our understanding of the edsdk
with open("./src/core/eospy.py", "w") as f:
    f.write(wrapped)
