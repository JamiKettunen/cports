pkgname = "android-libhybris-users"
pkgver = "15"
pkgrel = 0
depends = ["libhybris"]
pkgdesc = "Android 15 (and below) system users for libhybris consumers"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "Apache-2.0"
url = f"https://android.googlesource.com/platform/system/core/+/refs/tags/android-{pkgver}.0.0_r1/libcutils/include/private/android_filesystem_config.h"


def install(self):
    self.install_file(
        self.files_path / "sysusers.conf",
        "usr/lib/sysusers.d",
        name="android-libhybris.conf",
    )
