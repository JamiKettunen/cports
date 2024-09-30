pkgname = "power-profiles-daemon-git"
pkgver = "0.22_git20240902"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dsystemdsystemunitdir=",
    "-Dtests=false",
    "-Dzshcomp=/usr/share/zsh/site-functions",
]
hostmakedepends = [
    "glib-devel",
    "meson",
    "pkgconf",
    "python-gobject",
    "python-shtab",
]
makedepends = [
    "libgudev-devel",
    "polkit-devel",
    "upower-devel",
]
depends = ["!tlp", "python-gobject"]
checkdepends = ["python-dbusmock", "umockdev"]
provides = [f"power-profiles-daemon={pkgver}-r{pkgrel}"]
# prevent file conflict errors with tagged version pkg
replaces = [f"power-profiles-daemon<{pkgver.rsplit('_')[0]}"]
install_if = [f"power-profiles-daemon-meta={pkgver}-r{pkgrel}"]
pkgdesc = "D-Bus daemon for power management control"
maintainer = "Val Packett <val@packett.cool>"
license = "GPL-3.0-or-later"
url = "https://gitlab.freedesktop.org/upower/power-profiles-daemon"
_commit = "0100a228d055757caddaa8f3718b9c51bb80de19"
source = f"{url}/-/archive/{_commit}.tar.gz"
sha256 = "5cabe272d5f21c4825049c4078870cf8321954b211f9981c3ad1be3517c5f3ec"
hardening = ["vis"]
# FIXME: meson.build:120:4: ERROR: Problem encountered: Python3 module 'dbusmock' required but not found
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")
    self.install_service(self.files_path / "power-profiles-daemon")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")


@subpackage("power-profiles-daemon-git-meta")
def _(self):
    self.subdesc = "recommends package"
    self.options = ["empty"]
    self.provides = [f"power-profiles-daemon-meta={pkgver}-r{pkgrel}"]
    # prevent file conflict errors with tagged version pkg
    self.replaces = [f"power-profiles-daemon-meta~{pkgver.rsplit('_')[0]}"]
    return []
