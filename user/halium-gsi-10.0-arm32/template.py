pkgname = "halium-gsi-10.0-arm32"
pkgver = "828"
pkgrel = 0
archs = ["armv7", "aarch64"]
depends = ["lxc-android"]
pkgdesc = "Halium-patched 32-bit Android 10 Generic System Image for lxc-android"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "Apache-2.0"
url = "https://ci.ubports.com/job/UBportsCommunityPortsJenkinsCI/job/ubports%25252Fporting%25252Fcommunity-ports%25252Fjenkins-ci%25252Fgeneric_arm64/job/halium-10.0-arm32"
source = [
    f"{url}/{pkgver}/artifact/halium_halium_arm.tar.xz>build-{pkgver}.tar.xz",
    f"{url}/{pkgver}/artifact/halium_halium_arm.tar.build>build-{pkgver}.txt",
    f"{url}/{pkgver}/artifact/used-repos.txt>repos-{pkgver}.txt",
]
sha256 = [
    "3999dfd7da66baf7efe8d7c0195fe682c61bd09260590fbc11c776f4c50eccd7",
    "ed62893451ee2c6539ec6e9f793b6637a5c13ae5bad6b1de1038945cd2795e9e",
    "6aa688849a4294923c5e1612013e7bfcb0fed2b61ee4c54bd15d34ab65a73798",
]
compression = "zstd:19"


def install(self):
    self.install_file("system/var/lib/lxc/android/android-rootfs.img", "usr/lib/lxc/android")
    self.install_file(f"build-{pkgver}.txt", f"usr/share/doc/{pkgname}", 0o644, name="build")
    self.install_file(f"repos-{pkgver}.txt", f"usr/share/doc/{pkgname}", 0o644, name="used-repos.txt")
