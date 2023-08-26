pkgname = "base-visionfive2"
pkgver = "0.1"
pkgrel = 0
archs = ["riscv64"]
depends = [
    "firmware-linux-powervr",
    "u-boot-starfive_visionfive2",
    "u-boot-menu",
]
pkgdesc = "Chimera base package for StarFive VisionFive 2"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "custom:none"
url = "https://chimera-linux.org"


def do_install(self):
    # u-boot-menu
    self.install_file(self.files_path / "u-boot-device", "etc/default")
    self.install_file(self.files_path / "u-boot-cmdline", "etc/default")
    # agetty service customization
    self.install_file(self.files_path / "agetty", "etc/default")
