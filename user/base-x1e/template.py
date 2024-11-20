pkgname = "base-x1e"
pkgver = "0.1"
pkgrel = 0
# https://github.com/TravMurav/dtbloader#supported-devices
archs = ["aarch64"]
pkgdesc = "Chimera base package for Qualcomm Snapdragon X Elite/Plus devices"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "custom:none"
url = "https://chimera-linux.org"
_hwids = "abdb4b098b3958d0ca59f279e720acd8155a7fc3"
source = f"https://github.com/anonymix007/systemd-stub/archive/{_hwids}.tar.gz"
sha256 = "4cd2f3e5a1cd4843a1d8a17aa18b46ac0f874208c2fb20900add2a580256b286"
options = ["empty"]


def install(self):
    self.install_file("json/x1e*.json", "usr/share/x1e-hwids", glob=True)
    # TODO: tmpfiles cp /usr/share/x1e/ukify-args /etc/kernel/ukify-args
    self.install_file(self.files_path / "ukify-args", "etc/kernel")
    self.install_file(self.files_path / "ukify-dtbs", "etc/kernel")


@subpackage("base-x1e-firmware")
def _(self):
    self.subdesc = "commonly used firmware"
    self.install_if = [self.parent]
    self.depends = [
        "firmware-linux-ath11k",
        "firmware-linux-qca",
        "firmware-linux-qcom",
    ]
    self.options = ["empty"]
    return []


# TODO: rename from "base-x1e-ukify" to "base-x1e-uki"?
@subpackage("base-x1e-ukify")
def _(self):
    self.subdesc = "default systemd-boot bootloader setup"
    self.install_if = [self.parent]
    self.depends = ["systemd-boot", "ukify"]
    return ["etc/kernel/ukify-*", "usr/share/x1e-hwids"]
