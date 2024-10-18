pkgname = "bluebinder"
pkgver = "1.0.18"
pkgrel = 0
build_style = "makefile"
make_build_args = ["USE_SYSTEMD=0"]
make_install_args = ["SBINDIR=/usr/bin"]
hostmakedepends = ["pkgconf"]
makedepends = ["bluez-devel", "libgbinder-devel", "linux-headers"]
depends = ["halium-wrappers"]
pkgdesc = "VHCI proxy to use Android hwbinder-based Bluetooth"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later"
url = "https://github.com/mer-hybris/bluebinder"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "ddbe1f67c9828618eb36faf4e3f161b88b13b7c35b01c0c41864bbea47f2bbab"


def post_install(self):
    self.install_file("bluebinder_post.sh", "usr/lib", mode=0o755)
    self.install_file(
        self.files_path / "bluebinder.wrapper", "usr/lib", mode=0o755
    )
    self.install_service(self.files_path / "bluebinder", enable=True)
