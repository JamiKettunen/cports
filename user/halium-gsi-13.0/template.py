pkgname = "halium-gsi-13.0"
pkgver = "311"
pkgrel = 0
archs = ["aarch64"]
depends = ["lxc-android"]
pkgdesc = "Halium-patched Android 13 Generic System Image for lxc-android"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "Apache-2.0"
url = "https://ci.ubports.com/job/UBportsCommunityPortsJenkinsCI/job/ubports%25252Fporting%25252Fcommunity-ports%25252Fjenkins-ci%25252Fgeneric_arm64/job/halium-13.0"
source = f"{url}/{pkgver}/artifact/halium_halium_arm64.tar.xz"
sha256 = "f599b239e2eccbfce253a87b43407e772722a9a255c7df8d7bbcd900d0d9d780"
compression = "zstd:19"


def install(self):
    self.install_file("system/var/lib/lxc/android/android-rootfs.img", f"usr/lib/lxc/android")
