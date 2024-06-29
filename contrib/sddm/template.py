pkgname = "sddm"
pkgver = "0.21.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_WITH_QT6=ON",
    "-DBUILD_MAN_PAGES=ON",
    "-DNO_SYSTEMD=ON",
    "-DUSE_ELOGIND=ON",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "extra-cmake-modules",
    "pkgconf",
    "python-docutils",
]
makedepends = [
    "linux-pam-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
    "elogind-devel",
]
depends = [
    # TODO: possibly optional elogind? does it even run without?
    # "elogind",
    "dbus",
    "turnstile",
    "xrdb",
    "xserver-xorg-input-libinput",
]
pkgdesc = "QML based display manager"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later AND CC-BY-3.0"
url = "https://github.com/sddm/sddm"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "f895de2683627e969e4849dbfbbb2b500787481ca5ba0de6d6dfdae5f1549abf"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")

    self.install_service(self.files_path / "sddm")
    self.install_file(
        self.files_path / "10-breeze-theme.conf", "usr/lib/sddm/sddm.conf.d"
    )

    # FIXME: services/CMakeLists.txt installs to CMAKE_INSTALL_FULL_SYSCONFDIR
    self.rename("etc/pam.d", "usr/lib/pam.d", relative=False)


@subpackage("sddm-breeze")
def _breeze(self):
    self.pkgdesc += " (default to KDE's Plasma Breeze theme)"
    self.install_if = [self.parent.pkgname_ver, "plasma-workspace"]
    self.depends = ["plasma-workspace"]
    return ["usr/lib/sddm/sddm.conf.d/10-breeze-theme.conf"]


# TODO:
# - any tweaks to /usr/share/sddm/scripts/Xsession required like on gnome?
# - compile plama-workspace with -DINSTALL_SDDM_WAYLAND_SESSION=ON, is it too unstable/buggy for general use still?
