{
  pkgs ? import <nixpkgs> {
    config = {
      allowUnfree = true;
    };
  },
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
    virtualenv
    opencv
    pkg-config
    libusb1
    glibc
    cudatoolkit
    (python3.withPackages (
      ps: with ps; [
        textual
        watchdog
        matplotlib
        cffi
        inflection
        scikit-image
        (ps.opencv4.override {
          enableGtk3 = true;
        })
      ]
    ))
  ];

  shellHook = ''
    gcc -E -P ./include/EDSDK.h -o ./include/EDSDK_preprocessed.h
    echo "post GCC preprocessing"

    ${pkgs.virtualenv}/bin/virtualenv .venv
    source .venv/bin/activate

    export CUDA_PATH=${pkgs.cudatoolkit}
    export LD_LIBRARY_PATH=/run/opengl-driver/lib:${LD_LIBRARY_PATH}
    export EXTRA_LDFLAGS="-L/lib -L${pkgs.cudatoolkit}/lib"

    pip install torch numpy transformers accelerate timm
  '';
}
