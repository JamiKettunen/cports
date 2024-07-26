pkgname = "swaylockd"
pkgver = "0.1.0"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
# FIXME: patch Makefile to be BSD install(1) compatible
make_install_env = {"CHIMERAUTILS_INSTALL_GNU": "1"}
hostmakedepends = ["gmake", "asciidoctor"]
depends = ["swaylock"]
pkgdesc = "Launcher ensuring swaylock always runs"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "MIT"
url = "https://github.com/jirutka/swaylockd"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "6d3d39def422f087a26143c8e8c9838c9d597f5faeaaec92f000fa01db15c871"
# no testsuite
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
