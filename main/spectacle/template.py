pkgname = "spectacle"
pkgver = "6.6.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kconfig-devel",
    "kcoreaddons-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kdoctools-devel",
    "kglobalaccel-devel",
    "kguiaddons-devel",
    "ki18n-devel",
    "kio-devel",
    "kirigami-devel",
    "knotifications-devel",
    "kpipewire-devel",
    "kquickimageeditor-devel",
    "kstatusnotifieritem-devel",
    "kwidgetsaddons-devel",
    "kxmlgui-devel",
    "layer-shell-qt-devel",
    "opencv-devel",
    "plasma-wayland-protocols",
    "prison-devel",
    "purpose-devel",
    "qt6-qtbase-private-devel",  # qtx11extras_p.h
    "qt6-qtmultimedia-devel",
    "qt6-qtwayland-devel",
    "xcb-util-devel",
    "zxing-cpp-devel",
]
depends = ["tesseract"]
pkgdesc = "KDE Screenshot capture utility"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/spectacle"
source = f"$(KDE_SITE)/plasma/{pkgver}/spectacle-{pkgver}.tar.xz"
sha256 = "aa14a7fdaa0c44311f0c41f3502af39374c65057c515b779682d5dbd94fcbfe3"
hardening = ["vis"]


def post_install(self):
    self.uninstall("usr/lib/systemd/user")
