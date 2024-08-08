pkgname = "maliit-keyboard"
pkgver = "2.3.1_git20240314"
pkgrel = 0
build_style = "cmake"
# old: -Denable-presage=OFF
# FIXME: -Denable-tests=ON FTBFS
configure_args = ["-Dwith-qt6=ON", "-Denable-tests=OFF"]
#make_check_args = ["-E", "ft_mimpluginmanager"]
#make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = ["cmake", "ninja", "pkgconf", "gettext"]
# TODO: package AnthyUnicode, Anthy, Pinyin, Chewing
makedepends = [
    "qt6-qtdeclarative-devel",
    "qt6-qtmultimedia-devel",
    "qt6-qt5compat-devel",
    "maliit-framework-devel",
    "glib-devel",
    "hunspell-devel",
]
pkgdesc = "Virtual keyboard for Wayland and X11"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-3.0-only AND BSD-3-Clause"
url = "https://github.com/maliit/keyboard"
_commit = "9b6478448ba25519e146f9d6ff674e70583497bd"
source = f"{url}/archive/{_commit}.tar.gz"
sha256 = "daa83e7389affeac35d4eedc51b580dc941e5712ef7107886802bbd39ddb67b5"
# TODO:
#hardening = ["vis", "cfi"]
tool_flags = {
    "CXXFLAGS": [
        # avoid 300+ lines of spam
        #"-Wno-inconsistent-missing-override",
        "-Wno-deprecated-declarations"
    ]
}
options = ["!parallel"]


def post_install(self):
    self.install_license("COPYING.BSD")


# FIXME: FTBFS https://paste.c-net.org/hqybfgrcsa43
