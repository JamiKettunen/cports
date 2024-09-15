pkgname = "halium-gsi-10.0"
pkgver = "812"
pkgrel = 0
archs = ["aarch64"]
depends = ["lxc-android"]
pkgdesc = "Halium-patched Android 10 Generic System Image for lxc-android"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "Apache-2.0"
url = "https://ci.ubports.com/job/UBportsCommunityPortsJenkinsCI/job/ubports%25252Fporting%25252Fcommunity-ports%25252Fjenkins-ci%25252Fgeneric_arm64/job/halium-10.0"
source = f"{url}/{pkgver}/artifact/halium_halium_arm64.tar.xz"
sha256 = "db9a19bb9faf40434a0db58968adfb18b83f427336b140fa08a98fa9644e8db9"
compression = "zstd:19"


def install(self):
    self.install_file("system/var/lib/lxc/android/android-rootfs.img", f"usr/lib/lxc/android")
