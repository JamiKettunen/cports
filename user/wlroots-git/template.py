pkgname = "wlroots-git"
pkgver = "0.19.0_git20240716"
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
_commit = "015bb8512ee314e1deb858cf7350b0220fc58702"
pkgdesc = "Modular Wayland compositor library git commit {_commit:0:7}"
maintainer = "flukey <flukey@vapourmail.eu>"
license = "MIT"
url = "https://gitlab.freedesktop.org/wlroots/wlroots"
source = f"https://gitlab.freedesktop.org/wlroots/wlroots/-/archive/{_commit}.tar.gz"
sha256 = "ebdb2fc4c7d1da5b1986fa9f620638e0b2fb12ad9c0fb1caf1d1ec0f3063c86b"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("wlroots-git-devel")
def _devel(self):
    # TODO: needed?
    #self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.provides = [f"wlroots-devel={pkgver}-r{pkgrel}"]
    return self.default_devel()
