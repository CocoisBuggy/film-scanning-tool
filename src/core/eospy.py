
# DO NOT EDIT THIS, IT IS CODE-GENERATED AT RUNTIME
# FOR STATIC TYPE EVALUATION
import ctypes
from src.core.exception import intercept

clib = ctypes.CDLL("./lib/libEDSDK.so") 



@intercept
def close_session(*args):
    """
    <ctype 'unsigned long(*)(struct __EdsObject *)'>
    """
    return clib.EdsCloseSession(*args)


@intercept
def copy_data(*args):
    """
    <ctype 'unsigned long(*)(struct __EdsObject *, unsigned long, struct __EdsObject *)'>
    """
    return clib.EdsCopyData(*args)


@intercept
def create_evf_image_ref(*args):
    """
    <ctype 'unsigned long(*)(struct __EdsObject *, struct __EdsObject * *)'>
    """
    return clib.EdsCreateEvfImageRef(*args)


@intercept
def create_file_stream(*args):
    """
    <ctype 'unsigned long(*)(char *, EdsFileCreateDisposition, EdsAccess, struct __EdsObject * *)'>
    """
    return clib.EdsCreateFileStream(*args)


@intercept
def create_file_stream_ex(*args):
    """
    <ctype 'unsigned long(*)(wchar_t *, EdsFileCreateDisposition, EdsAccess, struct __EdsObject * *)'>
    """
    return clib.EdsCreateFileStreamEx(*args)


@intercept
def create_image_ref(*args):
    """
    <ctype 'unsigned long(*)(struct __EdsObject *, struct __EdsObject * *)'>
    """
    return clib.EdsCreateImageRef(*args)


@intercept
def create_memory_stream(*args):
    """
    <ctype 'unsigned long(*)(unsigned long, struct __EdsObject * *)'>
    """
    return clib.EdsCreateMemoryStream(*args)


@intercept
def create_memory_stream_from_pointer(*args):
    """
    <ctype 'unsigned long(*)(void *, unsigned long, struct __EdsObject * *)'>
    """
    return clib.EdsCreateMemoryStreamFromPointer(*args)


@intercept
def create_stream(*args):
    """
    <ctype 'unsigned long(*)(EdsIStream *, struct __EdsObject * *)'>
    """
    return clib.EdsCreateStream(*args)


@intercept
def delete_directory_item(*args):
    """
    <ctype 'unsigned long(*)(struct __EdsObject *)'>
    """
    return clib.EdsDeleteDirectoryItem(*args)


@intercept
def download(*args):
    """
    <ctype 'unsigned long(*)(struct __EdsObject *, unsigned long, struct __EdsObject *)'>
    """
    return clib.EdsDownload(*args)


@intercept
def download_cancel(*args):
    """
    <ctype 'unsigned long(*)(struct __EdsObject *)'>
    """
    return clib.EdsDownloadCancel(*args)


@intercept
def download_complete(*args):
    """
    <ctype 'unsigned long(*)(struct __EdsObject *)'>
    """
    return clib.EdsDownloadComplete(*args)


@intercept
def download_evf_image(*args):
    """
    <ctype 'unsigned long(*)(struct __EdsObject *, struct __EdsObject *)'>
    """
    return clib.EdsDownloadEvfImage(*args)


@intercept
def download_thumbnail(*args):
    """
    <ctype 'unsigned long(*)(struct __EdsObject *, struct __EdsObject *)'>
    """
    return clib.EdsDownloadThumbnail(*args)


@intercept
def format_volume(*args):
    """
    <ctype 'unsigned long(*)(struct __EdsObject *)'>
    """
    return clib.EdsFormatVolume(*args)


@intercept
def get_attribute(*args):
    """
    <ctype 'unsigned long(*)(struct __EdsObject *, EdsFileAttributes *)'>
    """
    return clib.EdsGetAttribute(*args)


@intercept
def get_camera_list(*args):
    """
    <ctype 'unsigned long(*)(struct __EdsObject * *)'>
    """
    return clib.EdsGetCameraList(*args)


@intercept
def get_child_at_index(*args):
    """
    <ctype 'unsigned long(*)(struct __EdsObject *, long, struct __EdsObject * *)'>
    """
    return clib.EdsGetChildAtIndex(*args)


@intercept
def get_child_count(*args):
    """
    <ctype 'unsigned long(*)(struct __EdsObject *, unsigned long *)'>
    """
    return clib.EdsGetChildCount(*args)


@intercept
def get_device_info(*args):
    """
    <ctype 'unsigned long(*)(struct __EdsObject *, EdsDeviceInfo *)'>
    """
    return clib.EdsGetDeviceInfo(*args)


@intercept
def get_directory_item_info(*args):
    """
    <ctype 'unsigned long(*)(struct __EdsObject *, EdsDirectoryItemInfo *)'>
    """
    return clib.EdsGetDirectoryItemInfo(*args)


@intercept
def get_event(*args):
    """
    <ctype 'unsigned long(*)()'>
    """
    return clib.EdsGetEvent(*args)


@intercept
def get_image(*args):
    """
    <ctype 'unsigned long(*)(struct __EdsObject *, EdsImageSource, EdsTargetImageType, EdsRect, EdsSize, struct __EdsObject *)'>
    """
    return clib.EdsGetImage(*args)


@intercept
def get_image_info(*args):
    """
    <ctype 'unsigned long(*)(struct __EdsObject *, EdsImageSource, EdsImageInfo *)'>
    """
    return clib.EdsGetImageInfo(*args)


@intercept
def get_length(*args):
    """
    <ctype 'unsigned long(*)(struct __EdsObject *, unsigned long *)'>
    """
    return clib.EdsGetLength(*args)


@intercept
def get_parent(*args):
    """
    <ctype 'unsigned long(*)(struct __EdsObject *, struct __EdsObject * *)'>
    """
    return clib.EdsGetParent(*args)


@intercept
def get_pointer(*args):
    """
    <ctype 'unsigned long(*)(struct __EdsObject *, void * *)'>
    """
    return clib.EdsGetPointer(*args)


@intercept
def get_position(*args):
    """
    <ctype 'unsigned long(*)(struct __EdsObject *, unsigned long *)'>
    """
    return clib.EdsGetPosition(*args)


@intercept
def get_property_data(*args):
    """
    <ctype 'unsigned long(*)(struct __EdsObject *, unsigned long, long, unsigned long, void *)'>
    """
    return clib.EdsGetPropertyData(*args)


@intercept
def get_property_desc(*args):
    """
    <ctype 'unsigned long(*)(struct __EdsObject *, unsigned long, EdsPropertyDesc *)'>
    """
    return clib.EdsGetPropertyDesc(*args)


@intercept
def get_property_size(*args):
    """
    <ctype 'unsigned long(*)(struct __EdsObject *, unsigned long, long, EdsDataType *, unsigned long *)'>
    """
    return clib.EdsGetPropertySize(*args)


@intercept
def get_volume_info(*args):
    """
    <ctype 'unsigned long(*)(struct __EdsObject *, EdsVolumeInfo *)'>
    """
    return clib.EdsGetVolumeInfo(*args)


@intercept
def initialize_sdk(*args):
    """
    <ctype 'unsigned long(*)()'>
    """
    return clib.EdsInitializeSDK(*args)


@intercept
def open_session(*args):
    """
    <ctype 'unsigned long(*)(struct __EdsObject *)'>
    """
    return clib.EdsOpenSession(*args)


@intercept
def read(*args):
    """
    <ctype 'unsigned long(*)(struct __EdsObject *, unsigned long, void *, unsigned long *)'>
    """
    return clib.EdsRead(*args)


@intercept
def release(*args):
    """
    <ctype 'unsigned long(*)(struct __EdsObject *)'>
    """
    return clib.EdsRelease(*args)


@intercept
def retain(*args):
    """
    <ctype 'unsigned long(*)(struct __EdsObject *)'>
    """
    return clib.EdsRetain(*args)


@intercept
def seek(*args):
    """
    <ctype 'unsigned long(*)(struct __EdsObject *, long, EdsSeekOrigin)'>
    """
    return clib.EdsSeek(*args)


@intercept
def send_command(*args):
    """
    <ctype 'unsigned long(*)(struct __EdsObject *, unsigned long, long)'>
    """
    return clib.EdsSendCommand(*args)


@intercept
def send_status_command(*args):
    """
    <ctype 'unsigned long(*)(struct __EdsObject *, unsigned long, long)'>
    """
    return clib.EdsSendStatusCommand(*args)


@intercept
def set_attribute(*args):
    """
    <ctype 'unsigned long(*)(struct __EdsObject *, EdsFileAttributes)'>
    """
    return clib.EdsSetAttribute(*args)


@intercept
def set_camera_added_handler(*args):
    """
    <ctype 'unsigned long(*)(unsigned long(*)(void *), void *)'>
    """
    return clib.EdsSetCameraAddedHandler(*args)


@intercept
def set_camera_state_event_handler(*args):
    """
    <ctype 'unsigned long(*)(struct __EdsObject *, unsigned long, unsigned long(*)(unsigned long, unsigned long, void *), void *)'>
    """
    return clib.EdsSetCameraStateEventHandler(*args)


@intercept
def set_capacity(*args):
    """
    <ctype 'unsigned long(*)(struct __EdsObject *, EdsCapacity)'>
    """
    return clib.EdsSetCapacity(*args)


@intercept
def set_frame_point(*args):
    """
    <ctype 'unsigned long(*)(struct __EdsObject *, EdsPoint, _Bool)'>
    """
    return clib.EdsSetFramePoint(*args)


@intercept
def set_meta_image(*args):
    """
    <ctype 'unsigned long(*)(struct __EdsObject *, unsigned long, unsigned long, void *)'>
    """
    return clib.EdsSetMetaImage(*args)


@intercept
def set_object_event_handler(*args):
    """
    <ctype 'unsigned long(*)(struct __EdsObject *, unsigned long, unsigned long(*)(unsigned long, struct __EdsObject *, void *), void *)'>
    """
    return clib.EdsSetObjectEventHandler(*args)


@intercept
def set_progress_callback(*args):
    """
    <ctype 'unsigned long(*)(struct __EdsObject *, unsigned long(*)(unsigned long, void *, int *), EdsProgressOption, void *)'>
    """
    return clib.EdsSetProgressCallback(*args)


@intercept
def set_property_data(*args):
    """
    <ctype 'unsigned long(*)(struct __EdsObject *, unsigned long, long, unsigned long, void *)'>
    """
    return clib.EdsSetPropertyData(*args)


@intercept
def set_property_event_handler(*args):
    """
    <ctype 'unsigned long(*)(struct __EdsObject *, unsigned long, unsigned long(*)(unsigned long, unsigned long, unsigned long, void *), void *)'>
    """
    return clib.EdsSetPropertyEventHandler(*args)


@intercept
def terminate_sdk(*args):
    """
    <ctype 'unsigned long(*)()'>
    """
    return clib.EdsTerminateSDK(*args)


@intercept
def write(*args):
    """
    <ctype 'unsigned long(*)(struct __EdsObject *, unsigned long, void *, unsigned long *)'>
    """
    return clib.EdsWrite(*args)
