pkgname = "qml-asteroid"
pkgver = "2.0.0_git20240828"
pkgrel = 0
_branch = "master"
_commit = "f3e3fb0cc9a072c74ecd1c69b0968142580f27f6"
build_style = "cmake"
configure_args = [
    "-DINSTALL_QML_IMPORT_DIR=/usr/lib/qt6/qml",  # TODO: make default & drop..
    #"-DWITH_MAPPLAUNCHERD=OFF"
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
    "extra-cmake-modules",
]
makedepends = [
    "qt6-qtbase-private-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtsvg-devel",
    "mlite-devel",
    "mapplauncherd-qt-devel",
    "qt6-qtvirtualkeyboard", # TODO: ?
]
depends = [
    "asteroid-icons-ion",  # special defaults used by e.g. IconButton
    "fonts-noto",  # "Noto Sans" default for org.asteroid.controls
    # TODO: qt6-qtvirtualkeyboard (as soft-dep subpkg even)?
]
pkgdesc = "QML components, styles and demos for AsteroidOS"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-only"
url = "https://github.com/AsteroidOS/qml-asteroid"
source = f"{url}/archive/{_commit}.tar.gz"
sha256 = "4e13a2d3196b28bfafd8caa7e88ed0981d36b2e28c3c809f397136a7510d7182"
# cfi: with QML cachegen crashes upon launching any AsteroidApp
hardening = ["vis", "!cfi"]


@subpackage("qml-asteroid-devel")
def _(self):
    # TODO: xmmlint? on host tho..
    self.depends += ["qt6-qtdeclarative-devel"]

    return self.default_devel(
        extra=[
            "cmd:asteroid-generate-desktop",
            "usr/lib/mkspecs",
            "usr/share/asteroidapp/cmake",
        ]
    )
