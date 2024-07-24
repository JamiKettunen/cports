pkgname = "wvkbd"
pkgver = "0.15"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_use_env = True
hostmakedepends = ["gmake", "pkgconf", "wayland-progs"]
makedepends = [
    "libxkbcommon-devel",
    "linux-headers",
    "pango-devel",
    "wayland-devel",
]
pkgdesc = "On-screen keyboard for wlroots"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-3.0-only"
url = "https://github.com/jjsullivan5196/wvkbd"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "b64ae5c1f8d92c0a4437b1288f7760a8df562330aae5398f2dc4ad6116a95f69"
hardening = ["vis", "cfi"]
# no
options = ["!check"]


# TODO: do_configure(): self.cp(self.files_path / "config.h", self.wrksrc)?
