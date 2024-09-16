# Python template

Provides a Python project template with some additional auxiliary tools described
below. To use, first ensure you have Nix with Flake support installed, then
simply run:

```bash
nix flake -t github:artsbentley/nix-flake-templates#python
nix develop
```

To further initialize Poetry and the rest of the Python proyject, run:

```bash
	poetry init --dependency=dependencyname
	echo "[tool.pyright]" >> pyproject.toml
	echo 'reportMatchNotExhaustive = "error"' >> pyproject.toml
	poetry lock --no-update
	poetry install --no-root
	direnv allow
```

# Auxiliary tooling

## SOPS

Included [SOPS](https://github.com/getsops/sops) for checking in secrets, run
e.g. `sops secrets/local.yaml` to get started. See the [usage
documentation](https://github.com/getsops/sops?tab=readme-ov-file#2usage) for
further guidance.

## Local scripts

If you have local scripts that you want to package, see the comments in
`flake.nix` for an example on how to add them.
