pkgname = "base-x1e"
pkgver = "0.1"
pkgrel = 0
archs = ["aarch64"]
pkgdesc = "Chimera base package for Qualcomm Snapdragon X Elite/Plus devices"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "custom:none"
url = "https://chimera-linux.org"


@subpackage("base-x1e-firmware")
def _(self):
    self.subdesc = "commonly used firmware"
    self.install_if = [self.parent]
    self.depends = [
        "firmware-linux-ath11k",
        "firmware-linux-qca",
        "firmware-linux-qcom",
    ]
    return []
