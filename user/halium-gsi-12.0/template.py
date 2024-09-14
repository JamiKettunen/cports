pkgname = "halium-gsi-12.0"
pkgver = "594"
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
    "5c3f3731563cbe7e0c6e712c207cd06bd9f9400b72170f7306f010f5fbdb4164",
    "006833373877ca636e5e0713bde248ebe6ca14abd62fd7a4fc9d757168f5e20e",
    "ee9d5323f875b4a3d7b047bb60fd53f8fb6bc993d9ab21d0e84e958caf1de3fe",
]
compression = "zstd:19"


def install(self):
    self.install_file("system/var/lib/lxc/android/android-rootfs.img", "usr/lib/lxc/android")
    self.install_file(f"build-{pkgver}.txt", f"usr/share/doc/{pkgname}", 0o644, name="build")
    self.install_file(f"repos-{pkgver}.txt", f"usr/share/doc/{pkgname}", 0o644, name="used-repos.txt")
