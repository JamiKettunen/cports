pkgname = "halium-gsi-14.0"
pkgver = "0"
pkgrel = 0
archs = ["aarch64"]
depends = ["lxc-android"]
pkgdesc = "Halium-patched Android 14 Generic System Image for lxc-android"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "Apache-2.0"
# FIXME: work in progress, no binaries online
# HALIUM: https://github.com/muhammad23012009/android-1/tree/halium-14.0
# DEVICE: https://github.com/muhammad23012009/android_device_halium_halium_arm64/tree/halium-14.0
# PATCHES: https://github.com/muhammad23012009/hybris-patches/commits/halium-14.0
# (+ as of 2024-10-19 two latest commits from https://github.com/Halium/hybris-patches/commits/halium-13.0)
url = "https://ci.ubports.com/job/UBportsCommunityPortsJenkinsCI/job/ubports%25252Fporting%25252Fcommunity-ports%25252Fjenkins-ci%25252Fgeneric_arm64/job/halium-14.0"
source = [
    f"{url}/{pkgver}/artifact/halium_halium_arm64.tar.xz>build-{pkgver}.tar.xz",
    f"{url}/{pkgver}/artifact/halium_halium_arm64.tar.build>build-{pkgver}.txt",
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
