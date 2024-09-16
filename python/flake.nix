{
  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  inputs.flake-utils.url = "github:numtide/flake-utils";

  outputs = { self, nixpkgs, flake-utils }: {
    overlay = nixpkgs.lib.composeManyExtensions [
      (final: prev: {
        myApp = prev.poetry2nix.mkPoetryApplication {
          projectDir = self;
        };
      })
    ];
  } // (flake-utils.lib.eachDefaultSystem (system:
    let
      pkgs = import nixpkgs {
        inherit system;
        overlays = [ self.overlay ];
      };
    in
    {
      apps = {
        inherit (pkgs)
          myApp;
      };

      defaultApp = pkgs.myApp;
      defaultPackage = pkgs.myApp;

      devShell = pkgs.mkShell {
        # buildInputs = with pkgs.python312Packages; [ python venvShellHook ];
        packages = with pkgs; [
          python312Packages.python
          python312Packages.venvShellHook
          poetry
          pyright
          maturin
          sops
          age
        ];

        venvDir = "./.venv";

        postVenvCreation = ''
          unset SOURCE_DATE_EPOCH
          ${pkgs.poetry}/bin/poetry env use $(venvDir)/bin/python
          ${pkgs.poetry}/bin/poetry install --no-root
        '';

        postShellHook = ''
          unset SOURCE_DATE_EPOCH
          ${pkgs.poetry}/bin/poetry env info
        '';
      };
    }));
}


