pkgname = "sway-hwcomposer"
pkgver = "1.9"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "libcap-progs",
    "meson",
    "pkgconf",
    "scdoc",
    "wayland-progs",
]
makedepends = [
    "cairo-devel",
    "gdk-pixbuf-devel",
    "json-c-devel",
    "pango-devel",
    "pcre2-devel",
    "wayland-devel",
    "wayland-protocols",
    "wlroots0.17-hwcomposer-devel",
]
depends = ["wlroots0.17-hwcomposer"]
provides = [self.with_pkgver("sway")]
replaces = ["sway"]
replaces_priority = 1000
pkgdesc = "Wayland compositor compatible with i3 patched for hwcomposer"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "MIT"
url = "https://swaywm.org"
source = f"https://github.com/swaywm/sway/releases/download/{pkgver}/sway-{pkgver}.tar.gz"
sha256 = "a63b2df8722ee595695a0ec6c84bf29a055a9767e63d8e4c07ff568cb6ee0b51"
file_modes = {
    "usr/bin/sway": ("root", "root", 0o755),
}
file_xattrs = {
    "usr/bin/sway": {
        "security.capability": "cap_sys_nice+ep",
    },
}
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_file(
        self.files_path / "sway-portals.conf", "usr/share/xdg-desktop-portal"
    )


@subpackage("sway-hwcomposer-backgrounds")
def _(self):
    self.subdesc = "backgrounds"
    self.install_if = [self.parent]
    self.provides = [self.with_pkgver("sway-hwcomposer-backgrounds")]
    self.replaces = ["sway-hwcomposer-backgrounds"]
    self.replaces_priority = 1000

    return ["usr/share/backgrounds"]
