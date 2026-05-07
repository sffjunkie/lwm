{
  description = "qtileconfig - QTile configuration";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";

    git-hooks = {
      url = "github:cachix/git-hooks.nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };

    pyproject-build-systems = {
      url = "github:pyproject-nix/build-system-pkgs";
      inputs.pyproject-nix.follows = "pyproject-nix";
      inputs.uv2nix.follows = "uv2nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };

    pyproject-nix = {
      url = "github:nix-community/pyproject.nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };

    uv2nix = {
      url = "github:pyproject-nix/uv2nix";
      inputs.pyproject-nix.follows = "pyproject-nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs =
    {
      git-hooks,
      nixpkgs,
      pyproject-build-systems,
      pyproject-nix,
      uv2nix,
      ...
    }:
    let
      inherit (nixpkgs) lib;

      forAllSystems = lib.genAttrs [
        "x86_64-linux"
      ];

      pyproject = pyproject-nix.lib.project.loadPyproject {
        projectRoot = ./.;
      };
      project_name = pyproject.pyproject.project.name;

      workspace = uv2nix.lib.workspace.loadWorkspace {
        workspaceRoot = ./.;
      };

      overlay = workspace.mkPyprojectOverlay {
        sourcePreference = "wheel";
      };

      pythonSets = forAllSystems (
        system:
        let
          pkgs = nixpkgs.legacyPackages.${system};
          python = pkgs.python3;
        in
        (pkgs.callPackage pyproject-nix.build.packages {
          inherit python;
        }).overrideScope
          (
            lib.composeManyExtensions [
              pyproject-build-systems.overlays.wheel
              overlay
            ]
          )
      );
    in
    {
      packages = forAllSystems (system: {
        # default = pythonSets.${system}.mkVirtualEnv "${project_name}-env" workspace.deps.default;
        default = pythonSets.${system}.callPackage ./package.nix { };
      });

      checks = forAllSystems (
        system:
        let
          pkgs = nixpkgs.legacyPackages.${system};
        in
        {
          pre-commit-check = git-hooks.lib.${system}.run {
            src = ./.;
            hooks = {
              # Use ruff from nixpkgs
              ruff = {
                enable = true;
                package = pkgs.ruff;
              };
            };
          };
        }
      );

      devShells = forAllSystems (
        system:
        let
          pkgs = nixpkgs.legacyPackages.${system};
          editableOverlay = workspace.mkEditablePyprojectOverlay { root = "$REPO_ROOT"; };
          pythonSet = pythonSets.${system}.overrideScope editableOverlay;
          virtualenv = pythonSet.mkVirtualEnv "${project_name}-env" workspace.deps.all;
        in
        {
          default = pkgs.mkShell {
            packages = [
              virtualenv
              pkgs.cairo
              pkgs.python3Packages.pytest
              pkgs.python3Packages.vulture
              pkgs.python3Packages.iwlib
              pkgs.python3Packages.mpd2
              pkgs.ruff
              pkgs.just
              pkgs.pre-commit
              pkgs.reuse
              pkgs.uv
            ];
            env = {
              NIX_DEVSHELL_PROJECT = project_name;
              UV_PYTHON = pythonSet.python.interpreter;
              UV_PYTHON_DOWNLOADS = "never";
            }
            // {
              LD_LIBRARY_PATH = lib.makeLibraryPath (
                (lib.optionals pkgs.stdenv.isLinux pkgs.pythonManylinuxPackages.manylinux1)
                ++ [
                  pkgs.cairo
                  pkgs.gdk-pixbuf
                  pkgs.glib
                  pkgs.libpulseaudio
                  pkgs.libxcb
                  pkgs.libxkbcommon
                  pkgs.libxrender
                  pkgs.pango
                ]
              );
            };
            shellHook = ''
              unset PYTHONPATH
              export REPO_ROOT=$(git rev-parse --show-toplevel)
            '';
          };
        }
      );
    };
}
