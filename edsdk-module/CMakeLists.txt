cmake_minimum_required(VERSION 3.14)
project(edsdk_bindings)

# Find Pybind11
find_package(pybind11 REQUIRED)

# Specify the library location
set(EDSDK_INCLUDE_DIR "/usr/local/include")
set(EDSDK_LIBRARY "/usr/local/lib/libedsdk.so")

# Build the bindings
pybind11_add_module(edsdk src/bindings.cpp)
target_include_directories(edsdk PRIVATE ${EDSDK_INCLUDE_DIR})
target_link_libraries(edsdk PRIVATE ${EDSDK_LIBRARY})

