typedef unsigned char __u_char;
typedef unsigned short int __u_short;
typedef unsigned int __u_int;
typedef unsigned long int __u_long;
typedef signed char __int8_t;
typedef unsigned char __uint8_t;
typedef signed short int __int16_t;
typedef unsigned short int __uint16_t;
typedef signed int __int32_t;
typedef unsigned int __uint32_t;
typedef signed long int __int64_t;
typedef unsigned long int __uint64_t;
typedef __int8_t __int_least8_t;
typedef __uint8_t __uint_least8_t;
typedef __int16_t __int_least16_t;
typedef __uint16_t __uint_least16_t;
typedef __int32_t __int_least32_t;
typedef __uint32_t __uint_least32_t;
typedef __int64_t __int_least64_t;
typedef __uint64_t __uint_least64_t;
typedef long int __quad_t;
typedef unsigned long int __u_quad_t;
typedef long int __intmax_t;
typedef unsigned long int __uintmax_t;
typedef unsigned long int __dev_t;
typedef unsigned int __uid_t;
typedef unsigned int __gid_t;
typedef unsigned long int __ino_t;
typedef unsigned long int __ino64_t;
typedef unsigned int __mode_t;
typedef unsigned long int __nlink_t;
typedef long int __off_t;
typedef long int __off64_t;
typedef int __pid_t;
typedef struct { int __val[2]; } __fsid_t;
typedef long int __clock_t;
typedef unsigned long int __rlim_t;
typedef unsigned long int __rlim64_t;
typedef unsigned int __id_t;
typedef long int __time_t;
typedef unsigned int __useconds_t;
typedef long int __suseconds_t;
typedef long int __suseconds64_t;
typedef int __daddr_t;
typedef int __key_t;
typedef int __clockid_t;
typedef void * __timer_t;
typedef long int __blksize_t;
typedef long int __blkcnt_t;
typedef long int __blkcnt64_t;
typedef unsigned long int __fsblkcnt_t;
typedef unsigned long int __fsblkcnt64_t;
typedef unsigned long int __fsfilcnt_t;
typedef unsigned long int __fsfilcnt64_t;
typedef long int __fsword_t;
typedef long int __ssize_t;
typedef long int __syscall_slong_t;
typedef unsigned long int __syscall_ulong_t;
typedef __off64_t __loff_t;
typedef char *__caddr_t;
typedef long int __intptr_t;
typedef unsigned int __socklen_t;
typedef int __sig_atomic_t;
typedef __int8_t int8_t;
typedef __int16_t int16_t;
typedef __int32_t int32_t;
typedef __int64_t int64_t;
typedef __uint8_t uint8_t;
typedef __uint16_t uint16_t;
typedef __uint32_t uint32_t;
typedef __uint64_t uint64_t;
typedef __int_least8_t int_least8_t;
typedef __int_least16_t int_least16_t;
typedef __int_least32_t int_least32_t;
typedef __int_least64_t int_least64_t;
typedef __uint_least8_t uint_least8_t;
typedef __uint_least16_t uint_least16_t;
typedef __uint_least32_t uint_least32_t;
typedef __uint_least64_t uint_least64_t;
typedef signed char int_fast8_t;
typedef long int int_fast16_t;
typedef long int int_fast32_t;
typedef long int int_fast64_t;
typedef unsigned char uint_fast8_t;
typedef unsigned long int uint_fast16_t;
typedef unsigned long int uint_fast32_t;
typedef unsigned long int uint_fast64_t;
typedef long int intptr_t;
typedef unsigned long int uintptr_t;
typedef __intmax_t intmax_t;
typedef __uintmax_t uintmax_t;
typedef uint64_t EdsUInt64;
typedef wchar_t WCHAR;
#pragma pack (push, 8)
typedef void EdsVoid;
typedef int EdsBool;
typedef char EdsChar;
typedef char EdsInt8;
typedef unsigned char EdsUInt8;
typedef short EdsInt16;
typedef unsigned short EdsUInt16;
typedef long EdsInt32;
typedef unsigned long EdsUInt32;
typedef int64_t EdsInt64;
typedef uint64_t EdsUInt64;
typedef float EdsFloat;
typedef double EdsDouble;
typedef EdsUInt32 EdsError;
typedef struct __EdsObject* EdsBaseRef;
typedef EdsBaseRef EdsCameraListRef;
typedef EdsBaseRef EdsCameraRef;
typedef EdsBaseRef EdsVolumeRef;
typedef EdsBaseRef EdsDirectoryItemRef;
typedef EdsBaseRef EdsStreamRef;
typedef EdsStreamRef EdsImageRef;
typedef EdsBaseRef EdsEvfImageRef ;
typedef enum
{
    kEdsDataType_Unknown = 0,
    kEdsDataType_Bool = 1,
    kEdsDataType_String = 2,
    kEdsDataType_Int8 = 3,
    kEdsDataType_UInt8 = 6,
    kEdsDataType_Int16 = 4,
    kEdsDataType_UInt16 = 7,
    kEdsDataType_Int32 = 8,
    kEdsDataType_UInt32 = 9,
    kEdsDataType_Int64 = 10,
    kEdsDataType_UInt64 = 11,
    kEdsDataType_Float = 12,
    kEdsDataType_Double = 13,
    kEdsDataType_ByteBlock = 14,
    kEdsDataType_Rational = 20,
    kEdsDataType_Point = 21,
    kEdsDataType_Rect = 22,
    kEdsDataType_Time = 23,
    kEdsDataType_Bool_Array = 30,
    kEdsDataType_Int8_Array = 31,
    kEdsDataType_Int16_Array = 32,
    kEdsDataType_Int32_Array = 33,
    kEdsDataType_UInt8_Array = 34,
    kEdsDataType_UInt16_Array = 35,
    kEdsDataType_UInt32_Array = 36,
    kEdsDataType_Rational_Array = 37,
    kEdsDataType_FocusInfo = 101,
    kEdsDataType_PictureStyleDesc,
} EdsDataType;
typedef EdsUInt32 EdsPropertyID;
typedef EdsUInt32 EdsCameraCommand;
typedef enum
{
 kEdsCameraCommand_EvfAf_OFF = 0,
 kEdsCameraCommand_EvfAf_ON = 1,
} EdsEvfAf ;
typedef enum
{
 kEdsCameraCommand_ShutterButton_OFF = 0x00000000,
 kEdsCameraCommand_ShutterButton_Halfway = 0x00000001,
 kEdsCameraCommand_ShutterButton_Completely = 0x00000003,
 kEdsCameraCommand_ShutterButton_Halfway_NonAF = 0x00010001,
 kEdsCameraCommand_ShutterButton_Completely_NonAF = 0x00010003,
} EdsShutterButton ;
typedef EdsUInt32 EdsCameraStatusCommand;
typedef EdsUInt32 EdsPropertyEvent;
typedef EdsUInt32 EdsObjectEvent;
typedef EdsUInt32 EdsStateEvent;
typedef enum
{
 kEdsEvfDriveLens_Near1 = 0x00000001,
 kEdsEvfDriveLens_Near2 = 0x00000002,
 kEdsEvfDriveLens_Near3 = 0x00000003,
 kEdsEvfDriveLens_Far1 = 0x00008001,
 kEdsEvfDriveLens_Far2 = 0x00008002,
 kEdsEvfDriveLens_Far3 = 0x00008003,
} EdsEvfDriveLens ;
typedef enum
{
 kEdsDrivePowerZoom_Stop = 0x00000000,
 kEdsDrivePowerZoom_LimitOff_Wide = 0x00000001,
 kEdsDrivePowerZoom_LimitOff_Tele = 0x00000002,
 kEdsDrivePowerZoom_LimitOn_Wide = 0x00000011,
 kEdsDrivePowerZoom_LimitOn_Tele = 0x00000012,
} EdsDrivePowerZoom;
typedef enum {
 kEdsEvfDepthOfFieldPreview_OFF = 0x00000000,
 kEdsEvfDepthOfFieldPreview_ON = 0x00000001,
} EdsEvfDepthOfFieldPreview ;
typedef enum
{
    kEdsSeek_Cur = 0,
    kEdsSeek_Begin ,
    kEdsSeek_End ,
} EdsSeekOrigin;
typedef enum
{
    kEdsAccess_Read = 0,
    kEdsAccess_Write ,
    kEdsAccess_ReadWrite ,
    kEdsAccess_Error = 0xFFFFFFFF,
} EdsAccess;
typedef enum
{
    kEdsFileCreateDisposition_CreateNew = 0,
    kEdsFileCreateDisposition_CreateAlways ,
    kEdsFileCreateDisposition_OpenExisting ,
    kEdsFileCreateDisposition_OpenAlways ,
    kEdsFileCreateDisposition_TruncateExsisting ,
} EdsFileCreateDisposition;
typedef enum
{
    kEdsImageType_Unknown = 0x00000000,
    kEdsImageType_Jpeg = 0x00000001,
    kEdsImageType_CRW = 0x00000002,
    kEdsImageType_RAW = 0x00000004,
    kEdsImageType_CR2 = 0x00000006,
    kEdsImageType_HEIF = 0x00000008,
} EdsImageType;
typedef enum
{
    kEdsImageSize_Large = 0,
    kEdsImageSize_Middle = 1,
    kEdsImageSize_Small = 2,
    kEdsImageSize_Middle1 = 5,
    kEdsImageSize_Middle2 = 6,
    kEdsImageSize_Small1 = 14,
    kEdsImageSize_Small2 = 15,
    kEdsImageSize_Small3 = 16,
 kEdsImageSize_Unknown = 0xffffffff,
} EdsImageSize;
typedef enum
{
    kEdsCompressQuality_Normal = 2,
    kEdsCompressQuality_Fine = 3,
    kEdsCompressQuality_Lossless = 4,
    kEdsCompressQuality_SuperFine = 5,
    kEdsCompressQuality_Unknown = 0xffffffff,
} EdsCompressQuality;
typedef enum
{
    EdsImageQuality_LJ = 0x0010ff0f,
    EdsImageQuality_MJ = 0x0110ff0f,
    EdsImageQuality_M1J = 0x0510ff0f,
    EdsImageQuality_M1F = 0x0513FF0F,
    EdsImageQuality_M1N = 0x0512FF0F,
    EdsImageQuality_M2J = 0x0610ff0f,
    EdsImageQuality_M2F = 0x0613FF0F,
    EdsImageQuality_M2N = 0x0612FF0F,
    EdsImageQuality_SJ = 0x0210ff0f,
    EdsImageQuality_S1J = 0x0e10ff0f,
    EdsImageQuality_S2J = 0x0f10ff0f,
    EdsImageQuality_LJF = 0x0013ff0f,
    EdsImageQuality_LJN = 0x0012ff0f,
    EdsImageQuality_MJF = 0x0113ff0f,
    EdsImageQuality_MJN = 0x0112ff0f,
    EdsImageQuality_SJF = 0x0213ff0f,
    EdsImageQuality_SJN = 0x0212ff0f,
    EdsImageQuality_S1JF = 0x0E13ff0f,
    EdsImageQuality_S1JN = 0x0E12ff0f,
    EdsImageQuality_S2JF = 0x0F13ff0f,
    EdsImageQuality_S3JF = 0x1013ff0f,
    EdsImageQuality_LR = 0x0064ff0f,
    EdsImageQuality_LRLJF = 0x00640013,
    EdsImageQuality_LRLJN = 0x00640012,
    EdsImageQuality_LRMJF = 0x00640113,
    EdsImageQuality_LRMJN = 0x00640112,
    EdsImageQuality_LRSJF = 0x00640213,
    EdsImageQuality_LRSJN = 0x00640212,
    EdsImageQuality_LRS1JF = 0x00640E13,
    EdsImageQuality_LRS1JN = 0x00640E12,
    EdsImageQuality_LRS2JF = 0x00640F13,
    EdsImageQuality_LRS3JF = 0x00641013,
    EdsImageQuality_LRLJ = 0x00640010,
    EdsImageQuality_LRMJ = 0x00640110,
    EdsImageQuality_LRM1J = 0x00640510,
    EdsImageQuality_LRM1F = 0x00640513,
    EdsImageQuality_LRM1N = 0x00640512,
    EdsImageQuality_LRM2J = 0x00640610,
    EdsImageQuality_LRM2F = 0x00640613,
    EdsImageQuality_LRM2N = 0x00640612,
    EdsImageQuality_LRSJ = 0x00640210,
    EdsImageQuality_LRS1J = 0x00640e10,
    EdsImageQuality_LRS2J = 0x00640f10,
    EdsImageQuality_MR = 0x0164ff0f,
    EdsImageQuality_MRLJF = 0x01640013,
    EdsImageQuality_MRLJN = 0x01640012,
    EdsImageQuality_MRMJF = 0x01640113,
    EdsImageQuality_MRMJN = 0x01640112,
    EdsImageQuality_MRSJF = 0x01640213,
    EdsImageQuality_MRSJN = 0x01640212,
    EdsImageQuality_MRS1JF = 0x01640E13,
    EdsImageQuality_MRS1JN = 0x01640E12,
    EdsImageQuality_MRS2JF = 0x01640F13,
    EdsImageQuality_MRS3JF = 0x01641013,
    EdsImageQuality_MRLJ = 0x01640010,
    EdsImageQuality_MRM1J = 0x01640510,
    EdsImageQuality_MRM1F = 0x01640513,
    EdsImageQuality_MRM1N = 0x01640512,
    EdsImageQuality_MRM2J = 0x01640610,
    EdsImageQuality_MRM2F = 0x01640613,
    EdsImageQuality_MRM2N = 0x01640612,
    EdsImageQuality_MRSJ = 0x01640210,
    EdsImageQuality_SR = 0x0264ff0f,
    EdsImageQuality_SRLJF = 0x02640013,
    EdsImageQuality_SRLJN = 0x02640012,
    EdsImageQuality_SRMJF = 0x02640113,
    EdsImageQuality_SRMJN = 0x02640112,
    EdsImageQuality_SRSJF = 0x02640213,
    EdsImageQuality_SRSJN = 0x02640212,
    EdsImageQuality_SRS1JF = 0x02640E13,
    EdsImageQuality_SRS1JN = 0x02640E12,
    EdsImageQuality_SRS2JF = 0x02640F13,
    EdsImageQuality_SRS3JF = 0x02641013,
    EdsImageQuality_SRLJ = 0x02640010,
    EdsImageQuality_SRM1J = 0x02640510,
    EdsImageQuality_SRM1F = 0x02640513,
    EdsImageQuality_SRM1N = 0x02640512,
    EdsImageQuality_SRM2J = 0x02640610,
    EdsImageQuality_SRM2F = 0x02640613,
    EdsImageQuality_SRM2N = 0x02640612,
    EdsImageQuality_SRSJ = 0x02640210,
    EdsImageQuality_CR = 0x0063ff0f,
    EdsImageQuality_CRLJF = 0x00630013,
    EdsImageQuality_CRMJF = 0x00630113,
    EdsImageQuality_CRM1JF = 0x00630513,
    EdsImageQuality_CRM2JF = 0x00630613,
    EdsImageQuality_CRSJF = 0x00630213,
    EdsImageQuality_CRS1JF = 0x00630E13,
    EdsImageQuality_CRS2JF = 0x00630F13,
    EdsImageQuality_CRS3JF = 0x00631013,
    EdsImageQuality_CRLJN = 0x00630012,
    EdsImageQuality_CRMJN = 0x00630112,
    EdsImageQuality_CRM1JN = 0x00630512,
    EdsImageQuality_CRM2JN = 0x00630612,
    EdsImageQuality_CRSJN = 0x00630212,
    EdsImageQuality_CRS1JN = 0x00630E12,
    EdsImageQuality_CRLJ = 0x00630010,
    EdsImageQuality_CRMJ = 0x00630110,
    EdsImageQuality_CRM1J = 0x00630510,
    EdsImageQuality_CRM2J = 0x00630610,
    EdsImageQuality_CRSJ = 0x00630210,
    EdsImageQuality_CRS1J = 0x00630e10,
    EdsImageQuality_CRS2J = 0x00630f10,
    EdsImageQuality_HEIFL = 0x0080ff0f,
    EdsImageQuality_HEIFM = 0x0180ff0f,
    EdsImageQuality_HEIFM1 = 0x0580FF0F,
    EdsImageQuality_HEIFM2 = 0x0680FF0F,
    EdsImageQuality_HEIFLF = 0x0083ff0f,
    EdsImageQuality_HEIFLN = 0x0082ff0f,
    EdsImageQuality_HEIFMF = 0x0183ff0f,
    EdsImageQuality_HEIFMN = 0x0182ff0f,
    EdsImageQuality_HEIFS1 = 0x0e80ff0f,
    EdsImageQuality_HEIFS1F = 0x0e83ff0f,
    EdsImageQuality_HEIFS1N = 0x0e82ff0f,
    EdsImageQuality_HEIFS2 = 0x0f80ff0f,
    EdsImageQuality_HEIFS2F = 0x0f83ff0f,
    EdsImageQuality_RHEIFL = 0x00640080,
    EdsImageQuality_RHEIFLF = 0x00640083,
    EdsImageQuality_RHEIFLN = 0x00640082,
    EdsImageQuality_RHEIFM = 0x00640180,
    EdsImageQuality_RHEIFM1 = 0x00640580,
    EdsImageQuality_RHEIFM2 = 0x00640680,
    EdsImageQuality_RHEIFMF = 0x00640183,
    EdsImageQuality_RHEIFMN = 0x00640182,
    EdsImageQuality_RHEIFS1 = 0x00640e80,
    EdsImageQuality_RHEIFS1F = 0x00640e83,
    EdsImageQuality_RHEIFS1N = 0x00640e82,
    EdsImageQuality_RHEIFS2 = 0x00640f80,
    EdsImageQuality_RHEIFS2F = 0x00640f83,
    EdsImageQuality_CRHEIFL = 0x00630080,
    EdsImageQuality_CRHEIFLF = 0x00630083,
    EdsImageQuality_CRHEIFLN = 0x00630082,
    EdsImageQuality_CRHEIFM = 0x00630180,
    EdsImageQuality_CRHEIFMF = 0x00630183,
    EdsImageQuality_CRHEIFMN = 0x00630182,
    EdsImageQuality_CRHEIFM1 = 0x00630580,
    EdsImageQuality_CRHEIFM2 = 0x00630680,
    EdsImageQuality_CRHEIFS1 = 0x00630e80,
    EdsImageQuality_CRHEIFS1F = 0x00630e83,
    EdsImageQuality_CRHEIFS1N = 0x00630e82,
    EdsImageQuality_CRHEIFS2 = 0x00630f80,
    EdsImageQuality_CRHEIFS2F = 0x00630f83,
    EdsImageQuality_Unknown = 0xffffffff,
}EdsImageQuality;
typedef enum
{
    kEdsImageSrc_FullView = 0 ,
    kEdsImageSrc_Thumbnail ,
    kEdsImageSrc_Preview ,
    kEdsImageSrc_RAWThumbnail ,
    kEdsImageSrc_RAWFullView ,
} EdsImageSource;
typedef enum
{
    kEdsTargetImageType_Unknown = 0x00000000,
    kEdsTargetImageType_Jpeg = 0x00000001,
    kEdsTargetImageType_TIFF = 0x00000007,
    kEdsTargetImageType_TIFF16 = 0x00000008,
    kEdsTargetImageType_RGB = 0x00000009,
    kEdsTargetImageType_RGB16 = 0x0000000A,
    kEdsTargetImageType_DIB = 0x0000000B
} EdsTargetImageType;
typedef enum
{
    kEdsProgressOption_NoReport = 0,
    kEdsProgressOption_Done ,
    kEdsProgressOption_Periodically ,
} EdsProgressOption;
typedef enum
{
    kEdsFileAttribute_Normal = 0x00000000,
    kEdsFileAttribute_ReadOnly = 0x00000001,
    kEdsFileAttribute_Hidden = 0x00000002,
    kEdsFileAttribute_System = 0x00000004,
    kEdsFileAttribute_Archive = 0x00000020,
} EdsFileAttributes;
typedef enum
{
   kEdsObjectFormat_Unknown = 0x00000000,
   kEdsObjectFormat_Jpeg = 0x3801,
   kEdsObjectFormat_CR2 = 0xB103,
   kEdsObjectFormat_MP4 = 0xB982,
   kEdsObjectFormat_CR3 = 0xB108,
   kEdsObjectFormat_HEIF_CODE = 0xB10B,
} EdsObjectFormat;
typedef enum
{
   kEdsBatteryLevel2_Empty = 0,
   kEdsBatteryLevel2_Low = 9,
   kEdsBatteryLevel2_Half = 49,
   kEdsBatteryLevel2_Normal = 80,
   kEdsBatteryLevel2_Hi = 69,
   kEdsBatteryLevel2_Quarter = 19,
   kEdsBatteryLevel2_Error = 0,
   kEdsBatteryLevel2_BCLevel = 0,
   kEdsBatteryLevel2_AC = 0xFFFFFFFF,
   kEdsBatteryLevel2_Unknown = 0xFFFFFFFE,
} EdsBatteryLevel2;
typedef enum
{
    kEdsSaveTo_Camera = 1,
    kEdsSaveTo_Host = 2,
    kEdsSaveTo_Both = kEdsSaveTo_Camera | kEdsSaveTo_Host,
} EdsSaveTo;
typedef enum
{
    kEdsStorageType_Non = 0,
    kEdsStorageType_CF = 1,
    kEdsStorageType_SD = 2,
    kEdsStorageType_HD = 4,
    kEdsStorageType_CFast = 5,
    kEdsStorageType_CFe = 7,
} EdsStorageType;
typedef enum
{
    kEdsWhiteBalance_Auto = 0,
    kEdsWhiteBalance_Daylight = 1,
    kEdsWhiteBalance_Cloudy = 2,
    kEdsWhiteBalance_Tungsten = 3,
    kEdsWhiteBalance_Fluorescent = 4,
    kEdsWhiteBalance_Strobe = 5,
    kEdsWhiteBalance_WhitePaper = 6,
    kEdsWhiteBalance_Shade = 8,
    kEdsWhiteBalance_ColorTemp = 9,
    kEdsWhiteBalance_PCSet1 = 10,
    kEdsWhiteBalance_PCSet2 = 11,
    kEdsWhiteBalance_PCSet3 = 12,
 kEdsWhiteBalance_WhitePaper2 = 15,
 kEdsWhiteBalance_WhitePaper3 = 16,
 kEdsWhiteBalance_WhitePaper4 = 18,
 kEdsWhiteBalance_WhitePaper5 = 19,
    kEdsWhiteBalance_PCSet4 = 20,
    kEdsWhiteBalance_PCSet5 = 21,
 kEdsWhiteBalance_AwbWhite = 23,
 kEdsWhiteBalance_Click = -1,
    kEdsWhiteBalance_Pasted = -2,
} EdsWhiteBalance;
typedef enum
{
    kEdsColorSpace_sRGB = 1,
    kEdsColorSpace_AdobeRGB = 2,
    kEdsColorSpace_Unknown = 0xffffffff,
} EdsColorSpace;
typedef enum
{
    kEdsPictureStyle_Standard = 0x0081,
    kEdsPictureStyle_Portrait = 0x0082,
    kEdsPictureStyle_Landscape = 0x0083,
    kEdsPictureStyle_Neutral = 0x0084,
    kEdsPictureStyle_Faithful = 0x0085,
    kEdsPictureStyle_Monochrome = 0x0086,
    kEdsPictureStyle_Auto = 0x0087,
 kEdsPictureStyle_FineDetail = 0x0088,
 kEdsPictureStyle_User1 = 0x0021,
    kEdsPictureStyle_User2 = 0x0022,
    kEdsPictureStyle_User3 = 0x0023,
    kEdsPictureStyle_PC1 = 0x0041,
    kEdsPictureStyle_PC2 = 0x0042,
    kEdsPictureStyle_PC3 = 0x0043,
} EdsPictureStyle;
typedef enum
{
    kEdsTransferOption_ByDirectTransfer = 1,
    kEdsTransferOption_ByRelease = 2,
    kEdsTransferOption_ToDesktop = 0x00000100,
} EdsTransferOption;
typedef enum
{
    kEdsAEMode_Program = 0x00 ,
    kEdsAEMode_Tv = 0x01,
    kEdsAEMode_Av = 0x02,
    kEdsAEMode_Manual = 0x03,
    kEdsAEMode_Bulb = 0x04,
    kEdsAEMode_A_DEP = 0x05,
    kEdsAEMode_DEP = 0x06,
    kEdsAEMode_Custom = 0x07,
    kEdsAEMode_Lock = 0x08,
    kEdsAEMode_Green = 0x09,
    kEdsAEMode_NightPortrait = 0x0A,
    kEdsAEMode_Sports = 0x0B,
    kEdsAEMode_Portrait = 0x0C,
    kEdsAEMode_Landscape = 0x0D,
    kEdsAEMode_Closeup = 0x0E,
    kEdsAEMode_FlashOff = 0x0F,
    kEdsAEMode_CreativeAuto = 0x13,
 kEdsAEMode_Movie = 0x14,
 kEdsAEMode_PhotoInMovie = 0x15,
 kEdsAEMode_SceneIntelligentAuto = 0x16,
 kEdsAEMode_SCN = 0x19,
 kEdsAEMode_NightScenes = 0x17,
 kEdsAEMode_BacklitScenes = 0x18,
 kEdsAEMode_Children = 0x1A,
 kEdsAEMode_Food = 0x1B,
 kEdsAEMode_CandlelightPortraits = 0x1C,
 kEdsAEMode_CreativeFilter = 0x1D,
 kEdsAEMode_RoughMonoChrome = 0x1E,
 kEdsAEMode_SoftFocus = 0x1F,
 kEdsAEMode_ToyCamera = 0x20,
 kEdsAEMode_Fisheye = 0x21,
 kEdsAEMode_WaterColor = 0x22,
 kEdsAEMode_Miniature = 0x23,
 kEdsAEMode_Hdr_Standard = 0x24,
 kEdsAEMode_Hdr_Vivid = 0x25,
 kEdsAEMode_Hdr_Bold = 0x26,
 kEdsAEMode_Hdr_Embossed = 0x27,
 kEdsAEMode_Movie_Fantasy = 0x28,
 kEdsAEMode_Movie_Old = 0x29,
 kEdsAEMode_Movie_Memory = 0x2A,
 kEdsAEMode_Movie_DirectMono = 0x2B,
 kEdsAEMode_Movie_Mini = 0x2C,
    kEdsAEMode_PanningAssist = 0x2D,
    kEdsAEMode_GroupPhoto = 0x2E,
    kEdsAEMode_Myself = 0x32,
 kEdsAEMode_PlusMovieAuto = 0x33,
    kEdsAEMode_SmoothSkin = 0x34,
 kEdsAEMode_Panorama = 0x35,
    kEdsAEMode_Silent = 0x36,
    kEdsAEMode_Flexible = 0x37,
 kEdsAEMode_OilPainting = 0x38,
 kEdsAEMode_Fireworks = 0x39,
 kEdsAEMode_StarPortrait = 0x3A,
    kEdsAEMode_StarNightscape = 0x3B,
 kEdsAEMode_StarTrails = 0x3C,
 kEdsAEMode_StarTimelapseMovie = 0x3D,
 kEdsAEMode_BackgroundBlur = 0x3E,
    kEdsAEMode_VideoBlog = 0x3F,
 kEdsAEMode_Unknown = 0xffffffff,
} EdsAEMode;
typedef enum
{
    kEdsBracket_AEB = 0x01,
    kEdsBracket_ISOB = 0x02,
    kEdsBracket_WBB = 0x04,
    kEdsBracket_FEB = 0x08,
    kEdsBracket_Unknown = 0xffffffff,
} EdsBracket;
typedef enum
{
 kEdsEvfOutputDevice_TFT = 1,
 kEdsEvfOutputDevice_PC = 2,
 kEdsEvfOutputDevice_PC_Small = 8,
} EdsEvfOutputDevice;
typedef enum
{
 kEdsEvfZoom_Fit = 1,
 kEdsEvfZoom_x5 = 5,
 kEdsEvfZoom_x6 = 6,
 kEdsEvfZoom_x10 = 10,
 kEdsEvfZoom_x15 = 15,
} EdsEvfZoom;
typedef enum
{
 Evf_AFMode_Quick = 0x00,
 Evf_AFMode_Live = 0x01,
 Evf_AFMode_LiveFace = 0x02,
 Evf_AFMode_LiveMulti = 0x03,
 Evf_AFMode_LiveZone = 0x04,
 Evf_AFMode_LiveSingleExpandCross = 0x05,
 Evf_AFMode_LiveSingleExpandAround = 0x06,
 Evf_AFMode_LiveZoneLargeH = 0x07,
 Evf_AFMode_LiveZoneLargeV = 0x08,
 Evf_AFMode_LiveCatchAF = 0x09,
 Evf_AFMode_LiveSpotAF = 0x0a,
 Evf_AFMode_FlexibleZone1 = 0x0b,
 Evf_AFMode_FlexibleZone2 = 0x0c,
 Evf_AFMode_FlexibleZone3 = 0x0d,
 Evf_AFMode_WholeArea = 0x0e,
 Evf_AFMode_NoTraking_Spot = 0x0f,
 Evf_AFMode_NoTraking_1Point = 0x10,
 Evf_AFMode_NoTraking_ExpandCross = 0x11,
 Evf_AFMode_NoTraking_ExpandAround = 0x12,
} EdsEvfAFMode;
typedef enum
{
 kEdsStroboModeInternal = 0,
 kEdsStroboModeExternalETTL = 1,
 kEdsStroboModeExternalATTL = 2,
 kEdsStroboModeExternalTTL = 3,
 kEdsStroboModeExternalAuto = 4,
 kEdsStroboModeExternalManual = 5,
 kEdsStroboModeManual = 6,
}EdsStroboMode;
typedef enum
{
 kEdsETTL2ModeEvaluative = 0,
 kEdsETTL2ModeAverage = 1,
}EdsETTL2Mode;
typedef enum
{
 kEdsDcStrobeAuto = 0,
 kEdsDcStrobeOn = 1,
 kEdsDcStrobeSlowsynchro = 2,
 kEdsDcStrobeOff = 3,
}EdsDcStrobe;
typedef enum
{
 kDcLensBarrelStateInner = 0,
 kDcLensBarrelStateOuter = 1,
}EdsDcLensBarrelState;
typedef enum
{
 kDcRemoteShootingModeStop = 0,
 kDcRemoteShootingModeStart = 1,
}EdsDcRemoteShootingMode;
typedef enum
{
    kEdsMirrorLockupStateDisable = 0,
    kEdsMirrorLockupStateEnable = 1,
    kEdsMirrorLockupStateDuringShooting = 2,
}EdsMirrorLockupState;
typedef enum
{
    kEdsMirrorUpSettingOff = 0,
    kEdsMirrorUpSettingOn = 1,
}EdsMirrorUpSetting;
typedef struct tagEdsPoint
{
    EdsInt32 x;
    EdsInt32 y;
} EdsPoint;
typedef struct tagEdsSize
{
    EdsInt32 width;
    EdsInt32 height;
} EdsSize;
typedef struct tagEdsRect
{
    EdsPoint point;
    EdsSize size;
} EdsRect;
typedef struct tagEdsRational
{
    EdsInt32 numerator;
    EdsUInt32 denominator;
} EdsRational;
typedef struct tagEdsTime
{
    EdsUInt32 year;
    EdsUInt32 month;
    EdsUInt32 day;
    EdsUInt32 hour;
    EdsUInt32 minute;
    EdsUInt32 second;
    EdsUInt32 milliseconds;
} EdsTime;
typedef struct tagEdsGpsMetaData
{
    EdsUInt8 latitudeRef;
    EdsUInt8 longitudeRef;
    EdsUInt8 altitudeRef;
    EdsUInt8 status;
    EdsRational latitude[3];
    EdsRational longitude[3];
    EdsRational altitude;
    EdsRational timeStamp[3];
    EdsUInt16 dateStampYear;
    EdsUInt8 dateStampMonth;
    EdsUInt8 dateStampDay;
} EdsGpsMetaData;
typedef struct tagEdsDeviceInfo
{
    EdsChar szPortName[ 256 ];
    EdsChar szDeviceDescription[ 256 ];
    EdsUInt32 deviceSubType;
 EdsUInt32 reserved;
} EdsDeviceInfo;
typedef struct tagEdsVolumeInfo
{
    EdsUInt32 storageType;
    EdsAccess access;
    EdsUInt64 maxCapacity;
    EdsUInt64 freeSpaceInBytes;
    EdsChar szVolumeLabel[ 256 ];
} EdsVolumeInfo;
typedef struct tagEdsDirectoryItemInfo
{
    EdsUInt64 size;
    EdsBool isFolder;
    EdsUInt32 groupID;
    EdsUInt32 option;
    EdsChar szFileName[ 256 ];
 EdsUInt32 format;
 EdsUInt32 dateTime;
} EdsDirectoryItemInfo;
typedef struct tagEdsImageInfo
{
    EdsUInt32 width;
    EdsUInt32 height;
    EdsUInt32 numOfComponents;
    EdsUInt32 componentDepth;
    EdsRect effectiveRect;
    EdsUInt32 reserved1;
    EdsUInt32 reserved2;
} EdsImageInfo;
typedef struct tagEdsSaveImageSetting
{
    EdsUInt32 JPEGQuality;
    EdsStreamRef iccProfileStream;
    EdsUInt32 reserved;
} EdsSaveImageSetting;
typedef struct tagEdsPropertyDesc
{
    EdsInt32 form;
    EdsInt32 access;
    EdsInt32 numElements;
    EdsInt32 propDesc[128];
} EdsPropertyDesc;
typedef struct tagEdsPictureStyleDesc
{
    EdsInt32 contrast;
    EdsUInt32 sharpness;
    EdsInt32 saturation;
    EdsInt32 colorTone;
    EdsUInt32 filterEffect;
    EdsUInt32 toningEffect;
 EdsUInt32 sharpFineness;
 EdsUInt32 sharpThreshold;
} EdsPictureStyleDesc;
typedef struct tagEdsFrameDesc
{
    EdsUInt32 valid;
 EdsUInt32 selected;
    EdsUInt32 justFocus;
    EdsRect rect;
    EdsUInt32 reserved;
} EdsFocusPoint;
typedef struct tagEdsFocusInfo
{
    EdsRect imageRect;
    EdsUInt32 pointNumber;
    EdsFocusPoint focusPoint[1053];
 EdsUInt32 executeMode;
} EdsFocusInfo;
typedef struct tagEdsUsersetData
{
    EdsUInt32 valid;
    EdsUInt32 dataSize;
    EdsChar szCaption[32];
    EdsUInt8 data[1];
} EdsUsersetData;
typedef struct tagEdsCapacity
{
    EdsInt32 numberOfFreeClusters;
    EdsInt32 bytesPerSector;
    EdsBool reset;
} EdsCapacity;
typedef struct tagEdsFramePoint
{
 EdsInt32 x;
 EdsInt32 y;
} EdsFramePoint;
typedef struct tagEdsCameraPos
{
    EdsInt32 status;
    EdsInt32 position;
    EdsInt32 rolling;
    EdsInt32 pitching;
} EdsCameraPos;
typedef struct tagEdsFocusShiftSet
{
 EdsInt32 version;
 EdsInt32 focusShiftFunction;
 EdsInt32 shootingNumber;
 EdsInt32 stepWidth;
 EdsInt32 exposureSmoothing;
 EdsInt32 focusStackingFunction;
 EdsInt32 focusStackingTrimming;
 EdsInt32 flashInterval;
} EdsFocusShiftSet;
typedef struct tagEdsManualWBData
{
    EdsInt32 valid;
    EdsInt32 dataSize;
    EdsChar szCaption[32];
    EdsInt8 data[8];
} EdsManualWBData;
typedef struct tagApertureLockSetting
{
    EdsUInt32 apertureLockStatus;
    EdsUInt32 avValue;
} ApertureLockSetting;
typedef EdsError ( *EdsProgressCallback )(
                    EdsUInt32 inPercent,
                    EdsVoid * inContext,
                    EdsBool * outCancel );
typedef EdsError ( *EdsCameraAddedHandler )(
                    EdsVoid *inContext );
typedef EdsError ( *EdsPropertyEventHandler )(
                    EdsPropertyEvent inEvent,
                    EdsPropertyID inPropertyID,
                    EdsUInt32 inParam,
                    EdsVoid * inContext );
typedef EdsError ( *EdsObjectEventHandler )(
                    EdsObjectEvent inEvent,
                    EdsBaseRef inRef,
                    EdsVoid * inContext );
typedef EdsError ( *EdsStateEventHandler )(
                    EdsStateEvent inEvent,
                    EdsUInt32 inEventData,
                    EdsVoid * inContext );
typedef EdsError EdsReadStream (void *inContext, EdsUInt32 inReadSize, EdsVoid* outBuffer, EdsUInt32* outReadSize);
typedef EdsError EdsWriteStream (void *inContext, EdsUInt32 inWriteSize, const EdsVoid* inBuffer, EdsUInt32* outWrittenSize);
typedef EdsError EdsSeekStream (void *inContext, EdsInt32 inSeekOffset, EdsSeekOrigin inSeekOrigin);
typedef EdsError EdsTellStream (void *inContext, EdsInt32 *outPosition);
typedef EdsError EdsGetStreamLength (void *inContext, EdsUInt32 *outLength);
typedef struct
{
    void *context;
    EdsReadStream *read;
    EdsWriteStream *write;
    EdsSeekStream *seek;
    EdsTellStream *tell;
    EdsGetStreamLength *getLength;
} EdsIStream;
#pragma pack (pop)
EdsError EdsInitializeSDK();
EdsError EdsTerminateSDK();
EdsUInt32 EdsRetain( EdsBaseRef inRef );
EdsUInt32 EdsRelease( EdsBaseRef inRef );
EdsError EdsGetChildCount( EdsBaseRef inRef,
                                  EdsUInt32* outCount );
EdsError EdsGetChildAtIndex( EdsBaseRef inRef,
                                     EdsInt32 inIndex,
                                     EdsBaseRef* outRef );
EdsError EdsGetParent( EdsBaseRef inRef,
                               EdsBaseRef* outParentRef );
EdsError EdsGetPropertySize( EdsBaseRef inRef,
                                    EdsPropertyID inPropertyID,
                                    EdsInt32 inParam,
                                    EdsDataType* outDataType,
                                    EdsUInt32* outSize );
EdsError EdsGetPropertyData( EdsBaseRef inRef,
                                    EdsPropertyID inPropertyID,
                                    EdsInt32 inParam,
                                    EdsUInt32 inPropertySize,
                                    EdsVoid* outPropertyData );
EdsError EdsSetPropertyData( EdsBaseRef inRef,
                                    EdsPropertyID inPropertyID,
                                    EdsInt32 inParam,
                                    EdsUInt32 inPropertySize,
                                    const EdsVoid* inPropertyData );
EdsError EdsGetPropertyDesc( EdsBaseRef inRef,
                                    EdsPropertyID inPropertyID,
                                    EdsPropertyDesc* outPropertyDesc );
EdsError EdsGetCameraList( EdsCameraListRef* outCameraListRef );
EdsError EdsGetDeviceInfo( EdsCameraRef inCameraRef,
                                  EdsDeviceInfo* outDeviceInfo );
EdsError EdsOpenSession( EdsCameraRef inCameraRef );
EdsError EdsCloseSession( EdsCameraRef inCameraRef );
EdsError EdsSendCommand( EdsCameraRef inCameraRef,
                                EdsCameraCommand inCommand,
                                EdsInt32 inParam );
EdsError EdsSendStatusCommand(
                    EdsCameraRef inCameraRef,
                    EdsCameraStatusCommand inStatusCommand,
                    EdsInt32 inParam );
EdsError EdsSetCapacity( EdsCameraRef inCameraRef,
                                EdsCapacity inCapacity );
EdsError EdsGetVolumeInfo( EdsVolumeRef inVolumeRef,
                                  EdsVolumeInfo* outVolumeInfo );
EdsError EdsFormatVolume( EdsVolumeRef inVolumeRef );
EdsError EdsGetDirectoryItemInfo(
                                EdsDirectoryItemRef inDirItemRef,
                                EdsDirectoryItemInfo* outDirItemInfo );
EdsError EdsDeleteDirectoryItem( EdsDirectoryItemRef inDirItemRef );
EdsError EdsDownload( EdsDirectoryItemRef inDirItemRef,
                                         EdsUInt64 inReadSize,
                                         EdsStreamRef outStream );
EdsError EdsDownloadCancel( EdsDirectoryItemRef inDirItemRef );
EdsError EdsDownloadComplete( EdsDirectoryItemRef inDirItemRef );
EdsError EdsDownloadThumbnail( EdsDirectoryItemRef inDirItemRef,
                                        EdsStreamRef outStream );
EdsError EdsGetAttribute( EdsDirectoryItemRef inDirItemRef,
                                    EdsFileAttributes* outFileAttribute );
EdsError EdsSetAttribute(
                            EdsDirectoryItemRef inDirItemRef,
                            EdsFileAttributes inFileAttribute );
EdsError EdsSetMetaImage( EdsDirectoryItemRef inDirItemRef,
                                EdsUInt32 inMetaType,
                                EdsUInt32 inMetaDataSize,
                                const EdsVoid* inMetaData );
EdsError EdsCreateFileStream(
                            const EdsChar* inFileName,
                            EdsFileCreateDisposition inCreateDisposition,
                            EdsAccess inDesiredAccess,
                            EdsStreamRef* outStream );
EdsError EdsCreateMemoryStream(
                            EdsUInt64 inBufferSize,
                            EdsStreamRef* outStream );
EdsError EdsCreateFileStreamEx(
        const WCHAR* inFileName,
       EdsFileCreateDisposition inCreateDisposition,
       EdsAccess inDesiredAccess,
       EdsStreamRef* outStream );
EdsError EdsCreateMemoryStreamFromPointer(
                EdsVoid* inUserBuffer,
                EdsUInt64 inBufferSize,
                EdsStreamRef* outStream );
EdsError EdsGetPointer(
                EdsStreamRef inStream,
                EdsVoid** outPointer );
EdsError EdsRead(
                EdsStreamRef inStreamRef,
                EdsUInt64 inReadSize,
                EdsVoid* outBuffer,
                EdsUInt64* outReadSize );
EdsError EdsWrite(
                EdsStreamRef inStreamRef,
                EdsUInt64 inWriteSize,
                const EdsVoid* inBuffer,
                EdsUInt64* outWrittenSize );
EdsError EdsSeek(
                EdsStreamRef inStreamRef,
                EdsInt64 inSeekOffset,
                EdsSeekOrigin inSeekOrigin );
EdsError EdsGetPosition(
                EdsStreamRef inStreamRef,
                EdsUInt64* outPosition );
EdsError EdsGetLength(
                EdsStreamRef inStreamRef,
                EdsUInt64* outLength );
EdsError EdsCopyData(
                EdsStreamRef inStreamRef,
                EdsUInt64 inWriteSize,
                EdsStreamRef outStreamRef );
EdsError EdsSetProgressCallback(
                EdsBaseRef inRef,
                EdsProgressCallback inProgressCallback,
                EdsProgressOption inProgressOption,
                EdsVoid* inContext );
EdsError EdsCreateImageRef( EdsStreamRef inStreamRef,
                                    EdsImageRef* outImageRef );
EdsError EdsGetImageInfo( EdsImageRef inImageRef,
                                  EdsImageSource inImageSource,
                                  EdsImageInfo* outImageInfo );
EdsError EdsGetImage(
        EdsImageRef inImageRef,
        EdsImageSource inImageSource,
        EdsTargetImageType inImageType,
        EdsRect inSrcRect,
        EdsSize inDstSize,
        EdsStreamRef outStreamRef );
EdsError EdsCreateEvfImageRef (
     EdsStreamRef inStreamRef,
     EdsEvfImageRef *outEvfImageRef ) ;
EdsError EdsDownloadEvfImage ( EdsCameraRef inCameraRef,
    EdsEvfImageRef inEvfImageRef ) ;
EdsError EdsSetCameraAddedHandler(
            EdsCameraAddedHandler inCameraAddedHandler,
            EdsVoid* inContext );
EdsError EdsSetPropertyEventHandler(
            EdsCameraRef inCameraRef,
            EdsPropertyEvent inEvnet,
            EdsPropertyEventHandler inPropertyEventHandler,
            EdsVoid* inContext );
EdsError EdsSetObjectEventHandler(
            EdsCameraRef inCameraRef,
            EdsObjectEvent inEvnet,
            EdsObjectEventHandler inObjectEventHandler,
            EdsVoid* inContext );
EdsError EdsSetCameraStateEventHandler(
            EdsCameraRef inCameraRef,
            EdsStateEvent inEvnet,
            EdsStateEventHandler inStateEventHandler,
            EdsVoid* inContext );
EdsError EdsCreateStream(EdsIStream* inStream, EdsStreamRef* outStreamRef);
EdsError EdsGetEvent();
EdsError EdsSetFramePoint(EdsCameraRef inCameraRef, EdsPoint inFramepoint, _Bool inLockAfFrame);
