pkgname = "kgamma"
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
    "kconfig-devel",
    "kconfigwidgets-devel",
    "kdoctools-devel",
    "ki18n-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "KDE tool for adjusting monitor gamma"
license = "GPL-2.0-or-later"
url = "https://invent.kde.org/plasma/kgamma"
source = f"$(KDE_SITE)/plasma/{pkgver}/kgamma-{pkgver}.tar.xz"
sha256 = "6f0b23e1bbef841b0d6fc5b70aafd1ca891529d6db6f612d15a002a474e9622f"
hardening = ["vis"]
