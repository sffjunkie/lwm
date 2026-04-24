{
  config,
  lib,
  pkgs,
  ...
}:
let
  cfg = config.looniversity.desktop.window_manager.lwm;

  inherit (lib)
    mkEnableOption
    mkIf
    mkOption
    types
    ;
in
{
  options.looniversity.desktop.window_manager.lwm = {
    enable = mkEnableOption "qtile";
    configPath = mkOption {
      type = types.str;
      default = "lwm";
    };

    dev = mkOption {
      type = types.bool;
      default = false;
      description = "Use the devleopment version of lwm";
    };

    python = mkOption {
      type = types.package;
      default = pkgs.python3;
    };

    extraPythonPackages = mkOption {
      type = types.functionTo (types.listOf types.package);
      description = ''
        A function that returns a list of packages from a package set
        to be added to the default packages required by qtile.
      '';
    };

    environmentFile = mkOption {
      type = types.nullOr types.path;
      default = null;
      description = ''
        A systemd environment file to pass secrets needed by the qtile config.
      '';
    };
  };

  config = mkIf cfg.enable {
    looniversity.wayland.enable = true;
    looniversity.desktop.window_manager.lwm.dev = true;

    environment.sessionVariables = {
      XDG_SESSION_TYPE = "wayland";
      XDG_CURRENT_DESKTOP = "lwm";
    };

    systemd.user.services.lwm =
      let
        pyEnv = cfg.python.withPackages (
          ps:
          [
            ps.qtile
          ]
          ++ (cfg.extraPythonPackages ps)
        );
      in
      {
        description = "lwm - Looniversity window manager";
        documentation = [ "man:qtile(5)" ];
        bindsTo = [ "lde-session.target" ];
        wants = [ "lde-session.target" ];
        after = [ "lde-session.target" ];

        environment.PATH = lib.mkForce null;
        environment.PYTHONPATH = lib.mkForce null;

        serviceConfig = {
          Type = "simple";
          ExecStart = "${pyEnv}/bin/qtile start --backend wayland --config %h/.config/${config.looniversity.desktop.window_manager.lwm.configPath}";
          Restart = "on-failure";
          RestartSec = 1;
          TimeoutStopSec = 10;

          EnvironmentFile = mkIf (cfg.environmentFile != null) cfg.environmentFile;
        };
      };
  };
}
