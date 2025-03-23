pkgname = "plasma-mobile"
pkgver = "6.3.3"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
    #"qt6-qtbase",
]
makedepends = [
    "qt6-qtbase-private-devel",  # qwaylandwindow_p.h -> qtguiglobal_p.h
    "qt6-qtdeclarative-devel",
    "qt6-qtsensors-devel",
    "qt6-qtwayland-devel",
    "ki18n-devel",
    "kglobalaccel-devel",
    "kio-devel",
    "kdbusaddons-devel",
    "kitemmodels-devel",
    "knotifications-devel",
    "modemmanager-qt-devel",
    "networkmanager-qt-devel",
    "kcmutils-devel",
    "kpackage-devel",
    "libplasma-devel",
    "plasma-activities-devel",
    "libkscreen-devel",
    "kwayland-devel",
    "qcoro-devel",
    "kirigami-addons-devel",
    "kwin-devel",
    "layer-shell-qt-devel",
    "plasma-workspace-devel",
]
depends = [
    "kpipewire",
    # TODO: likely a bunch more missing stuff...
]
pkgdesc = "KDE shell components for Plasma Mobile"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://plasma-mobile.org"
source = f"$(KDE_SITE)/plasma/{'.'.join(pkgver.split('.')[0:3])}/plasma-mobile-{pkgver}.tar.xz"
sha256 = "a7cea53614b5ba62eb1a3a0edebdf07cb9d60d060b9d2df5f2c74ee318740ac8"
hardening = ["vis"]
# ECM qtpaths
options = ["!cross"]
