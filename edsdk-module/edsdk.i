%module edsdk
#include <wchar.h>
#include <stdint.i>

%{
    #include <wchar.h>
    #include <stdbool.h>
    #include "./include/edsdk_fix.h"
    #include "./include/EDSDK_preprocessed.h"
%}

%include "./include/EDSDK_preprocessed.h"
