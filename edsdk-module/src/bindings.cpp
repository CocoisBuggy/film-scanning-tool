#include <pybind11/pybind11.h>
#include <pybind11/functional.h>
#include "edsdk_fix.h"
#include "EDSDK.h"

namespace pybind11 {
    namespace detail {
        template <> struct type_caster<__EdsObject*> {
            PYBIND11_TYPE_CASTER(__EdsObject*, _("__EdsObject*"));

            bool load(pybind11::handle src, bool) {
                if (!src) return false;
                // Custom conversion logic here
                return true;
            }

            static pybind11::handle cast(__EdsObject* src, pybind11::return_value_policy policy, pybind11::handle parent) {
                // Custom conversion logic here
                return pybind11::none();  // Modify to return appropriate value
            }
        };

         template <> struct type_caster<EdsBaseRef> {
        PYBIND11_TYPE_CASTER(EdsBaseRef, _("EdsBaseRef"));

        bool load(handle src, bool) {
            // Implement logic to convert a Python object to EdsBaseRef
            return true;
        }

        static handle cast(EdsBaseRef src, return_value_policy /* policy */, handle /* parent */) {
            // Implement logic to convert EdsBaseRef to Python object
            return pybind11::none().release();
        }
    };
    }
}

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
PYBIND11_MODULE(edsdk, m) {
    m.doc() = "Python bindings for Canon EDSDK";


    m.def("retain", [](EdsBaseRef ref) {
        return EdsRetain(ref);
    }, "Increase reference count");

    m.def("release", [](EdsBaseRef ref) {
        return EdsRelease(ref);
    }, "Decrease reference count");

    // SDK Initialization
    m.def("initialize_sdk", &EdsInitializeSDK, "Initialize the SDK");
    m.def("terminate_sdk", &EdsTerminateSDK, "Terminate the SDK");

    // Reference management
    m.def("retain", &EdsRetain, "Increase reference count");
    m.def("release", &EdsRelease, "Decrease reference count");

    // Child elements
    m.def("get_child_count", &EdsGetChildCount, "Get the number of child elements");
    m.def("get_child_at_index", &EdsGetChildAtIndex, "Get child element at index");
    m.def("get_parent", &EdsGetParent, "Get parent of an element");

    // Property handling
    m.def("get_property_size", &EdsGetPropertySize, "Get the size of a property");
    m.def("get_property_data", &EdsGetPropertyData, "Retrieve property data");
    m.def("set_property_data", &EdsSetPropertyData, "Set property data");
    m.def("get_property_desc", &EdsGetPropertyDesc, "Retrieve property description");

    // Camera functions
    m.def("get_camera_list", &EdsGetCameraList, "Retrieve a list of connected cameras");
    m.def("get_device_info", &EdsGetDeviceInfo, "Retrieve device information");
    m.def("open_session", &EdsOpenSession, "Open a session with a camera");
    m.def("close_session", &EdsCloseSession, "Close the session with a camera");

    // Camera Commands
    m.def("send_command", &EdsSendCommand, "Send a command to the camera");
    m.def("send_status_command", &EdsSendStatusCommand, "Send a status command");
    m.def("set_capacity", &EdsSetCapacity, "Set storage capacity");

    // Volume and File operations
    m.def("get_volume_info", &EdsGetVolumeInfo, "Get information about a volume");
    m.def("format_volume", &EdsFormatVolume, "Format a volume");

    // Directory Items
    m.def("get_directory_item_info", &EdsGetDirectoryItemInfo, "Get directory item info");
    m.def("delete_directory_item", &EdsDeleteDirectoryItem, "Delete a directory item");
    m.def("download", &EdsDownload, "Download a file from the camera");
    m.def("download_cancel", &EdsDownloadCancel, "Cancel a download");
    m.def("download_complete", &EdsDownloadComplete, "Mark download as complete");
    m.def("download_thumbnail", &EdsDownloadThumbnail, "Download a thumbnail");
    m.def("get_attribute", &EdsGetAttribute, "Get file attributes");
    m.def("set_attribute", &EdsSetAttribute, "Set file attributes");

    // File and Memory Streams
    m.def("create_file_stream", &EdsCreateFileStream, "Create a file stream");
    m.def("create_memory_stream", &EdsCreateMemoryStream, "Create a memory stream");
    m.def("create_file_stream_ex", &EdsCreateFileStreamEx, "Create an extended file stream");
    m.def("create_memory_stream_from_pointer", &EdsCreateMemoryStreamFromPointer, "Create memory stream from a pointer");
    m.def("get_pointer", &EdsGetPointer, "Get pointer to stream data");
    m.def("read", &EdsRead, "Read data from stream");
    m.def("write", &EdsWrite, "Write data to stream");
    m.def("seek", &EdsSeek, "Seek within a stream");
    m.def("get_position", &EdsGetPosition, "Get stream position");
    m.def("get_length", &EdsGetLength, "Get stream length");
    m.def("copy_data", &EdsCopyData, "Copy data from one stream to another");

    // Image Handling
    m.def("create_image_ref", &EdsCreateImageRef, "Create an image reference");
    m.def("get_image_info", &EdsGetImageInfo, "Get image info");
    m.def("get_image", &EdsGetImage, "Retrieve an image");

    // Live View
    m.def("create_evf_image_ref", &EdsCreateEvfImageRef, "Create an EVF image reference");
    m.def("download_evf_image", &EdsDownloadEvfImage, "Download an EVF image");

    // Event Handlers
    m.def("set_camera_added_handler", &EdsSetCameraAddedHandler, "Set handler for when a camera is added");
    m.def("set_property_event_handler", &EdsSetPropertyEventHandler, "Set property event handler");
    m.def("set_object_event_handler", &EdsSetObjectEventHandler, "Set object event handler");
    m.def("set_camera_state_event_handler", &EdsSetCameraStateEventHandler, "Set camera state event handler");

    // Miscellaneous
    m.def("create_stream", &EdsCreateStream, "Create a stream");
    m.def("get_event", &EdsGetEvent, "Retrieve an event");
    m.def("set_frame_point", &EdsSetFramePoint, "Set autofocus frame point");
}


