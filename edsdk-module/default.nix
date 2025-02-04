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
python.pkgs.buildPythonPackage rec {
  pname = "edsdk";
  version = "0.1";

  src = ./.; # Use the current directory as source

  nativeBuildInputs = [
    python.pkgs.pybind11 # Provides Pybind11 headers
    python.pkgs.setuptools # Needed to install Python extensions
  ] ++ libraries;

  buildInputs = [
    python
    python.pkgs.pybind11
    stdenv.cc.cc
    pkgs.libdsk
    pkgs.patchelf
  ];

  # Ensure correct linking
  env.NIX_CFLAGS_COMPILE = "-I${python.pkgs.pybind11}/include -I./include";
  env.NIX_LDFLAGS = "-L${pkgs.libdsk}/lib -L./lib";

  # Specify how to build the module
  doCheck = false; # Skip tests for now

  # Install libEDSDK.so into the Python package's site-packages
  preInstall = ''
    mkdir -p $out/lib/python3.12/site-packages
    cp ${edsdkLib} $out/lib/python3.12/site-packages/libEDSDK.so
  '';

  # After installation, patch the Python shared library
  postInstall = ''
    # Use patchelf to link edsdk.so to the python shared object
    patchelf --set-rpath '$ORIGIN' $out/lib/python3.12/site-packages/edsdk.cpython-312-x86_64-linux-gnu.so
    patchelf --add-needed libEDSDK.so $out/lib/python3.12/site-packages/edsdk.cpython-312-x86_64-linux-gnu.so
  '';

  meta = {
    description = "Python bindings for Canon EDSDK using Pybind11";
    license = pkgs.lib.licenses.mit;
  };
}
