%module edsdk
%{
    #include <wchar.h>
    #include <stdbool.h>
    #include <Python.h>
    #include "./include/edsdk_fix.h"
    #include "./include/EDSDK_preprocessed.h"
%}

%include "./include/EDSDK_preprocessed.h"
