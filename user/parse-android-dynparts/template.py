pkgname = "parse-android-dynparts"
pkgver = "0_git20240101"
pkgrel = 0
_commit = "b776ff276f20b91c8df4e2c84cf314ba7b7a3fb5"
build_style = "cmake"
hostmakedepends = ["cmake", "ninja"]
makedepends = ["openssl-devel", "linux-headers"]
depends = ["device-mapper"]
pkgdesc = "Mount Android dynamic (super) partitions on Linux"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "Apache-2.0"
url = "https://github.com/droidian/parse-android-dynparts"
source = f"https://github.com/droidian/parse-android-dynparts/archive/{_commit}.tar.gz"
sha256 = "2e68e02578f1523b4d9207842c1b439c8413ce61ae9556128a6390fa5cd38293"


# TODO: use debian initramfs hook later?
