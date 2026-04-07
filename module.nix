{
  config,
  pkgs,
  ...
}:
let
  cfg = config.looniversity.window_manager.qtile;

  inherit (pkgs.lib)
    mkEnableOption
    mkForce
    mkIf
    mkOption
    types
    ;
in
{
  options.looniversity.window_manager.qtile = {
    enable = mkEnableOption "Looniversity QTile";
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
    environment.sessionVariables = {
      MOZ_ENABLE_WAYLAND = "1";
      XDG_SESSION_TYPE = "wayland";
      XDG_CURRENT_DESKTOP = "qtile";
      SDL_VIDEODRIVER = "wayland,x11,windows";
      QT_QPA_PLATFORM = "wayland";
      QT_WAYLAND_DISABLE_WINDOWDECORATION = "1";
      _JAVA_AWT_WM_NONREPARENTING = "1";
    };

    systemd.user.services.qtile =
      let
        pyEnv = cfg.python.withPackages (
          ps:
          [
            ps.qtile
            ps.iwlib
          ]
          ++ (cfg.extraPythonPackages ps)
        );
      in
      {
        description = "Qtile - Wayland window manager";
        documentation = [ "man:qtile(5)" ];
        bindsTo = [ "graphical-session.target" ];
        wants = [ "graphical-session-pre.target" ];
        after = [ "graphical-session-pre.target" ];

        # We explicitly unset PATH here, as we want it to be set by
        # systemctl --user import-environment in startqtile
        environment.PATH = mkForce null;
        environment.PYTHONPATH = mkForce null;

        serviceConfig = {
          Type = "simple";
          ExecStart = "${pyEnv}/bin/qtile start --backend wayland --config ${pkgs.qtileconfig}";
          Restart = "on-failure";
          RestartSec = 1;
          TimeoutStopSec = 10;

          EnvironmentFile = mkIf (cfg.environmentFile != null) cfg.environmentFile;
        };
      };
  };
}
