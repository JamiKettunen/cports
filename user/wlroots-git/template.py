pkgname = "wlroots-git"
pkgver = "0.18.0_git20240630"
pkgrel = 0
build_style = "meson"
configure_args = [
    # all auto features are needed,
    # don't accidentally end up with them disabled
    "--auto-features=enabled",
    "-Dexamples=false",
]
hostmakedepends = [
    "glslang-progs",
    "meson",
    "pkgconf",
    "xwayland-devel",
]
makedepends = [
    "hwdata-devel",
    "lcms2-devel",
    "libdisplay-info-devel",
    "libdrm-devel",
    "libgbm-devel",
    "libinput-devel",
    "libliftoff-devel",
    "libseat-devel",
    "libxcb-devel",
    "libxkbcommon-devel",
    "mesa-devel",
    "pixman-devel",
    "udev-devel",
    "vulkan-headers",
    "vulkan-loader-devel",
    "wayland-devel",
    "wayland-protocols",
    "xcb-util-errors-devel",
    "xcb-util-renderutil-devel",
    "xcb-util-wm-devel",
]
provides = [f"wlroots={pkgver}-r{pkgrel}"]
pkgdesc = "Modular Wayland compositor library (0.18.x in-development)"
maintainer = "flukey <flukey@vapourmail.eu>"
license = "MIT"
url = "https://gitlab.freedesktop.org/wlroots/wlroots"
_commit = "67b88e46b04a9a42a735f88066872821caab8e7d"
source = f"https://gitlab.freedesktop.org/wlroots/wlroots/-/archive/{_commit}.tar.gz"
sha256 = "d5db533f9dc8d181ef64ffda8cec529a6ea83aed1259d40253b6c27bdc973520"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("wlroots-git-devel")
def _devel(self):
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.provides = [f"wlroots-devel={pkgver}-r{pkgrel}"]
    # FIXME: no more self.default_devel() with 0.18?!
    # just non-symlink /usr/lib/libwlroots-0.18.so exists now
    # good 13b9b54f3f22e6c932207f6cad9632782ec86d71
    #  (or b1b34cd6653d51f3bf8e331e6ae7b39290ae820e)
    # bad d9bfb47648aa40c15b699cde567763ebc4603e55
    return [
        "usr/include",
        "usr/lib/pkgconfig",
        "usr/lib/*.a",
    ]
