pkgname = "mapplauncherd"
pkgver = "4.2.13"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DINSTALL_SYSTEMD_UNITS=OFF", "-DUSE_SAILJAIL=OFF"]
hostmakedepends = ["cmake", "extra-cmake-modules", "ninja", "pkgconf"]
makedepends = ["dbus-devel", "elogind-devel", "glib-devel", "libcap-devel"]
pkgdesc = "Daemon helping applications launch faster"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-only"
url = "https://github.com/sailfishos/mapplauncherd"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "310c3f301d8fd81d125a038ba09819f1c7b0fad4a91a618c08c28cf9b27c34fc"
# CFI: breaks mapplauncherd-qt6 booster
hardening = ["vis", "!cfi"]


#def post_install(self):
    # TODO: drop sailjail from compiled binaries optionally?!
    # TODO: dinit user service replacements for usr/lib/systemd/user/booster-generic{,@}.service!
    # TODO: usr/libexec/mapplauncherd/booster-generic -> usr/lib/mapplauncherd/booster-generic


@subpackage("mapplauncherd-devel")
def _(self):
    return self.default_devel()
