pkgname = "miracle-wm"
pkgver = "0.4.1"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "mir-devel",
    "glib-devel",
    "yaml-cpp-devel",
    "libevdev-devel",
    "nlohmann-json",
    "libnotify-devel",
    "gtest-devel",
    "mesa-devel",
    "glm",
    "libxkbcommon-devel",
    "boost-devel",
    "json-c-devel",
]
pkgdesc = "Tiling Wayland compositor based on Mir"
license = "GPL-3.0-or-later"
url = "https://mattkae.github.io/miracle-wm-wiki"
source = f"https://github.com/mattkae/miracle-wm/archive/v{pkgver}.tar.gz"
sha256 = "250bfe04f3f887f64bb7dfa98c9d6f56827ca628b68851424a20b5783ba13482"


# FIXME: cannot ^C / use close button when nested under X11 unlike mir_demo_server! needs SIGKILL to close
# -> Super+Shift+E to exit compositor still works as expected.. maybe signal handling should be relaxed when running as nested?
# TODO: sensible runtime soft-deps? what about a config with e.g. Chimera Linux wallpaper?
