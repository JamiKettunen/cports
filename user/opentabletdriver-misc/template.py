pkgname = "opentabletdriver-misc"
pkgver = "0.6.5.1"
pkgrel = 0
hostmakedepends = ["bash", "jq"]
triggers = ["/usr/lib/opentabletdriver"]
pkgdesc = "Misc files for cross-platform tablet driver tool flatpak"
license = "LGPL-3.0-or-later"
url = "https://github.com/OpenTabletDriver/OpenTabletDriver"
source = f"https://github.com/OpenTabletDriver/OpenTabletDriver/archive/v{pkgver}.tar.gz"
sha256 = "682cea127a583b9e4a2fceaf8ec92557502a25ce7d34b18b085ba790c911f0cb"
file_modes = {
    # for self-trigger to avoid constant initramfs regen meme
    "+usr/lib/opentabletdriver": ("root", "root", 0o755, True),
}


def install(self):
    self.mkdir(self.destdir / "usr/lib/udev/rules.d", parents=True)
    # TODO: somehow avoid sh -c?
    # self.do("./generate-rules.sh", "-o", f"{self.chroot_destdir}/usr/lib/udev/rules.d/70-opentabletdriver.rules")
    self.do(
        "sh",
        "-c",
        f"./generate-rules.sh > {self.chroot_destdir}/usr/lib/udev/rules.d/70-opentabletdriver.rules",
    )
    self.install_file(
        "eng/linux/Generic/usr/lib/modprobe.d/99-opentabletdriver.conf",
        "usr/lib/modprobe.d",
    )
    self.install_service(self.files_path / "opentabletdriver.user")


# TODO: reload tablet kernel drivers if needed somehow and regen initfs post-deinstall?
