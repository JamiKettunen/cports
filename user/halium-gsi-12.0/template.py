pkgname = "halium-gsi-12.0"
pkgver = "547"
pkgrel = 0
archs = ["aarch64"]
depends = ["lxc-android"]
pkgdesc = "Halium-patched Android 12 Generic System Image for lxc-android"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "Apache-2.0"
url = "https://ci.ubports.com/job/UBportsCommunityPortsJenkinsCI/job/ubports%25252Fporting%25252Fcommunity-ports%25252Fjenkins-ci%25252Fgeneric_arm64/job/halium-12.0"
source = f"{url}/{pkgver}/artifact/halium_halium_arm64.tar.xz"
sha256 = "0ea055d67b39ee6c97b039fc4a3abd3f212200214208319de3bd1d1e2e5d069a"
compression = "zstd:19"


def install(self):
    self.install_file("system/var/lib/lxc/android/android-rootfs.img", f"usr/lib/lxc/android")
