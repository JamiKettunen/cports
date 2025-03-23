pkgname = "plasma-nano"
pkgver = "6.3.3"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "extra-cmake-modules", "gettext", "ninja"]
makedepends = [
    "qt6-qtdeclarative-devel",
    "qt6-qtsvg-devel",
    "kwindowsystem-devel",
    "ki18n-devel",
    "kservice-devel",
    "kitemmodels-devel",
    "libplasma-devel",
    "kwayland-devel",
]
pkgdesc = "KDE minimal Plasma shell for embedded devices"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://invent.kde.org/plasma/plasma-nano"
source = f"$(KDE_SITE)/plasma/{'.'.join(pkgver.split('.')[0:3])}/plasma-nano-{pkgver}.tar.xz"
sha256 = "8b84c2150bd180c5dc2daa7c0a1b43323ba361216b85ef9558773f97ff049c16"
hardening = ["vis"]
# ECM qtpaths
options = ["!cross"]
