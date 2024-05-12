pkgname = "dmz-cursor-theme"
pkgver = "0.4.5.1"
pkgrel = 0
hostmakedepends = ["xcursorgen"]
pkgdesc = "DMZ cursor theme"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "CC-BY-SA-3.0"
url = "https://salsa.debian.org/gnome-team/dmz-cursor-theme"
source = f"$(DEBIAN_SITE)/main/d/dmz-cursor-theme/dmz-cursor-theme_{pkgver}.tar.xz"
sha256 = "9d6a00de42b2e02e89804b6e53cbf3c0440b6f620e09cf2e9a857851ba1126f0"
_colors = ["White", "Black"]


def do_build(self):
    for color in _colors:
        with self.pushd(f"DMZ-{color}/pngs"):
            self.do("./make.sh")


def do_install(self):
    for color in _colors:
        self.install_file(f"DMZ-{color}/index.theme", f"usr/share/icons/DMZ-{color}")
        self.install_files(f"DMZ-{color}/xcursors", f"usr/share/icons/DMZ-{color}", name="cursors")
