pkgname = "android-headers"
pkgver = "11.0_git20211130"
pkgrel = 0
# FIXME: drop later, mostly to keep myself from building for x86_64 host on accident
archs = ["aarch64", "armv7"]
_branch = "halium-11.0"
_commit = "2c6ac3dcc4f8db593dd69906b0ec22822abfed91"
build_style = "makefile"
hostmakedepends = ["pkgconf"]
pkgdesc = f"Android {pkgver[0:pkgver.rfind('.')]} userspace headers for libhybris"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "Apache-2.0"
url = "https://github.com/Halium/android-headers"
source = f"{url}/archive/{_commit}.tar.gz"
sha256 = "b25c9fae7bf2e9061e4b853a51927816ca28a8ee645b1d2efb125f4475a08eb2"
# no testsuite, just headers
options = ["!check"]


def build(self):
    self.rm("libnfc-nxp/*.c", glob=True)
