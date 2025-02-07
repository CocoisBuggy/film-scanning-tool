{
  pkgs ? import <nixpkgs> { },
}:
let
  inherit (pkgs) mkShell;

  libraries = with pkgs; [
    glib
    glib.dev
    stdenv.cc.cc.lib
    clang
    clang.libc
    libusb1
  ];

  LD_LIBRARY_PATH = "${pkgs.lib.makeLibraryPath libraries}";
in
mkShell {
  inherit LD_LIBRARY_PATH;
  buildInputs = with pkgs; [
    opencv
    pkg-config
    libusb1
    glibc
    libjpeg
    (python3.withPackages (
      ps: with ps; [
        matplotlib
        cffi
        inflection
        (ps.opencv4.override {
          enableGtk3 = true;
        })
      ]
    ))
  ];

  shellHook = ''
    gcc -E -P ./include/EDSDK.h -o ./include/EDSDK_preprocessed.h
    echo "post GCC preprocessing"
  '';
}
