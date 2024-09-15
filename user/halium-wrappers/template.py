pkgname = "halium-wrappers"
pkgver = "17_git20241014"
pkgrel = 0
_commit = "7603f2e10b921a9b9301a164c52911f09fae13c0"
_branch = "chimera"
build_style = "makefile"
make_install_args = ["SBINDIR=/usr/bin", "TRIPLET="]
hostmakedepends = ["pkgconf"]
makedepends = [
    "zlib-ng-compat-devel",
    "libhybris-devel",
    "mesa-devel",
]
depends = ["libhybris-progs"]
pkgdesc = "Convenience wrappers to Android utilities"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "BSD-3-Clause"
url = "https://github.com/droidian/halium-wrappers"
source = f"https://github.com/JamiKettunen/halium-wrappers/archive/{_commit}.tar.gz"
sha256 = "2c945e06b2929f8ec3d069d303d559568ab036cc3ae68b42f38c65245eaf4ab2"
file_modes = {
    "usr/lib/libtls-padding.so": ("root", "root", 0o4644),
    "usr/lib/libgtk6216workaround.so": ("root", "root", 0o4644),
    "usr/lib/libglesshadercache.so": ("root", "root", 0o4644),
}
# distlicense: no bsd license to be found in dirs
options = ["!distlicense"]


def post_install(self):
    self.uninstall("usr/lib/systemd")

    self.install_service(self.files_path / "android-service")
