pkgname = "halium-gsi-9.0"
pkgver = "807"
pkgrel = 0
archs = ["aarch64"]
depends = ["lxc-android"]
pkgdesc = "Halium-patched Android 9 Generic System Image for lxc-android"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "Apache-2.0"
url = "https://ci.ubports.com/job/UBportsCommunityPortsJenkinsCI/job/ubports%25252Fporting%25252Fcommunity-ports%25252Fjenkins-ci%25252Fgeneric_arm64/job/main"
source = f"{url}/{pkgver}/artifact/halium_halium_arm64.tar.xz"
sha256 = "025035990940e10ddab47355a1be1131fc8cf145bb67555d6d281c53ef35fd99"
compression = "zstd:19"


def install(self):
    self.install_file("system/var/lib/lxc/android/android-rootfs.img", f"usr/lib/lxc/android")
