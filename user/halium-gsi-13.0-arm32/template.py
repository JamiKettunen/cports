pkgname = "halium-gsi-13.0-arm32"
# NOTE: 27 didn't actually include VNDK parts!
pkgver = "29"
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
    "0186baf3706c820243bebd79199eda053ee2c98c3aa92da5d80a644f861a657f",
    "613e96b6d56d39fbbbe0cdefb62107219cb8820b12dc006515f2d4e5b30738de",
    "34857e11a5870500afbd209a770f421ca4e767cd7e016f13daa4b31350627dce",
]
compression = "zstd:19"


def install(self):
    self.install_file("system/var/lib/lxc/android/android-rootfs.img", "usr/lib/lxc/android")
    self.install_file(f"build-{pkgver}.txt", f"usr/share/doc/{pkgname}", 0o644, name="build")
    self.install_file(f"repos-{pkgver}.txt", f"usr/share/doc/{pkgname}", 0o644, name="used-repos.txt")
