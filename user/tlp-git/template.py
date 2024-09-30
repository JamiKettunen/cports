pkgname = "tlp-git"
pkgver = "1.7.0_git20240830"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_install_args = [
    "-j1",
    "TLP_SBIN=/usr/bin",
    "TLP_ULIB=/usr/lib/udev",
    "TLP_ELOD=/usr/libexec/elogind/system-sleep",
    "TLP_NO_INIT=1",
    "TLP_WITH_ELOGIND=1",
    "TLP_WITH_SYSTEMD=0",
]
hostmakedepends = ["gmake"]
depends = ["perl", "ethtool", "hdparm"]
provides = [f"tlp={pkgver}-r{pkgrel}"]
# prevent file conflict errors with tagged version pkg
replaces = [f"tlp<{pkgver.rsplit('_')[0]}"]
pkgdesc = "Battery life optimization utility"
maintainer = "Subhaditya Nath <sn03.general@gmail.com>"
license = "GPL-2.0-or-later"
url = "https://linrunner.de/tlp"
_commit = "4a9f5d5bf775299c3cc70dffdb9d3baaedd2e77d"
source = f"https://github.com/linrunner/TLP/archive/{_commit}.tar.gz"
sha256 = "c0355ac04bb12682004c654e1e350e422c3ea87e60b2aa445d651307ee778642"
# no tests
# FIXME ERROR: zsh completion '_tlp-radio-device' has no matching command
options = ["!check", "!lintcomp"]


def post_install(self):
    self.install_service(self.files_path / "tlp")


@subpackage("tlp-rdw-git")
def _(self):
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}", "networkmanager"]
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}", "networkmanager"]
    self.provides = [f"tlp-rdw={pkgver}-r{pkgrel}"]
    # prevent file conflict errors with tagged version pkg
    self.replaces = [f"tlp-rdw~{pkgver.rsplit('_')[0]}"]
    return [
        "usr/bin/tlp-rdw",
        "usr/lib/NetworkManager",
        "usr/lib/udev/tlp-rdw-udev",
        "usr/lib/udev/rules.d/85-tlp-rdw.rules",
        "usr/share/man/man8/tlp-rdw.8",
        "usr/share/zsh/site-functions/_tlp-rdw",
        "usr/share/bash-completion/completions/tlp-rdw",
    ]
