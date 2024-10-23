pkgname = "halium-gsi-13.0-arm32"
# FIXME: update to actually include VNDK parts!
pkgver = "27"
pkgrel = 0
archs = ["armv7", "aarch64"]
depends = ["lxc-android"]
pkgdesc = "Halium-patched 32-bit Android 13 Generic System Image for lxc-android"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "Apache-2.0"
url = "https://ci.ubports.com/job/UBportsCommunityPortsJenkinsCI/job/ubports%25252Fporting%25252Fcommunity-ports%25252Fjenkins-ci%25252Fgeneric_arm64/job/halium-13.0-arm32"
source = [
    f"{url}/{pkgver}/artifact/halium_halium_arm.tar.xz>build-{pkgver}.tar.xz",
    f"{url}/{pkgver}/artifact/halium_halium_arm.tar.build>build-{pkgver}.txt",
    f"{url}/{pkgver}/artifact/used-repos.txt>repos-{pkgver}.txt",
]
sha256 = [
    "40748306cdd9fcfb964048e320da0997e709c7dfc62ece443bef9e651e6c1de9",
    "7f731b89fe78fabf024abb78039e435c2c4d4e36894ef9675b0dfcd233554e9a",
    "160ac9a23fb9f38a217c27bbb92dcbaa31484965b7fb79a8d924906603df1dc7",
]
compression = "zstd:19"


def install(self):
    self.install_file("system/var/lib/lxc/android/android-rootfs.img", "usr/lib/lxc/android")
    self.install_file(f"build-{pkgver}.txt", f"usr/share/doc/{pkgname}", 0o644, name="build")
    self.install_file(f"repos-{pkgver}.txt", f"usr/share/doc/{pkgname}", 0o644, name="used-repos.txt")
