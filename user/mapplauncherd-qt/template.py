pkgname = "mapplauncherd-qt"
pkgver = "1.1.22"
pkgrel = 0
# TODO: port to cmake? -> pick https://github.com/sailfishos/mapplauncherd-qt/pull/3 back up maybe
#build_style = "qmake"  # TODO...
build_style = "makefile"
configure_args = [f"VERSION={pkgver}"]
make_use_env = True
hostmakedepends = ["pkgconf", "qt6-qtbase-devel"]
makedepends = [
    "qt6-qtbase-private-devel",  # NOTE: rebuild this pkg on Qt upgrades!
    "qt6-qtdeclarative-devel",
    "glib-devel",
    "mapplauncherd-devel",
]
pkgdesc = "Application launch boosters for Qt6"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-only"
url = "https://github.com/sailfishos/mapplauncherd-qt"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "1a71dc2ef0340287dfd067d9189db689896a231256b8d264933cb5417b95eedd"
#hardening = ["vis", "cfi"]  # TODO: mdeclarativecache public symbols breaks with vis
# qmake cross mess...
options = ["!cross"]


def configure(self):
    self.do(
        "qmake6",
        "PREFIX=/usr",
        f"QMAKE_CFLAGS={self.get_cflags(shell=True)}",
        f"QMAKE_CXXFLAGS={self.get_cxxflags(shell=True)}",
        f"QMAKE_LFLAGS={self.get_ldflags(shell=True)}",
        *configure_args,
    )


def init_install(self):
    self.make_install_args += [f"INSTALL_ROOT={self.chroot_destdir}"]


#def post_install(self):
    # TODO: replicate data/booster-qt*.service
    # TODO: usr/libexec/mliteremoteaction -> usr/lib?
    # TODO: usr/bin/mlitenotificationtool -> -progs subpkg?


@subpackage("mapplauncherd-qt-devel")
def _(self):
    return self.default_devel()
