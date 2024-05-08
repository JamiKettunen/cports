pkgname = "mir"
pkgver = "2.17.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DMIR_FATAL_COMPILE_WARNINGS=OFF", "-DMIR_ENABLE_TESTS=OFF"]
hostmakedepends = ["cmake", "ninja", "pkgconf", "python-pillow"]
makedepends = [
    "boost-devel",
    "glm",
    "libdrm-devel",
    "mesa-devel",
    "libepoxy-devel",
    "glib-devel",
    "libinput-devel",
    "lttng-ust-devel",
    "wayland-devel",
    "libxcursor-devel",
    "nettle-devel",
    "libxkbcommon-devel",
    "libxml++-2.6-devel",
    "freetype-devel",
    "yaml-cpp-devel",
    "gtest-devel",
    "gmpxx-devel",
]
depends = ["dmz-cursor-theme"]  # for examples/{mir_demo_server,miral-shell}
pkgdesc = "Wayland compositor and shell library"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later AND LGPL-2.0-or-later"
url = "https://github.com/canonical/mir"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "745d507de912ff66864c15fa4262e618cbb52a4d493bb834e84a4a6611b89968"


def init_configure(self):
    if self.has_lto():
        self.configure_args += ["-DMIR_LINK_TIME_OPTIMIZATION=ON"]


# TODO:: subpackaging
# mir-tools
# usr/bin/mir_wayland_generator
# usr/lib/mir/tools/libmirserverlttng.so
# mir-demos
# usr/bin/mir_demo_*
# usr/bin/miral-*
# usr/share/applications/miral-shell.desktop
# usr/share/icons/hicolor/scalable/apps/ubuntu-logo.svg


@subpackage("mir-devel")
def _devel(self):
    return self.default_devel()
