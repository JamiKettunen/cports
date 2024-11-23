pkgname = "asteroid-calculator"
pkgver = "2.0.0_git20240729"
pkgrel = 0
_branch = "master"
_commit = "45ad2057af2ad72776965d21d43ac847ecf44d12"
build_style = "cmake"
# TODO: performance tests!
#configure_args = ["-DWITH_MAPPLAUNCHERD=OFF"]
hostmakedepends = ["cmake", "libxml2-progs", "ninja", "qt6-qttools-devel"]
makedepends = ["qml-asteroid-devel", "qt6-qtbase-private-devel"]
depends = ["mapplauncherd-qt", "qml-asteroid"]
pkgdesc = "Default calculator app for AsteroidOS"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-3.0-or-later"
url = "https://github.com/AsteroidOS/asteroid-calculator"
source = f"{url}/archive/{_commit}.tar.gz"
sha256 = "8ad2ae9b2416024ac6cf4adaf9b75291dbd96da72a57754bb00a4ff30c29978a"
# cfi: with QML cachegen crashes upon interacting with any CalcButton
hardening = ["vis", "!cfi"]

# TODO: "nan" displayed when pressing result (default as "0") toggling between -/+ output or "." while result is 0 makes it
