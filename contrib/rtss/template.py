pkgname = "rtss"
pkgver = "0.6.2"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo"]
makedepends = ["rust-std"]
pkgdesc = "Relative TimeStamps for Stuff"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "MIT"
url = "https://github.com/freaky/rtss"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "2e526d77eb3cd1d691dbcec937992c297aab4bc369b121620ee4903cfbd1525e"


def post_install(self):
    self.install_license("LICENSE.txt")
