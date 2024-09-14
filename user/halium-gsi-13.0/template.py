pkgname = "halium-gsi-13.0"
pkgver = "347"
pkgrel = 0
archs = ["aarch64"]
depends = ["lxc-android"]
pkgdesc = "Halium-patched Android 13 Generic System Image for lxc-android"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "Apache-2.0"
url = "https://ci.ubports.com/job/UBportsCommunityPortsJenkinsCI/job/ubports%25252Fporting%25252Fcommunity-ports%25252Fjenkins-ci%25252Fgeneric_arm64/job/halium-13.0"
source = [
    f"{url}/{pkgver}/artifact/halium_halium_arm64.tar.xz>build-{pkgver}.tar.xz",
    f"{url}/{pkgver}/artifact/halium_halium_arm64.tar.build>build-{pkgver}.txt",
    f"{url}/{pkgver}/artifact/used-repos.txt>repos-{pkgver}.txt",
]
sha256 = [
    "e910ffd186fa37d0b0f5a258b57d64f410668e1d9ae5de40384eda030cec419b",
    "d1290934fa66ac3a0284203f8a1d8cf8e04ab059ca7261a241cde3de83e62e9a",
    "4f86a5b07b531a778962e199d6ec6968ad9eab2339820e2d18cc540ed55f753b",
]
compression = "zstd:19"


def install(self):
    self.install_file("system/var/lib/lxc/android/android-rootfs.img", "usr/lib/lxc/android")
    self.install_file(f"build-{pkgver}.txt", f"usr/share/doc/{pkgname}", 0o644, name="build")
    self.install_file(f"repos-{pkgver}.txt", f"usr/share/doc/{pkgname}", 0o644, name="used-repos.txt")
