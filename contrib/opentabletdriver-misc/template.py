pkgname = "opentabletdriver-misc"
pkgver = "0.6.4.0"
pkgrel = 0
hostmakedepends = ["bash", "jq"]
triggers = ["/var/lib/opentabletdriver"]
pkgdesc = "Misc files for cross-platform tablet driver tool flatpak"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-3.0-or-later"
url = "https://github.com/OpenTabletDriver/OpenTabletDriver"
source = f"https://github.com/OpenTabletDriver/OpenTabletDriver/archive/v{pkgver}.tar.gz"
sha256 = "1ad04f4a32b54b9b62bd944b0196abb6613873b19c269abcc9f9e94c1dc3027f"


def do_install(self):
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
    # for self-trigger to avoid constant initramfs regen meme
    self.install_dir("var/lib/opentabletdriver", empty=True)
    self.install_service(self.files_path / "opentabletdriver.user")


# TODO: reload tablet kernel drivers if needed somehow and regen initfs post-deinstall?
