pkgname = "stubble"
pkgver = "7"
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
sha256 = "33ff21a507092328ca4495d465df31f6384fcc0dbf5a10710531713cb0cc0b17"
# No tests, busted cross-unfriendly makefile
options = ["!check", "!cross"]
# TODO: SOURCE_DATE_EPOCH used by elf2efi.py?


def post_install(self):
    self.install_file("hwids/finddtbs.py", "usr/lib/stubble", mode=0o755)
