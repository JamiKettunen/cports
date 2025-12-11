pkgname = "stubble"
pkgver = "11"
pkgrel = 0
archs = ["aarch64", "loongarch64", "riscv64"]
build_style = "makefile"
make_use_env = True
hostmakedepends = ["python-pyelftools"]
depends = [
    "cmd:readelf!llvm-binutils",
    "dtc-python",
    "file",
    "python-pefile",
    "python-zstandard",
]
pkgdesc = "Device-tree loading EFI stub"
license = "LGPL-2.1-or-later"
url = "https://discourse.ubuntu.com/t/spec-stubble-a-secure-boot-friendly-device-tree-loading-efi-stub"
source = f"https://github.com/ubuntu/stubble/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "3146bda62cc9f2080a7566cbe1911ed2e28e8be0c31f84f8e7ce9b1588951f90"
# fix https://github.com/ubuntu/stubble/issues/81
tool_flags = {"LDFLAGS": ["-Wl,-z,nopack-relative-relocs"]}
# No tests, busted cross-unfriendly makefile
options = ["!check", "!cross"]
# TODO: SOURCE_DATE_EPOCH used by elf2efi.py?


def post_install(self):
    # FIXME: kernel.d script -> see chimera-live hack as example
    self.install_file("hwids/finddtbs.py", "usr/lib/stubble", mode=0o755)
