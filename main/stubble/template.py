pkgname = "stubble"
pkgver = "9"
pkgrel = 0
# TODO loongarch64/riscv64: to be tested on some UEFI+FDT setup
archs = ["aarch64", "loongarch64", "riscv64"]
build_style = "makefile"
make_use_env = True
hostmakedepends = ["python-pyelftools"]
depends = ["dtc-python", "systemd-boot-ukify"]
pkgdesc = "Device-tree loading EFI stub"
license = "LGPL-2.1-or-later"
url = "https://discourse.ubuntu.com/t/spec-stubble-a-secure-boot-friendly-device-tree-loading-efi-stub"
source = f"https://github.com/ubuntu/stubble/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "97c5174694dcf989a7e3df69df2c1abd134fe1bbc047d7e3f274248941cb0df2"
# No tests, busted cross-unfriendly makefile
options = ["!check", "!cross"]
# TODO: SOURCE_DATE_EPOCH used by elf2efi.py?


def post_install(self):
    self.install_file("hwids/finddtbs.py", "usr/lib/stubble", mode=0o755)
