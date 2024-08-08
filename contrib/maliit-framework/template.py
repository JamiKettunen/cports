pkgname = "maliit-framework"
pkgver = "2.3.0_git20240624"
pkgrel = 0
build_style = "cmake"
# -Denable-examples=ON 
# -Denable-dbus-activation=ON
# FIXME: -Denable-xcb=ON once "XCB: requested unknown components xfixes" fixed
# TODO: -Denable-docs=ON with doxygen, though htmldocs are meh
configure_args = ["-Dwith-qt6=ON", "-Denable-xcb=OFF", "-Denable-docs=OFF"]
# FIXME: testLoadPlugins segfaults (probably also on runtime?)
make_check_args = ["-E", "ft_mimpluginmanager"]
#make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "extra-cmake-modules",
    "qt6-qtdeclarative-devel",
    "qt6-qtwayland-devel",
    "wayland-protocols",
    "wayland-devel",
    #"libxfixes-devel",
    #"libxcb-devel",
]
pkgdesc = "Core libraries and server of Maliit input method framework"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-only"
url = "https://github.com/maliit/framework"
_commit = "ba6f7eda338a913f2c339eada3f0382e04f7dd67"
source = f"{url}/archive/{_commit}.tar.gz"
sha256 = "c78a06fe350eddfcd80d7995373fff4a06dd451ea73770dd5aaaf6fcd25154ee"
# TODO:
#hardening = ["vis", "cfi"]
tool_flags = {
    "CXXFLAGS": [
        # avoid 2.6k lines of spam
        "-Wno-inconsistent-missing-override",
        "-Wno-deprecated-declarations"
    ]
}


@subpackage("maliit-framework-devel")
def _(self):
    return self.default_devel()
