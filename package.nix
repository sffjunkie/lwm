{
  lib,
  stdenv,
}:
stdenv.mkDerivation {
  pname = "lwm";
  version = "0.1";

  src = ./src/lwm;

  installPhase = ''
    mkdir -p $out/lwm
    cp -r . $out/lwm/
  '';

  meta = {
    description = "Looniversity Qtile configuration";
    homepage = "https://github.com/sffjunkie/lwm";
    license = lib.licenses.asl20;
  };
}
