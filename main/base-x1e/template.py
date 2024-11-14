pkgname = "base-x1e"
pkgver = "0.1"
pkgrel = 0
# https://github.com/TravMurav/dtbloader#supported-devices
archs = ["aarch64"]
pkgdesc = "Chimera base package for Qualcomm Snapdragon X Elite devices"
license = "custom:none"
url = "https://chimera-linux.org"
_hwids = "20250328"
source = f"https://github.com/anonymix007/systemd-stub/archive/refs/tags/{_hwids}.tar.gz"
sha256 = "8e00e91256d3edaccf3d78eb5605fc95e118fb682aec6f91346d5a42d71ff3f2"
options = ["empty"]


def install(self):
    self.install_file("json/x1e*.json", "usr/share/x1e-hwids", glob=True)
    self.install_file(self.files_path / "ukify-args", "usr/lib/systemd/boot")
    self.install_file(self.files_path / "ukify-dtbs", "usr/lib/systemd/boot")
    # TODO: touch /usr/lib/systemd/boot/relax-esp?


@subpackage("base-x1e-firmware")
def _(self):
    self.subdesc = "commonly used firmware"
    self.install_if = [self.parent]
    self.depends = [
        "firmware-linux-ath11k",
        "firmware-linux-ath12k",
        "firmware-linux-qca",
        "firmware-linux-qcom",
    ]
    self.options = ["empty"]
    return []


@subpackage("base-x1e-uki")
def _(self):
    self.subdesc = "systemd-boot UKI bootloader setup"
    # self.install_if = [self.parent]
    self.depends = ["systemd-boot", "systemd-boot-ukify"]
    return ["usr/lib/systemd/boot", "usr/share/x1e-hwids"]
