pkgname = "sddm-kcm"
pkgver = "6.1.2"
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
    "kcoreaddons-devel",
    "ki18n-devel",
    "kauth-devel",
    "kio-devel",
    "karchive-devel",
    "knewstuff-devel",
    "kcmutils-devel",
]
depends = ["sddm"]
pkgdesc = "KDE Login Screen (SDDM) KCM"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later"
url = "https://invent.kde.org/plasma/sddm-kcm"
source = f"$(KDE_SITE)/plasma/{pkgver}/sddm-kcm-{pkgver}.tar.xz"
sha256 = "6c78b202420e3d2d597a22b98f6e24023539d0f806f5ce09f7dcc83efe7480d7"
hardening = ["vis", "cfi"]


# FIXME: selecting anything other than breeze gives fallback theme, something is going wrong
# - elarun
# - maldives
# - maya
