#!/usr/bin/env bash
set -euo pipefail

if ! command -v brew >/dev/null 2>&1; then
  echo "Homebrew is required on macOS to install wheel build dependencies." >&2
  exit 1
fi

brew update
brew install \
  boost \
  cmake \
  gettext \
  glib \
  guile \
  icu4c \
  libxml2 \
  libxslt \
  ninja \
  pkg-config \
  swig
