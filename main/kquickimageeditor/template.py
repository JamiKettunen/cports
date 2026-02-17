pkgname = "kquickimageeditor"
pkgver = "0.6.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "extra-cmake-modules", "ninja"]
makedepends = ["kconfig-devel", "opencv-devel", "qt6-qtdeclarative-devel"]
pkgdesc = "KDE Image editing components"
license = "LGPL-2.1-or-later"
url = "https://invent.kde.org/libraries/kquickimageeditor"
source = f"$(KDE_SITE)/kquickimageeditor/kquickimageeditor-{pkgver}.tar.xz"
sha256 = "11ed4ce1c164a8b6d50bbc1548b5849ab75d5fb837619b90f2cea51ed122547a"
hardening = ["vis"]


@subpackage("kquickimageeditor-devel")
def _(self):
    self.depends += ["qt6-qtdeclarative-devel"]

    return self.default_devel()
