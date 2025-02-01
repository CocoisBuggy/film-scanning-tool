{
  pkgs ? import <nixpkgs> { },
}:
let
  libraries = with pkgs; [
    glib
    glib.dev
    stdenv.cc.cc.lib
    clang
    clang.libc
    libusb1
  ];

  python = pkgs.python3; # Use Python 3
  stdenv = pkgs.stdenv; # Standard environment
  edsdkLib = ./lib/libEDSDK.so; # Path to your pre-built libEDSDK.so
  LD_LIBRARY_PATH = "${pkgs.lib.makeLibraryPath libraries}:${edsdkLib}";
in
pkgs.stdenv.mkDerivation rec {
  inherit LD_LIBRARY_PATH;
  pname = "edsdk_py";
  version = "0.1.2";
  src = ./.;

  nativeBuildInputs =
    with pkgs;
    [
      gcc
      swig
      python
      python.pkgs.setuptools # For building the Python package
      patchelf
    ]
    ++ libraries;

  buildInputs = with pkgs; [
    python
    libusb1
  ];

  # Include paths for glibc and Python headers
  NIX_CFLAGS_COMPILE = "-I${pkgs.glibc.dev}/include -I${python}/include/python${python.pythonVersion}";

  configurePhase = ''
    echo "No configure step needed"
  '';

  buildPhase = ''
    # We preprocess the headers into one to quiet the many many errors
    gcc -I./include -E ./include/EDSDK.h -o ./include/EDSDK_preprocessed.h
    swig -python -o edsdk_wrap.c ./edsdk.i

    echo "BUILD TIME"

    # Compile the wrapper into a shared library
    $CC -fPIC -c edsdk_wrap.c -o edsdk_wrap.o $NIX_CFLAGS_COMPILE

    # Link the wrapper with libEDSDK.so
    $CC -shared edsdk_wrap.o -L./lib -lEDSDK -o _edsdk.so

    # Ensure that the shared library is properly linked by adding the path to libEDSDK.so
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$out/${python.sitePackages}/lib
  '';

  installPhase = ''
    mkdir -p $out/${python.sitePackages}
    cp edsdk.py _edsdk.so $out/${python.sitePackages}
    cp ${edsdkLib} $out/${python.sitePackages}/libEDSDK.so


    # Set RPATH to $ORIGIN so _edsdk.so finds libEDSDK.so in the same directory
    patchelf --set-rpath '$ORIGIN' $out/${python.sitePackages}/_edsdk.so
  '';

  meta = {
    description = "Python bindings for EDSDK";
    license = pkgs.lib.licenses.mit;
  };
}
