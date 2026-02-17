pkgname = "plasma-nm"
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
    "kcmutils-devel",
    "kcolorscheme-devel",
    "kcompletion-devel",
    "kcoreaddons-devel",
    "kdbusaddons-devel",
    "ki18n-devel",
    "kio-devel",
    "kirigami-devel",
    "knotifications-devel",
    "ksvg-devel",
    "kwallet-devel",
    "libplasma-devel",
    "modemmanager-qt-devel",
    "networkmanager-qt-devel",
    "prison-devel",
    "qca-devel",
    "qcoro-devel",
    "qt6-qtdeclarative-devel",
    # TODO: openconnect>=3.99 -> qt6-qtwebengine-devel
]
depends = ["prison"]
pkgdesc = "KDE Plasma NetworkManager integration"
license = "GPL-2.0-or-later AND LGPL-2.0-or-later"
url = "https://invent.kde.org/plasma/plasma-nm"
source = f"$(KDE_SITE)/plasma/{pkgver}/plasma-nm-{pkgver}.tar.xz"
sha256 = "01e543d5c6f101fb2e01ceefd7d4338b7e2ed0b2d67546d7227ed3aa78dd5d50"
hardening = ["vis"]
