pkgname = "ktexteditor"
pkgver = "6.15.0"
pkgrel = 0
build_style = "cmake"
make_check_args = [
    "-E",
    # FIXME: katedocument_test testAboutToSave() hangs for 5 minutes,
    # txt_diff encoding tests broken similar to alpine but pass in cbuild chroot?
    # messagetest flakes about half of the time
    "katedocument_test|messagetest|encoding_(utf8|latin15|utf32|utf16|utf32be|utf16be|cyrillic_utf8|cp1251|koi8-r|one-char-latin-15|latin15-with-utf8-bom).txt_diff|bug313759",
]
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
make_check_wrapper = ["dbus-run-session", "--"]
hostmakedepends = ["cmake", "extra-cmake-modules", "gettext", "ninja"]
makedepends = [
    "editorconfig-devel",
    "karchive-devel",
    "kauth-devel",
    "kconfig-devel",
    "kguiaddons-devel",
    "ki18n-devel",
    "kio-devel",
    "kparts-devel",
    "ktextwidgets-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtspeech-devel",
    "qt6-qttools-devel",
    "sonnet-devel",
    "syntax-highlighting-devel",
]
checkdepends = ["dbus"]
pkgdesc = "KDE Full text editor component"
license = "LGPL-2.0-or-later AND (LGPL-2.0-only OR LGPL-3.0-only)"
url = "https://api.kde.org/frameworks/ktexteditor/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/ktexteditor-{pkgver}.tar.xz"
sha256 = "ea9a7c084042250bdfa33e9bf5fc1dc700d55b2b5fd8f2aba640bff90392e23d"
hardening = ["vis"]


@subpackage("ktexteditor-devel")
def _(self):
    self.depends += ["kparts-devel", "syntax-highlighting-devel"]

    return self.default_devel()
