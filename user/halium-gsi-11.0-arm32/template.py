pkgname = "halium-gsi-11.0-arm32"
pkgver = "0"
pkgrel = 0
archs = ["armv7", "aarch64"]
depends = ["lxc-android"]
pkgdesc = "Halium-patched 32-bit Android 11 Generic System Image for lxc-android"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "Apache-2.0"
# NOTE: no binaries built by UBports
# DEVICE: https://github.com/Halium/android_device_halium_halium/tree/halium-11.0
url = "https://ci.ubports.com/job/UBportsCommunityPortsJenkinsCI/job/ubports%25252Fporting%25252Fcommunity-ports%25252Fjenkins-ci%25252Fgeneric_arm64/job/halium-11.0-arm32"
source = [
    f"{url}/{pkgver}/artifact/halium_halium_arm.tar.xz>build-{pkgver}.tar.xz",
    f"{url}/{pkgver}/artifact/halium_halium_arm.tar.build>build-{pkgver}.txt",
    f"{url}/{pkgver}/artifact/used-repos.txt>repos-{pkgver}.txt",
]
sha256 = [
    "FIXME1",
    "FIXME2",
    "FIXME3",
]
compression = "zstd:19"


def install(self):
    self.install_file("system/var/lib/lxc/android/android-rootfs.img", "usr/lib/lxc/android")
    self.install_file(f"build-{pkgver}.txt", f"usr/share/doc/{pkgname}", 0o644, name="build")
    self.install_file(f"repos-{pkgver}.txt", f"usr/share/doc/{pkgname}", 0o644, name="used-repos.txt")
