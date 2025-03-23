pkgname = "plasma-settings"
pkgver = "25.02.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
]
makedepends = [
    "qt6-qtdeclarative-devel",
    "kirigami-addons-devel",
    "kcoreaddons-devel",
    "kdbusaddons-devel",
    "ki18n-devel",
    "kcmutils-devel",
    "kcrash-devel",
    "kservice-devel",
    "kitemviews-devel",
    "kitemmodels-devel",
]
#depends = []  # TODO: kded kirigami-addons openrc-settingsd
pkgdesc = "KDE settings application for Plasma Mobile"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://invent.kde.org/plasma-mobile/plasma-settings"
source = f"$(KDE_SITE)/plasma-settings/plasma-settings-{pkgver}.tar.xz"
sha256 = "c72a0e847fba06e248d66c1c9bc4432dc94b195f6eab693aa1183970bc6bf363"
hardening = ["vis"]
# ECM qtpaths
options = ["!cross"]
