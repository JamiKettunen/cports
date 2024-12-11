# FIXME: needs following ugly hack before building for techpack kernel modules to find included files:
# mkdir bldroot/kernel
# ln -s /builddir/linux-fairphone-fp5-5.4.219 bldroot/kernel/msm-5.4
pkgname = "linux-fairphone-fp5"
pkgver = "5.4.219"
pkgrel = 0
_commit = "1cb5931a30e31f306d254a1b4ac5330ef042a803"
_branch = "halium-11.0"
archs = ["aarch64"]
make_dir = "build"
hostmakedepends = ["base-kernel-devel"]
depends = ["base-kernel"]
provides = ["linux"]
pkgdesc = f"Linux kernel {pkgver[0:pkgver.rfind('.')]}.x for Volla Phone X23"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-only"
# based on https://gerrit-public.fairphone.software/plugins/gitiles/kernel/msm-5.4/+/refs/heads/kernel/13/fp5
url = "https://gitlab.com/ubports/porting/community-ports/android11/fairphone-5/kernel-fairphone-qcm6490"
# as per https://gitlab.com/ubports/porting/community-ports/android11/fairphone-5/fairphone-fp5/-/blob/master/build.sh
_gerrit_base = "https://gerrit-public.fairphone.software/plugins/gitiles"
_audio = "5fbf4684d85a1abc292af4133f29a89412d80e12" # 2023-12-19
_camera = "7ce47e5dee052f1656cf11d9d0182fe16d30497b" # 2024-03-04
_dataipa = "cfc3bc0cd5593195229aa4c28e78152715da6ee1" # 2022-12-15
_display = "56ad68d53b65bef11e830f7eef16b7a71db37ac3" # 2024-03-04
_video = "1802a11c202531b0373a3a655e32bd743366a990" # 2023-06-30
_wlan_fw_api = "5aefc742a89a4c145f202d64370f4595056f4997" # 2023-01-18
_wlan_host = "43e3025dac6ca57bff2080bb36eedc03b433345b" # 2024-03-04
_wlan_qcacld = "e11956ddf5fc1530e621047fe9ff6d1222c3fa8b" # 2024-03-04
_dts = "7e600e19309c45828eabdfeea99270c62816728f" # 2024-03-04
source = [
    f"{url}/-/archive/{_commit}.tar.gz",
    f"{_gerrit_base}/platform/vendor/opensource/audio-kernel/+archive/{_audio}.tar.gz",
    f"{_gerrit_base}/platform/vendor/opensource/camera-kernel/+archive/{_camera}.tar.gz",
    f"{_gerrit_base}/platform/vendor/opensource/dataipa/+archive/{_dataipa}.tar.gz",
    f"{_gerrit_base}/platform/vendor/opensource/display-drivers/+archive/{_display}.tar.gz",
    f"{_gerrit_base}/platform/vendor/opensource/video-driver/+archive/{_video}.tar.gz",
    f"{_gerrit_base}/platform/vendor/qcom-opensource/wlan/fw-api/+archive/{_wlan_fw_api}.tar.gz",
    f"{_gerrit_base}/platform/vendor/qcom-opensource/wlan/qca-wifi-host-cmn/+archive/{_wlan_host}.tar.gz",
    f"{_gerrit_base}/platform/vendor/qcom-opensource/wlan/qcacld-3.0/+archive/{_wlan_qcacld}.tar.gz",
    f"{_gerrit_base}/kernel/msm-extra/devicetree/+archive/{_dts}.tar.gz",
]
source_paths = [
    ".",
    "techpack/audio",
    "techpack/camera",
    "techpack/dataipa",
    "techpack/display",
    "techpack/video",
    "drivers/staging/wlan-qc/fw-api",
    "drivers/staging/wlan-qc/qca-wifi-host-cmn",
    "drivers/staging/wlan-qc/qcacld-3.0",
    "arch/arm64/boot/dts/vendor",
]
sha256 = [
    "135b0ac4d3b1ba52cdcebab29f0aaa71e206afb24517dc648e81a91d59329c50",
    "601211a06ba0e85a1bed7d56306052118c0eec9231e5e0edf20f102e94f8b6ee",
    "057f4e2a06fe4cd0b2cbc38ea0196044ce5ecf657454c7413e0644a7995e8cce",
    "759f19fa50181d2fbc768f87df341f16948326c775de313561f4a2034bd4a854",
    "47e3d0a4f7e22e1215d2a21c6553a1bf6f0768469dd364725c53abd606c7f186",
    "d121313a94c4a95803f0e50493bfa468f61367b4cbb748d8cb8913484d683631",
    "92fa3a7034d0f44b710a4a947b18564386bfe5929ae8dfd471ade60772c30fc5",
    "eebc9f4a7ccb5dee61b62be0942b81b37db5273eb1860b03dfc3e061bb82d84d",
    "f3f8f9f6cb93077e1becb89e68d4d7d36502e8f22a7673aefc6f4a02eab847a2",
    "05a231bbe05ba984382b05c77d340a521c8d41c15c4d051e3c99857b9416e865",
]
# no meaningful checking to be done
options = [
    "!check",
    "!debug",
    "!strip",
    "!scanrundeps",
    "!scanshlibs",
    "!lto",
    "textrels",
    "execstack",
    "foreignelf",  # vdso32
]

_flavor = "fairphone-fp5"

if self.current_target == "custom:generate-configs":
    hostmakedepends += ["base-cross", "ncurses-devel"]


#if self.profile().cross:
#    broken = "linux-devel does not come out right"


# generate fp5_ALLYES_GKI.config from fp5_GKI.config: ./scripts/gki/fragment_allyesconfig.sh arch/arm64/configs/vendor/fp5_GKI.config arch/arm64/configs/vendor/fp5_ALLYES_GKI.config
@custom_target("generate-configs", "patch")
def _(self):
    from cbuild.util import linux

    linux.update_configs(self, archs, _flavor)


def configure(self):
    from cbuild.util import linux

    linux.configure(self, _flavor)


def build(self):
    from cbuild.util import linux

    linux.build(self, _flavor)


def install(self):
    from cbuild.util import linux

    linux.install(self, _flavor)


@subpackage("linux-fairphone-fp5-devel")
def _(self):
    self.depends += ["clang"]
    self.options = ["foreignelf", "execstack", "!scanshlibs"]
    return ["usr/src", "usr/lib/modules/*/build"]


@subpackage("linux-fairphone-fp5-dbg")
def _(self):
    self.options = [
        "!scanrundeps",
        "!strip",
        "!scanshlibs",
        "foreignelf",
        "execstack",
        "textrels",
    ]
    return ["usr/lib/debug", "usr/lib/modules/*/apk-dist/boot/System.map-*"]
