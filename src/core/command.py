from enum import Enum


class EdsCameraCommand(Enum):
    """Canon EDSDK Camera Commands."""

    TakePicture = 0x00000000
    ExtendShutDownTimer = 0x00000001
    BulbStart = 0x00000002
    BulbEnd = 0x00000003
    DoEvfAf = 0x00000102
    DriveLensEvf = 0x00000103
    DoClickWBEvf = 0x00000104
    MovieSelectSwON = 0x00000107
    MovieSelectSwOFF = 0x00000108
    PressShutterButton = 0x00000004
    RequestRollPitchLevel = 0x00000109
    DrivePowerZoom = 0x0000010D
    SetRemoteShootingMode = 0x0000010F
    RequestSensorCleaning = 0x00000112
    SetModeDialDisable = 0x00000113


class EdsEvfAf(Enum):
    """Canon EDSDK EVF AF Commands."""

    OFF = 0
    ON = 1


class EdsShutterButton(Enum):
    """Canon EDSDK Shutter Button Commands."""

    OFF = 0x00000000
    Halfway = 0x00000001
    Completely = 0x00000003
    Halfway_NonAF = 0x00010001
    Completely_NonAF = 0x00010003


class EdsCameraStatusCommand(Enum):
    """Canon EDSDK Camera Status Commands."""

    UILock = 0x00000000
    UIUnLock = 0x00000001
    EnterDirectTransfer = 0x00000002
    ExitDirectTransfer = 0x00000003


class StateEvent(Enum):
    """Canon EDSDK State Events."""

    All = 0x00000300
    Shutdown = 0x00000301
    JobStatusChanged = 0x00000302
    WillSoonShutDown = 0x00000303
    ShutDownTimerUpdate = 0x00000304
    CaptureError = 0x00000305
    InternalError = 0x00000306
    AfResult = 0x00000309
    BulbExposureTime = 0x00000310
    PowerZoomInfoChanged = 0x00000311
