pkgname = "halium-wrappers"
pkgver = "17_git20241017"
pkgrel = 0
_commit = "173c613c2795f41d0ca4a9751128a5a99a999ff0"
_branch = "chimera"
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
source = f"https://github.com/JamiKettunen/halium-wrappers/archive/{_commit}.tar.gz"
sha256 = "00eeee8ea0d48b9e6d832cf2a22a4080b8bd5e0f973b900d97944dac8baff287"
file_modes = {
    "usr/lib/libtls-padding.so": ("root", "root", 0o4644),
    "usr/lib/libgtk6216workaround.so": ("root", "root", 0o4644),
    #"usr/lib/libglesshadercache.so": ("root", "root", 0o4644), # armv7 FIXME !cross mesa, also drop patches/no-mesa-graphical..patch
}
# distlicense: no bsd license to be found in dirs
options = ["!distlicense"]


def post_install(self):
    self.uninstall("usr/lib/systemd")

    self.install_service(self.files_path / "android-service")
