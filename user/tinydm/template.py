pkgname = "tinydm"
pkgver = "1.2.0"
pkgrel = 0
build_style = "makefile"
make_install_args = ["OPENRC=0"]
# FIXME: patch Makefile to be BSD install(1) compatible?
make_install_env = {"CHIMERAUTILS_INSTALL_GNU": "1"}
depends = ["autologin"]
pkgdesc = "Wayland/X11 session starter for single user machines"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-3.0-or-later"
url = "https://gitlab.com/postmarketOS/tinydm"
source = f"{url}/-/archive/{pkgver}/tinydm-{pkgver}.tar.gz"
sha256 = "5b9b821a8f198b31e010d7db865a6121867db229abf989a11985387bb1d73fa0"
# no testsuite
options = ["!check"]


# FIXME: tries to run install with just "make" leading to unset DESTDIR and
# permission errors installing stuff to build chroot
def build(self): pass


def post_install(self):
    self.install_bin(self.files_path / "tinydm-wrapper")
    self.install_service(self.files_path / "tinydm")


# TODO: keep empty default dirs /etc/tinydm.d/env-wayland.d /etc/tinydm.d/env-x11.d?
# FIXME: terminated on service start! how to debug? just missing PAM config?
