#include <pybind11/pybind11.h>
#include <pybind11/functional.h>
#include <functional>
#include "edsdk_fix.h"
#include "EDSDK.h"

namespace py = pybind11;


// Global storage for the callback
std::function<EdsError(void*)> global_callback;

// C-style wrapper function for EdsSetCameraAddedHandler
EdsError EDSCALLBACK CameraAddedHandler(void* context) {
    if (global_callback) {
        return global_callback(context);
    }
    return EDS_ERR_OK;
}

// Function to set the callback from Python
void set_camera_added_handler(std::function<EdsError(void*)> callback) {
    global_callback = std::move(callback);
    EdsSetCameraAddedHandler(CameraAddedHandler, nullptr);
}

// Pybind11 module definition
PYBIND11_MODULE(edsdk_py, m) {
    m.def("set_camera_added_handler", &set_camera_added_handler, "Set the camera added callback");
}

