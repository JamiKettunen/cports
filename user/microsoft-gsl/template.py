pkgname = "microsoft-gsl"
pkgver = "4.0.0"
pkgrel = 0
build_style = "cmake"
# FIXME: doesn't build with checkdepends = ["gtest-devel"]
configure_args = ["-DGSL_TEST=OFF"]
hostmakedepends = ["cmake", "ninja"]
pkgdesc = "C++ guidelines support header library"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "MIT"
url = "https://github.com/microsoft/GSL"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "f0e32cb10654fea91ad56bde89170d78cfbf4363ee0b01d8f097de2ba49f6ce9"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
