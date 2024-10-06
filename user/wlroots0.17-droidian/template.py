pkgname = "wlroots0.17-droidian"
pkgver = "0.17.4_git20240830"
pkgrel = 0
_branch = "feature/next/upgrade-0-17-4"
_commit = "65c5ac2bc0f0c56770732d7027005621ded5b5cb"
build_style = "meson"
configure_args = [
    # all auto features are needed,
    # don't accidentally end up with them disabled
    "--auto-features=enabled",
    "--includedir=/usr/include/wlroots-0.17",
    "-Dexamples=false",
    "-Ddroidian-extensions=true",
]
hostmakedepends = [
    "glslang-progs",
    "meson",
    "pkgconf",
    "wayland-progs",
    "hwdata-devel",
]
makedepends = [
    "android-headers",
    "hwdata-devel",
    "libhybris-devel",
    "libdisplay-info-devel",
    "libdrm-devel",
    "libgbm-devel",
    "libinput-devel",
    "libliftoff-devel",
    "libseat-devel",
    "libxcb-devel",
    "libxkbcommon-devel",
    "mesa-devel",
    "musl-bsd-headers",
    "pixman-devel",
    "udev-devel",
    "vulkan-headers",
    "vulkan-loader-devel",
    "wayland-devel",
    "wayland-protocols",
    "xcb-util-errors-devel",
    "xcb-util-renderutil-devel",
    "xcb-util-wm-devel",
    "xwayland-devel",
]
depends = ["lxc-android"]
provides = [self.with_pkgver("wlroots0.17")]
replaces = ["wlroots0.17"]
replaces_priority = 1000
pkgdesc = "Modular Wayland compositor library 0.17.x with hwcomposer patches"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "MIT"
url = "https://github.com/droidian/wlroots"
source = f"https://github.com/droidian/wlroots/archive/{_commit}.tar.gz"
sha256 = "52a09adc14a90d5fe483670d8a354864c80c7a5702a1a186461ff3f98b135a6d"
# WLR_HAS_DROIDIAN_EXTENSIONS is not defined, evaluates to 0 (???)
# warning: '__ANDROID_API__' is not defined, evaluates to 0 [-Wundef]
#tool_flags = {
#    "CFLAGS": [
#        "-DWLR_HAS_DROIDIAN_EXTENSIONS=1",
#        #"-D__ANDROID_API__=30"
#    ],
#    "CXXFLAGS": [
#        "-DWLR_HAS_DROIDIAN_EXTENSIONS=1",
#        #"-D__ANDROID_API__=30"
#    ],
#}


# FIXME: cross xwayland rpath fucked requiring "ln -s / /usr/aarch64-chimera-linux-musl"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("wlroots0.17-droidian-devel")
def _(self):
    self.provides = [self.with_pkgver("wlroots0.17-devel")]
    self.replaces = ["wlroots0.17-devel"]
    self.replaces_priority = 1000
    return self.default_devel()
