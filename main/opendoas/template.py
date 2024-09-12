pkgname = "opendoas"
pkgver = "6.8.2"
pkgrel = 4
build_style = "configure"
configure_args = [
    "--with-pam",
    "--with-timestamp",
    "--with-doas-confdir",
    "--prefix=/usr",
    "--pamdir=/usr/lib/pam.d",
]
hostmakedepends = ["byacc"]
makedepends = ["linux-pam-devel"]
pkgdesc = "Portable OpenBSD doas to execute commands as another user"
maintainer = "q66 <q66@chimera-linux.org>"
license = "ISC AND BSD-3-Clause"
url = "https://github.com/Duncaen/OpenDoas"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "6da058a0e70b7543bc60624389b0b00b686189ec933828c522bf8b2600495a67"
file_modes = {"usr/bin/doas": ("root", "root", 0o4755)}
hardening = ["vis", "cfi"]
# no test suite
options = ["!check"]


def pre_configure(self):
    self.cp(self.files_path / "doas.pam", "pam.d__doas__linux")


def post_install(self):
    self.install_license("LICENSE")
    # default conf
    self.install_file(self.files_path / "doas.conf", "etc/doas.d", name="chimera.conf")
