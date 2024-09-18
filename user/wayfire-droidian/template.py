pkgname = "wayfire-droidian"
pkgver = "0.9.0_git20240914"
pkgrel = 0
_branch = "test-wf9"
_commit = "767a92fd26d142d46f88726b67669c70a7d62d45"
build_style = "meson"
configure_args = [
    "-Duse_system_wfconfig=enabled",
    "-Duse_system_wlroots=enabled",
    "-Dxwayland=enabled",
]
hostmakedepends = [
    "meson",
    "pkgconf",
    "wayland-progs",
]
makedepends = [
    "cairo-devel",
    "glm",
    "libomp-devel",
    "libxml2-devel",
    "nlohmann-json",
    "pango-devel",
    "wayland-protocols",
    "wf-config-devel",
    "wlroots0.17-droidian-devel",
]
depends = ["wlroots0.17-droidian"]
provides = [self.with_pkgver("wayfire")]
replaces = ["wayfire"]
replaces_priority = 1000
pkgdesc = "Modular and extensible wayland compositor patched for hwcomposer"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "MIT"
url = "https://wayfire.org"
source = [
    f"https://github.com/arpio23/wayfire/archive/{_commit}.tar.gz",
    "https://github.com/WayfireWM/wf-utils/archive/08553c418f164bf5e84613d27447a32e380b75f0.tar.gz",
    "https://github.com/WayfireWM/wf-touch/archive/b8b844fa873871f90a9cf0768c8ae8c92ad49f34.tar.gz",
]
source_paths = [".", "subprojects/wf-utils", "subprojects/wf-touch"]
sha256 = [
    "0c52e180e3bc5f0346c54dee18c20c8f3cb4ff9a67a13f98c72622e6ee386e9e",
    "a271a567b4512a523c07e98fe724ee2d30c903751e6ebee47b80ed58c468c073",
    "6cc22527bd46716515052d2a5086149143af6fb4ea0206bae3ae8ef6ce7db851",
]
# vis breaks symbols
hardening = ["!vis"]
# FIXME: crashes in signal-provider.hpp::provider_t::emit from libblur
# probably since clang17
options = ["!lto"]


def post_install(self):
    self.install_license("LICENSE")
    self.install_file(
        self.files_path / "wayfire-portals.conf", "usr/share/xdg-desktop-portal"
    )


@subpackage("wayfire-droidian-devel")
def _(self):
    self.provides = [self.with_pkgver("wayfire-devel")]
    self.replaces = ["wayfire-devel"]
    self.replaces_priority = 1000
    return self.default_devel()
