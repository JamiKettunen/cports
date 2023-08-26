pkgname = "u-boot-starfive_visionfive2"
pkgver = "2024.01"
pkgrel = 0
archs = ["riscv64"]
build_style = "u_boot"
make_build_args = ["OPENSBI=/usr/lib/opensbi/generic/fw_dynamic.bin"]
hostmakedepends = [
    "gmake",
    "gcc-riscv64-unknown-elf",
    "flex",
    "bison",
    "dtc",
    "swig",
    "opensbi",
    "python-devel",
    "openssl-devel",
    "python-setuptools",
]
# TODO: decide if these should be deps here (for flashing QSPI)!
#depends = ["u-boot-tools", "mtd-utils"]
pkgdesc = "U-Boot for StarFive VisionFive 2 boards"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-only AND BSD-3-Clause"
url = "https://www.denx.de/wiki/U-Boot"
source = f"https://ftp.denx.de/pub/u-boot/u-boot-{pkgver.replace('_', '-')}.tar.bz2"
sha256 = "b99611f1ed237bf3541bdc8434b68c96a6e05967061f992443cb30aabebef5b3"
env = {
    "U_BOOT_TRIPLET": "riscv64-unknown-elf",
    "U_BOOT_TARGETS": "spl/u-boot-spl.bin.normal.out u-boot.itb",
}
hardening = ["!int"]
# not relevant
options = ["!strip", "!check", "!lto", "!debug", "foreignelf"]
