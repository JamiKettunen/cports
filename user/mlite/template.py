pkgname = "mlite"
pkgver = "0.4.5"
pkgrel = 0
# TODO: port to cmake?
#build_style = "qmake"  # TODO...
build_style = "makefile"
configure_args = [f"VERSION={pkgver}"]
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
make_check_wrapper = ["dbus-run-session"]
make_use_env = True
hostmakedepends = ["pkgconf", "qt6-qtbase-devel", "qt6-qttools"]
makedepends = ["qt6-qtbase-devel", "dconf-devel"]
checkdepends = ["dbus"]
pkgdesc = "Useful Qt classes originating from MeeGo Touch"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-only"
url = "https://github.com/sailfishos/mlite"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "cfcee411c563915d050b2f53f25e0b73b810cd14cbff1908269696f73123302b"
hardening = ["vis", "cfi"]
# qmake cross mess...
options = ["!cross"]
# avoid useless dbus-x11 in checkdepends (tests/ut_mnotification*)
exec_wrappers = [("/usr/bin/env", "dbus-launch")]


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


def post_install(self):
    # no installed test junk
    self.uninstall("opt/tests")
    # TODO: usr/libexec/mliteremoteaction -> usr/lib?
    # TODO: usr/bin/mlitenotificationtool -> -progs subpkg?


@subpackage("mlite-devel")
def _(self):
    return self.default_devel()
