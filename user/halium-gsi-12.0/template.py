pkgname = "halium-gsi-12.0"
pkgver = "581"
pkgrel = 0
archs = ["aarch64"]
depends = ["lxc-android"]
pkgdesc = "Halium-patched Android 12 Generic System Image for lxc-android"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "Apache-2.0"
url = "https://ci.ubports.com/job/UBportsCommunityPortsJenkinsCI/job/ubports%25252Fporting%25252Fcommunity-ports%25252Fjenkins-ci%25252Fgeneric_arm64/job/halium-12.0"
source = [
    f"{url}/{pkgver}/artifact/halium_halium_arm64.tar.xz>build-{pkgver}.tar.xz",
    f"{url}/{pkgver}/artifact/halium_halium_arm64.tar.build>build-{pkgver}.txt",
    f"{url}/{pkgver}/artifact/used-repos.txt>repos-{pkgver}.txt",
]
sha256 = [
    "3b556efc690b0585c695734e1a2accc6c25878a05d3aadb6b2a6d23a7a656c17",
    "879b632a83c49cac0ecdf6513d034c118ff44fc6645c555e7eef588a0372d2dc",
    "fd4a103f6e248342be8a026888557dba5aff4d6c7cc486aa98bb7d843942c199",
]
compression = "zstd:19"


def install(self):
    self.install_file("system/var/lib/lxc/android/android-rootfs.img", "usr/lib/lxc/android")
    self.install_file(f"build-{pkgver}.txt", f"usr/share/doc/{pkgname}", 0o644, name="build")
    self.install_file(f"repos-{pkgver}.txt", f"usr/share/doc/{pkgname}", 0o644, name="used-repos.txt")
