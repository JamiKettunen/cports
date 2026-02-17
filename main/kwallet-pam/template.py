pkgname = "kwallet-pam"
pkgver = "6.6.0"
pkgrel = 0
build_style = "cmake"
# XXX drop libexec
configure_args = ["-DCMAKE_INSTALL_LIBEXECDIR=/usr/lib"]
hostmakedepends = ["cmake", "extra-cmake-modules", "ninja", "pkgconf"]
makedepends = [
    "kwallet-devel",
    "libgcrypt-devel",
    "linux-pam-devel",
    "qt6-qtdeclarative-devel",
]
depends = ["socat"]
pkgdesc = "KDE KWallet PAM plugin"
license = "LGPL-2.1-or-later"
url = "https://invent.kde.org/plasma/kwallet-pam"
source = f"$(KDE_SITE)/plasma/{pkgver}/kwallet-pam-{pkgver}.tar.xz"
sha256 = "5ab6026975785e216105fd58362b2832ab075b68c1d242b732a556179cc4ca05"
hardening = ["vis"]


def post_install(self):
    # TODO: dinit user service with graphical
    self.uninstall("usr/lib/systemd/user")
