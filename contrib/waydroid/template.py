pkgname = "waydroid"
pkgver = "1.4.3"
pkgrel = 0
# officially supported 64-bit architectures from https://developer.android.com/ndk/guides/abis#sa
archs = ["aarch64", "x86_64"]
build_style = "makefile"
# TODO dinit D-Bus activation later? wait for https://github.com/chimera-linux/dinit-dbus to be finished and widely available in repo
make_install_args = ["USE_SYSTEMD=0", "USE_NFTABLES=1", "USE_DBUS_ACTIVATION=0"]
hostmakedepends = ["python"]
depends = [
    "gbinder-python",
    "python-gobject",
    "python-dbus",
    "gtk+3",
    "polkit",
    #"dnsmasq", # lxc already depends on it
    "nftables",
    "lxc",
]
pkgdesc = "Container-based approach to boot a full Android system"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-3.0-or-later"
url = "https://waydro.id"
source = (
    f"https://github.com/waydroid/waydroid/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "6557c6fed6a0a7417503eaaab3602efd67c6ced2026725ac24ec8c809fc672e4"
# no tests
options = ["!check"]


def post_install(self):
    from cbuild.util import python

    python.precompile(self, "usr/lib/waydroid")
    # TODO: drop the former after dinit D-Bus activation possible? or at least default disable
    self.install_service(self.files_path / "waydroid-container", enable=True)


@subpackage("waydroid-audio")
def _audio(self):
    self.pkgdesc += " (audio support)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.depends = ["pipewire"]
    self.options = ["empty"]
    return []


@subpackage("waydroid-adb")
def _adb(self):
    self.pkgdesc += " (ADB support)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.depends = ["android-tools"]
    self.options = ["empty"]
    return []


@subpackage("waydroid-clipboard")
def _clipboard(self):
    self.pkgdesc += " (clipboard sync support)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.depends = ["python-pyclip"]
    self.options = ["empty"]
    return []


#@subpackage("waydroid-sensors")
#def _sensors(self):
#    self.pkgdesc += " (sensors support)"
#    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}"]
#    self.depends = ["waydroid-sensord"]
#    self.options = ["empty"]
#    return []


# TODO:
# - https://github.com/waydroid/waydroid-sensors? how would the soft-dep work here if it can't be called the same?
#   -> just install_if in the other pkg?
# - README? https://github.com/void-linux/void-packages/blob/master/srcpkgs/waydroid/files/README.voidlinux
