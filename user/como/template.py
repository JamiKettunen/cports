pkgname = "como"
pkgver = "0.2.0"
pkgrel = 0
build_style = "cmake"
# FIXME: in tests/CMakeLists.txt:13 avoid Catch2 vendoring via FetchContent!!!
configure_args = ["-DBUILD_TESTING=OFF"]
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
    "qt6-qtdeclarative-devel",
    "qt6-qt5compat-devel",
    "qt6-qttools-devel",
    "kauth-devel",
    "kconfig-devel",
    "kconfigwidgets-devel",
    "kcrash-devel",
    "kglobalaccel-devel",
    "ki18n-devel",
    "kidletime-devel",
    "knotifications-devel",
    "kpackage-devel",
    "ksvg-devel",
    "kwindowsystem-devel",
    "kdeclarative-devel",
    "kcmutils-devel",
    "knewstuff-devel",
    "kservice-devel",
    "kxmlgui-devel",
    "kdbusaddons-devel",
    "kdoctools-devel",
    "kirigami-devel", # TODO: RUNTIME ONLY?
    #"plasma-desktop-devel", # TODO: RUNTIME ONLY? (wasn't plasma-workspace)
    "libplasma-devel", # TODO: fixes looking for Plasma
    "kdecoration-devel",
    "kscreenlocker-devel",
    "breeze-devel",
    # TODO: maybe just patch for 0.17 and submit?
    "wlroots-git-devel",
#    "libx11-devel",
#    "libx*-devel",  # TODO: https://github.com/winft/como/blob/master/CMakeLists.txt#L232
#    "freetype-devel",
#    "fontconfig-devel",
    "xcb-util-devel",
    "wrapland-devel",

#    "xwayland",  # RUNTIME?!
    "libcap-devel",  # TODO: UNUSED?!
    "libqaccessibilityclient-devel",
    # TODO: any QML modules? runtime only?
    # QtQuick.Controls-QMLModule_FOUND
    # QtMultimedia-QMLModule
]
# checkdepends = ["dbus"]
# depends = ["kirigami"]
pkgdesc = "Compositor Modules for creating Wayland and X11 compositors"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later"
url = "https://github.com/winft/como"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "24a43c5cb49760eb89f0414aa03f0007441fb2b8ef934e9ccb39af01646a27a9"
hardening = ["vis", "cfi"]


def post_install(self):
    # TODO: dinit user service with graphical
    self.rm(self.destdir / "usr/lib/systemd/user", recursive=True)


@subpackage("como-devel")
def _devel(self):
    self.depends = [
        f"{pkgname}={pkgver}-r{pkgrel}",
        "wrapland-devel",
        "wlroots-git-devel",
        "kauth-devel",
        "kcolorscheme-devel",
        "kglobalaccel-devel",
        "ki18n-devel",
        "kidletime-devel",
        "kcmutils-devel",
        "knewstuff-devel",
        "knotifications-devel",
        "kpackage-devel",
        "kservice-devel",
        "ksvg-devel",
        "kwindowsystem-devel",
        "kxmlgui-devel",
    ]

    # libbase-x11-backend.so is needed by e.g. theseus-ship, drop it from -devel
    return [
        "usr/include",
        "usr/lib/cmake",
    ]
