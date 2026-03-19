# GnuCash Python Wheel Build

This directory contains the Python packaging entrypoint for building a local, platform-specific wheel from the GnuCash source tree.

## Local build (current machine)

From the repository root:

```bash
python3 -m pip install --upgrade pip build
python3 -m pip wheel ./packaging/python-wheel -w ./dist
```

The resulting wheel appears in `dist/` and is specific to your local OS/architecture and Python ABI.

## Build-time dependencies

GnuCash bindings are native extensions and need system packages (glib, guile, boost, swig, libxml2/libxslt, etc.).

For CI and reproducible local setup, helper scripts are provided:

- `install-linux-deps.sh`
- `install-macos-deps.sh`

You can run one of those scripts first, then run the wheel command above.

## cibuildwheel

GitHub Actions uses this package directory with `cibuildwheel` via `.github/workflows/wheels.yml`.
