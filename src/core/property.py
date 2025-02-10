from enum import Enum


class EosPropID(Enum):
    Unknown = 0x0000FFFF

    ProductName = 0x00000002
    OwnerName = 0x00000004
    MakerName = 0x00000005
    DateTime = 0x00000006
    FirmwareVersion = 0x00000007
    BatteryLevel = 0x00000008
    SaveTo = 0x0000000B
    CurrentStorage = 0x0000000C
    CurrentFolder = 0x0000000D
    BatteryQuality = 0x00000010
    BodyIDEx = 0x00000015
    HDDirectoryStructure = 0x00000020

    # Image Properties
    ImageQuality = 0x00000100
    Orientation = 0x00000102
    ICCProfile = 0x00000103
    FocusInfo = 0x00000104
    WhiteBalance = 0x00000106
    ColorTemperature = 0x00000107
    WhiteBalanceShift = 0x00000108
    ColorSpace = 0x0000010D
    PictureStyle = 0x00000114
    PictureStyleDesc = 0x00000115
    PictureStyleCaption = 0x00000200

    # Image GPS Properties
    GPSVersionID = 0x00000800
    GPSLatitudeRef = 0x00000801
    GPSLatitude = 0x00000802
    GPSLongitudeRef = 0x00000803
    GPSLongitude = 0x00000804
    GPSAltitudeRef = 0x00000805
    GPSAltitude = 0x00000806
    GPSTimeStamp = 0x00000807
    GPSSatellites = 0x00000808
    GPSStatus = 0x00000809
    GPSMapDatum = 0x00000812
    GPSDateStamp = 0x0000081D

    # Capture Properties
    AEMode = 0x00000400
    DriveMode = 0x00000401
    ISOSpeed = 0x00000402
    MeteringMode = 0x00000403
    AFMode = 0x00000404
    Av = 0x00000405
    Tv = 0x00000406
    ExposureCompensation = 0x00000407
    FocalLength = 0x00000409
    AvailableShots = 0x0000040A
    Bracket = 0x0000040B
    WhiteBalanceBracket = 0x0000040C
    LensName = 0x0000040D
    AEBracket = 0x0000040E
    FEBracket = 0x0000040F
    ISOBracket = 0x00000410
    NoiseReduction = 0x00000411
    FlashOn = 0x00000412
    RedEye = 0x00000413
    FlashMode = 0x00000414
    LensStatus = 0x00000416
    Artist = 0x00000418
    Copyright = 0x00000419
    AEModeSelect = 0x00000436
    PowerZoom_Speed = 0x00000444
    ColorFilter = 0x0000047F
    DigitalZoomSetting = 0x00000477
    AfLockState = 0x00000480
    BrightnessSetting = 0x00000483

    # EVF Properties
    Evf_OutputDevice = 0x00000500
    Evf_Mode = 0x00000501
    Evf_WhiteBalance = 0x00000502
    Evf_ColorTemperature = 0x00000503
    Evf_DepthOfFieldPreview = 0x00000504
    Evf_Zoom = 0x00000507
    Evf_ZoomPosition = 0x00000508
    Evf_Histogram = 0x0000050A
    Evf_ImagePosition = 0x0000050B
    Evf_HistogramStatus = 0x0000050C
    Evf_AFMode = 0x0000050E
    Record = 0x00000510
    Evf_HistogramY = 0x00000515
    Evf_HistogramR = 0x00000516
    Evf_HistogramG = 0x00000517
    Evf_HistogramB = 0x00000518
    Evf_CoordinateSystem = 0x00000540
    Evf_ZoomRect = 0x00000541
    Evf_ImageClipRect = 0x00000545
    Evf_PowerZoom_CurPosition = 0x00000550
    Evf_PowerZoom_MaxPosition = 0x00000551
    Evf_PowerZoom_MinPosition = 0x00000552

    # Limited Properties
    UTCTime = 0x01000016
    TimeZone = 0x01000017
    SummerTimeSetting = 0x01000018
    ManualWhiteBalanceData = 0x01000204
    TempStatus = 0x01000415
    MirrorLockUpState = 0x01000421
    FixedMovie = 0x01000422
    MovieParam = 0x01000423
    Aspect = 0x01000431
    ContinuousAfMode = 0x01000433
    MirrorUpSetting = 0x01000438
    MovieServoAf = 0x0100043E
    AutoPowerOffSetting = 0x0100045E
    AFEyeDetect = 0x01000455
    FocusShiftSetting = 0x01000457
    MovieHFRSetting = 0x0100045D
    AFTrackingObject = 0x01000468
    RegisterFocusEdge = 0x0100046C
    DriveFocusToEdge = 0x0100046D
    FocusPosition = 0x0100046E
    StillMovieDivideSetting = 0x01000470
    CardExtension = 0x01000471
    MovieCardExtension = 0x01000472
    StillCurrentMedia = 0x01000473
    MovieCurrentMedia = 0x01000474
    ApertureLockSetting = 0x01000476
    LensIsSetting = 0x010004C0
    ScreenDimmerTime = 0x010004C1
    ScreenOffTime = 0x010004C2
    ViewfinderOffTime = 0x010004C3
    Evf_ClickWBCoeffs = 0x01000506
    EVF_RollingPitching = 0x01000544
    Evf_VisibleRect = 0x01000546

    # DC Properties
    DC_Zoom = 0x00000600
    DC_Strobe = 0x00000601
    LensBarrelStatus = 0x00000605


class PropertyEvent(Enum):
    _All = 0x100
    Changed = 0x101
    DescChanged = 0x102


class DeviceOutput(Enum):
    Camera = 0x01
    Pc = 0x10
    PcSmall = 0x08
