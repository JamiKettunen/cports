pkgname = "plasma-keyboard"
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
    "kcoreaddons-devel",
    "ki18n-devel",
    "qt6-qtbase-private-devel",  # qwaylandshellintegration_p.h/qxkbcommon_p.h
    "qt6-qtvirtualkeyboard-devel",
    "wayland-protocols",
]
pkgdesc = "KDE Virtual keyboard"
license = "GPL-2.0-or-later"
url = "https://invent.kde.org/plasma/plasma-keyboard"
source = f"$(KDE_SITE)/plasma/{pkgver}/plasma-keyboard-{pkgver}.tar.xz"
sha256 = "cc2ee9154e55e1a49c934aa8b2d4146a7209859de58057d96d297561652b76dc"
