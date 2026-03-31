pkgname = "dislocker"
pkgver = "0.7.3_git20240607"
pkgrel = 0
_commit = "38dab03175cb5798d625375154e716665201bae1"
build_style = "cmake"
configure_args = ["-DLIB_INSTALL_DIR=/usr/lib"]
hostmakedepends = ["cmake", "fuse-devel", "ninja", "pkgconf"]
makedepends = ["mbedtls-devel-static", "fuse-devel"]
pkgdesc = "Mount BitLocker encrypted Windows volumes"
license = "GPL-2.0-or-later"
url = "https://github.com/Aorimn/dislocker"
source = f"https://github.com/Aorimn/dislocker/archive/{_commit}.tar.gz"
sha256 = "ed441d8e6b2180a0a2c6e995f3dfde866c33cb60a37c25514dfcb69fdcbf383b"


def post_install(self):
    # unbreak pre-compressed manpage symlink
    (self.destdir / "usr/share/man/man1/dislocker.1.gz").unlink()
    (self.destdir / "usr/share/man/man1/dislocker.1").symlink_to(
        "dislocker-fuse.1"
    )
