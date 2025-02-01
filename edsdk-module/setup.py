import os

from setuptools import Extension, setup

setup(
    ext_modules=[
        Extension(
            "edsdk",
            ["src/bindings.cpp"],
            libraries=["EDSDK"],
            library_dirs=[os.path.abspath("./lib")],  # Ensure correct path
            include_dirs=["/path/to/edsdk/include"],  # Adjust as needed
            extra_compile_args=["-std=c++11"],
        )
    ],
)
