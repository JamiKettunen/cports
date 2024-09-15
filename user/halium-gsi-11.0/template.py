pkgname = "halium-gsi-11.0"
pkgver = "821"
pkgrel = 0
archs = ["aarch64"]
depends = ["lxc-android"]
pkgdesc = "Halium-patched Android 11 Generic System Image for lxc-android"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "Apache-2.0"
url = "https://ci.ubports.com/job/UBportsCommunityPortsJenkinsCI/job/ubports%25252Fporting%25252Fcommunity-ports%25252Fjenkins-ci%25252Fgeneric_arm64/job/halium-11.0"
source = f"{url}/{pkgver}/artifact/halium_halium_arm64.tar.xz"
sha256 = "a85e2d3056d229507a283363e231fa2e6cf2ca3a6935c165a622f0455b6c7758"
compression = "zstd:19"


def install(self):
    self.install_file("system/var/lib/lxc/android/android-rootfs.img", f"usr/lib/lxc/android")
