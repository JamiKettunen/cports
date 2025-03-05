pkgname = "mir"
pkgver = "2.19.3"
pkgrel = 0
build_style = "cmake"
# FIXME: drop MIR_ENABLE_TESTS=OFF!
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
    "gmp-gmpxx-devel",
]
depends = ["dmz-cursor-theme"]  # for examples/{mir_demo_server,miral-shell}
pkgdesc = "Wayland compositor and shell library"
license = "GPL-2.0-or-later AND LGPL-2.0-or-later"
url = "https://github.com/canonical/mir"
source = f"https://github.com/canonical/mir/archive/5f49884f046e8ef44fe5a210d9fbefe5b752cb00.tar.gz"
sha256 = "696a5aef1ebde9cfd4880e57db0f0537014e2a8093407795da9f63eeddb5f70a"


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
def _(self):
    return self.default_devel()
