pkgname = "base-x1e"
pkgver = "0.1"
pkgrel = 0
archs = ["aarch64"]
pkgdesc = "Chimera base package for Qualcomm Snapdragon X Series WoA computers"
license = "custom:none"
url = "https://chimera-linux.org"
options = ["empty"]


def install(self):
    self.install_initramfs(
        self.files_path / "initrd-fw.hook", name="qcom-x1e-fw"
    )
    self.install_file(
        self.files_path / "initrd.modules",
        "usr/share/initramfs-tools/modules.d",
        name="qcom-x1e",
    )


# TODO: signed device-specific firmware sourcing (from windows?) for non-Lenovo..
# also firmware-linux-ath11k firmware-linux-ath12k firmware-linux-qca but those are pulled in by default
@subpackage("base-x1e-firmware")
def _(self):
    self.subdesc = "commonly used firmware"
    self.install_if = [self.parent, "base-full-firmware"]
    self.depends = ["firmware-linux-qcom"]
    self.options = ["empty"]
    return []


@subpackage("base-x1e-stubble")
def _(self):
    self.subdesc = "recommended devicetree setup"
    self.install_if = [self.parent, "base-kernel"]
    self.depends = ["stubble"]
    self.options = ["empty"]
    return []
