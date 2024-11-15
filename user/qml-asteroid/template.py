pkgname = "qml-asteroid"
pkgver = "2.0.0_git20240828"
pkgrel = 0
_branch = "master"
_commit = "f3e3fb0cc9a072c74ecd1c69b0968142580f27f6"
build_style = "cmake"
configure_args = [
    # FIXME: SailfishOS Mlite5/Mapplauncherd_qt5 Qt6 ports for asteroidapp...
    "-DWITH_ASTEROIDAPP=OFF",
    "-DQT_MAJOR_VERSION=6",
    # otherwise installs to invalid /usr/lib/qml
    "-DINSTALL_QML_IMPORT_DIR=/usr/lib/qt6/qml"
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
    "extra-cmake-modules",
]
makedepends = [
    "qt6-qtdeclarative-devel",
    "qt6-qtsvg-devel",
]
depends = [
    "asteroid-icons-ion",  # defaults used by e.g. IconButton
    # TODO: qt6-qtvirtualkeyboard ?
]
pkgdesc = "QML components, styles and demos for AsteroidOS"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-only"
url = "https://github.com/AsteroidOS/qml-asteroid"
source = f"{url}/archive/{_commit}.tar.gz"
sha256 = "4e13a2d3196b28bfafd8caa7e88ed0981d36b2e28c3c809f397136a7510d7182"
hardening = ["vis", "cfi"]


@subpackage("qml-asteroid-devel")
def _(self):
    return self.default_devel(extra=["usr/share/asteroidapp/cmake"])
