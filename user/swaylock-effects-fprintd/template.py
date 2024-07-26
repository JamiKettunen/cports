pkgname = "swaylock-effects-fprintd"
pkgver = "1.7.0_git20231206"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dfingerprint=enabled"]
hostmakedepends = [
    "meson",
    "pkgconf",
    "scdoc",
]
makedepends = [
    "cairo-devel",
    "gdk-pixbuf-devel",
    "libxkbcommon-devel",
    "linux-pam-devel",
    "wayland-devel",
    "wayland-protocols",
    "libomp-devel",
    "dbus-devel",
    "fprintd",
]
depends = ["fprintd-meta"]
provides = ["swaylock=999"] # -r99
replaces = ["swaylock<999"]
pkgdesc = "Screen locker for Wayland with effects & fingerprint support"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "MIT"
url = "https://github.com/jirutka/swaylock-effects/pull/49"
_commit = "a124d1adc717fba32887828e8ae675695dd8eeda"
source = f"https://github.com/quantum5/swaylock-effects/archive/{_commit}.tar.gz"
sha256 = "fbc76e4a9abcb284fe2678d4afe90bd8b8a2f10bdbe7c67a3a55ac291b94c437"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
    self.rename("etc/pam.d", "usr/lib/pam.d", relative=False)
