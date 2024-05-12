pkgname = "dmz-cursor-theme"
pkgver = "0.4.5.2"
pkgrel = 0
hostmakedepends = ["xcursorgen"]
pkgdesc = "DMZ cursor theme"
license = "CC-BY-SA-3.0"
url = "https://salsa.debian.org/gnome-team/dmz-cursor-theme"
source = f"$(DEBIAN_SITE)/main/d/dmz-cursor-theme/dmz-cursor-theme_{pkgver}.tar.xz"
sha256 = "75ecbc5ddb1f8295472ca9f8e048f8d799a3102debc87020009bb11240110e4e"
_colors = ["White", "Black"]


def build(self):
    for color in _colors:
        with self.pushd(f"DMZ-{color}/pngs"):
            self.do("./make.sh")


def install(self):
    for color in _colors:
        self.install_file(f"DMZ-{color}/index.theme", f"usr/share/icons/DMZ-{color}")
        self.install_files(f"DMZ-{color}/xcursors", f"usr/share/icons/DMZ-{color}", name="cursors")
