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
source = f"https://github.com/miracle-wm-org/miracle-wm/archive/12492c821ad6152031a8181adedd38fea0112340.tar.gz"
sha256 = "8756cf4f212460c2c09d832d057d168f24e8d6d653bf6a387ad90bd4d1421caf"


# FIXME: cannot ^C / use close button when nested under X11 unlike mir_demo_server! needs SIGKILL to close
# -> Super+Shift+E to exit compositor still works as expected.. maybe signal handling should be relaxed when running as nested?
# TODO: sensible runtime soft-deps? what about a config with e.g. Chimera Linux wallpaper?
