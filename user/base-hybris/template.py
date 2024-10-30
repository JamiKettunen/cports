pkgname = "base-hybris"
pkgver = "0.1"
pkgrel = 0
# https://developer.android.com/ndk/guides/abis#sa
archs = ["aarch64", "armv7", "x86_64"]
build_style = "meta"
depends = [
    "base-bootstrap",
    "dinit-chimera",
    "lxc-android",
]
pkgdesc = "Chimera base package for libhybris devices"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "custom:none"
url = "https://github.com/JamiKettunen/chimera-libhybris"


def install(self):
    d = "usr/lib/dinit.d/boot.d"
    self.install_dir(d)
    self.install_link(f"{d}/bluetoothd", "../bluetoothd")
    self.install_link(f"{d}/networkmanager", "../networkmanager")
    self.install_link(f"{d}/syslog-ng", "../syslog-ng")


@subpackage("base-hybris-bluetooth")
def _(self):
    self.subdesc = "Bluetooth by default via hwbinder"
    self.install_if = [self.parent]
    self.depends = ["bluez", "bluebinder"]
    self.options = ["!splitdinit", "brokenlinks"]
    return ["usr/lib/dinit.d/boot.d/bluetoothd"]


@subpackage("base-hybris-bringup")
def _(self):
    self.subdesc = "test tools etc for early stage port bringup"
    self.install_if = [self.parent]
    self.depends = ["libhybris-test-progs"]
    return []


@subpackage("base-hybris-gpu")
def _(self):
    self.subdesc = "Android GPU driver wrapping libs"
    self.install_if = [self.parent]
    self.depends = [
        "libegl-hybris",
        "libgles2-hybris",
        "libopencl-hybris",
        # TODO: "libvulkan-hybris",
        "libgles1-hybris",
    ]
    return []


# NOTE: ~74M of optional space savings at cost of no software renderers
@subpackage("base-hybris-gpu-no-mesa")
def _(self):
    self.subdesc = "drop generally unused mesa-dri etc bits"
    self.install_if = [self.parent, self.with_pkgver("!base-hybris-bringup")]
    self.depends = ["base-hybris-gpu", "!mesa-dri"]
    self.provides = [
        "so:libEGL.so.1=1.0.0",
        "so:libGLESv1_CM.so.1=1.0.1",
        "so:libGLESv2.so.2=2.0.0",
        "so:libOpenCL.so.1=1.0.0",
        # TODO: "so:libvulkan.so.1=1.3.277"
    ]
    return []


@subpackage("base-hybris-nm")
def _(self):
    self.subdesc = "NetworkManager by default for WLAN etc"
    self.install_if = [self.parent]
    self.depends = ["networkmanager"]
    self.options = ["!splitdinit", "brokenlinks"]
    return ["usr/lib/dinit.d/boot.d/networkmanager"]


@subpackage("base-hybris-syslog")
def _(self):
    self.subdesc = "system-wide logging by default via syslog-ng"
    self.install_if = [self.parent]
    self.depends = ["syslog-ng"]
    self.options = ["!splitdinit", "brokenlinks"]
    return ["usr/lib/dinit.d/boot.d/syslog-ng"]


@subpackage("base-hybris-wayfire")
def _(self):
    self.subdesc = "Wayland desktop with nyagetty autologin"
    self.install_if = [self.parent, "wayfire"]
    self.depends = ["nyagetty", "cmd:wayfire!wayfire-hwcomposer"]
    return []
