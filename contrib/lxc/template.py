pkgname = "lxc"
pkgver = "6.0.1"
pkgrel = 0
build_style = "meson"
# -Dpam-cgroup=true
# -Drootfs-mount-path=/var/lxc/containers
# -Dlog-path=/var/lxc/log
# FIXME man: requires last-updated-in-2007 docbook2x?! what about docbook-{xml,xsl-nons}
configure_args = [
    "-Ddistrosysconfdir=default",
    "-Dinit-script=[]",
    "-Dman=false",
    "-Dtests=true",  # NOTE: make sure no tests are installed?
]
hostmakedepends = [
    "meson",
    "pkgconf",
]
# openssl-devel pam-devel
makedepends = [
    "linux-headers",
    "libcap-devel",
    "libseccomp-devel",
    "dbus-devel",
]
# TODO: xz & wget2 for scripts?
depends = [
    "ugetopt",
    # TODO: lxc-net subpackage with networking related stuff?
    # "nftables",
    # FIXME: does networking only work with iptables but not nftables?!
    # "iptables",
    # iptables-legacy
    "dnsmasq",
]
pkgdesc = "Linux Containers"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-or-later"
url = "https://linuxcontainers.org/lxc"
source = f"https://github.com/lxc/lxc/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "4d8805adecd80ce9270fca5caf06a732bf043b5ad3a994ad1b976071517ff976"
file_modes = {"usr/libexec/lxc/lxc-user-nic": ("root", "root", 0o4755)}
# CFI: lxc-info crash with waydroid
hardening = ["vis", "!cfi"]


# TODO: look into src/tests/? should they run here? install into -tests subpkg or not at all?


def post_install(self):
    self.install_service(self.files_path / "lxc-autostart")
    # TODO: should any of these be made?
    # self.install_dir("var/lib/lxc", mode=0o755, empty=True)
    # self.install_dir("var/lxc/containers", mode=0o755, empty=True)
    # self.install_dir("var/lxc/log", mode=0o755, empty=True)


@subpackage("lxc-devel")
def _devel(self):
    return self.default_devel()
