with import <nixpkgs> { };
let
  edsdk = import ./edsdk-module { inherit pkgs; };
in
mkShell {
  LD_LIBRARY_PATH = "${lib.makeLibraryPath [
    libusb1
    stdenv.cc.cc
  ]}";
  buildInputs = [
    pre-commit
    uv

    edsdk
    (python3.withPackages (
      ps: with ps; [
        pybind11
      ]
    ))
  ];
}
