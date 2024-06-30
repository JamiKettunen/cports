pkgname = "theseus-ship"
pkgver = "6.1.0"
pkgrel = 0
build_style = "cmake"
# configure_args = ["-DBUILD_DESIGNERPLUGIN=OFF"]
# FIXME: same tests broken as alpine
# make_check_args = ["-E", "kwinfttest"]
# make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
# make_check_wrapper = ["dbus-run-session"]
hostmakedepends = [
    "cmake",
    "ninja",
    "extra-cmake-modules",
    "pkgconf",
#    "qt6-qttools-devel",
    "gettext",
    "libcap-progs", # TODO: needed?
]
makedepends = [
    "qt6-qttools-devel",
    "como-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kirigami-devel", # TODO: runtime?
    "libplasma-devel", # TODO: runtime?
    "kdecoration-devel", # TODO: runtime?
    "kscreenlocker-devel",
    "xcb-util-devel",
    "breeze-devel", # TODO: runtime?
    "libcap-devel",  # TODO: UNUSED?!

#    "qt6-qtdeclarative-devel",
#    "qt6-qt5compat-devel",
#    "kconfig-devel",
#    "kconfigwidgets-devel",
#    "kdeclarative-devel",
#    # TODO: KF6DocTools
#    # "plasma-workspace-devel", # Plasma?
#    # FIXME: wayland-devel?
]
# depends = ["kirigami"] # hwdata qt6-qtmultimedia xwayland kglobalacceld?
provides = ["kwin=6.1.69-r420"]
replaces = ["kwin~6.1"]
pkgdesc = "Wayland and X11 Compositor for KDE Plasma desktop"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later"
url = "https://github.com/winft/theseus-ship"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "dd3bb31644636e4d3e855df36b4467b20312184ac2b5462594c211107f36824c"
hardening = ["vis", "cfi"]
