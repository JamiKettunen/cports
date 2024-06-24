pkgname = "miracle-wm"
pkgver = "0.3.2"
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
]
pkgdesc = "Tiling Wayland compositor based on Mir"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-3.0-or-later"
url = "https://mattkae.github.io/miracle-wm-wiki"
source = f"https://github.com/mattkae/miracle-wm/archive/v{pkgver}.tar.gz"
sha256 = "da62b048c02ed7ed92734832d82875302de8524b1920264b69e8ee54a685fab7"


# FIXME: cannot ^C / use close button when nested under X11 unlike mir_demo_server! needs SIGKILL to close
# -> Super+Shift+E to exit compositor still works as expected.. maybe signal handling should be relaxed when running as nested?
# TODO: sensible runtime soft-deps? what about a config with e.g. Chimera Linux wallpaper?
