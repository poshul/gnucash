#!/usr/bin/env bash
set -euo pipefail

if command -v apt-get >/dev/null 2>&1; then
  export DEBIAN_FRONTEND=noninteractive
  apt-get update
  apt-get install -y \
    bash \
    build-essential \
    cmake \
    gettext \
    googletest \
    guile-3.0-dev \
    libboost-all-dev \
    libglib2.0-dev \
    libicu-dev \
    libxml2-dev \
    libxslt1-dev \
    ninja-build \
    pkg-config \
    swig \
    xsltproc \
    zlib1g-dev
  exit 0
fi

if command -v dnf >/dev/null 2>&1; then
  dnf -y install dnf-plugins-core
  dnf -y install epel-release
  dnf config-manager --set-enabled crb
  dnf -y install \
    bash \
    boost-devel \
    cmake \
    gcc \
    gcc-c++ \
    gettext \
    glib2-devel \
    gmock-devel \
    gtest-devel \
    guile30-devel \
    libicu-devel \
    libxml2-devel \
    libxslt-devel \
    libxslt \
    make \
    ninja-build \
    pkgconf-pkg-config \
    swig \
    zlib-devel
  exit 0
fi

if command -v yum >/dev/null 2>&1; then
  yum -y install \
    bash \
    boost-devel \
    cmake \
    gcc \
    gcc-c++ \
    gettext \
    glib2-devel \
    gmock-devel \
    gtest-devel \
    guile30-devel \
    libicu-devel \
    libxml2-devel \
    libxslt-devel \
    libxslt \
    make \
    ninja-build \
    pkgconfig \
    swig \
    zlib-devel
  exit 0
fi

echo "No supported package manager found (apt-get/dnf/yum)." >&2
exit 1
