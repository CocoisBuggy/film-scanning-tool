from setuptools import Extension, setup

module = Extension(
    "_edsdk",
    sources=["edsdk_wrap.c"],
    include_dirs=[
        "./include",
        "./lib",
    ],
)

setup(
    name="edsdk",
    version="1.0",
    ext_modules=[module],
    py_modules=["edsdk"],
)
