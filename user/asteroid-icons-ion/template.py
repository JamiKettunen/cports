pkgname = "asteroid-icons-ion"
pkgver = "2.0.0"
pkgrel = 0
pkgdesc = "Default set of icons of AsteroidOS"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "MIT"
url = "https://github.com/AsteroidOS/asteroid-icons-ion"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "eb957954fb0b47286738fe50e16ba82db78a6020048df9aecce1509656fbfe51"


def install(self):
    self.install_file("src/*.svg", "usr/share/icons/asteroid", glob=True)
    self.install_license("LICENSE")
