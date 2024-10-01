pkgname = "powertop-git"
pkgver = "2.16_git20240302"
pkgrel = 0
_commit = "9beafe3bd5e9d4c6cf2596dacdf6ab9c9be0c85e"
_branch = "master"
build_style = "gnu_configure"
configure_args = ["--disable-nls"]
configure_gen = ["./autogen.sh"]
hostmakedepends = [
    "autoconf",
    "automake",
    "pkgconf",
    "slibtool",
]
makedepends = [
    "autoconf-archive",
    "gettext-devel",
    "libnl-devel",
    "libtracefs-devel",
    "linux-headers",
    "ncurses-devel",
    "pciutils-devel",
]
provides = [f"powertop={pkgver}-r{pkgrel}"]
# prevent file conflict errors with tagged version pkg
replaces = [f"powertop<{pkgver.rsplit('_')[0]}"]
pkgdesc = "Diagnostic tool for power usage"
maintainer = "stbk <stbk@elia.garden>"
license = "GPL-2.0-only"
url = "https://github.com/fenrus75/powertop"
source = f"{url}/archive/{_commit}.tar.gz"
sha256 = "b63bb179b18bfe9a1ca92a6e57d4a7bc8c045a1cd5ac67d99d58be5fa062781e"
