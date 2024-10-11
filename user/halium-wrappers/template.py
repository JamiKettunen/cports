pkgname = "halium-wrappers"
pkgver = "17"
pkgrel = 0
build_style = "makefile"
make_install_args = ["SBINDIR=/usr/bin", "TRIPLET="]
hostmakedepends = ["pkgconf"]
makedepends = [
    "zlib-ng-compat-devel",
    "libhybris-devel",
    #"mesa-devel",
]
depends = ["libhybris-progs"]
pkgdesc = "Convenience wrappers to Android utilities"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "BSD-3-Clause"
url = "https://github.com/droidian/halium-wrappers"
source = f"{url}/archive/refs/tags/droidian/next/{pkgver}.tar.gz"
sha256 = "5f9e583dc14fe682f5c3baf594f2da6db152ea85e642c57cbda5a3388f3f8e10"
file_modes = {
    "usr/lib/libtls-padding.so": ("root", "root", 0o4644),
    "usr/lib/libgtk6216workaround.so": ("root", "root", 0o4644),
    #"usr/lib/libglesshadercache.so": ("root", "root", 0o4644), # armv7 FIXME !cross mesa, also drop patches/no-mesa-graphical..patch
}
# distlicense: no bsd license to be found in dirs
options = ["!distlicense"]


def post_install(self):
    self.uninstall("usr/lib/systemd")

    self.install_file(
        self.files_path / "android-service.wrapper", "usr/libexec", mode=0o755
    )
    self.install_service(self.files_path / "android-service")
    self.install_service(self.files_path / "android-hwcomposer", enable=True) # TODO: no auto-enable?
    self.install_file(self.files_path / "android-hwcomposer.conf", "etc")
