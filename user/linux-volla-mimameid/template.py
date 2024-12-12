# FIXME: dtbs_install fails with CONFIG_BUILD_ARM64_DTB_OVERLAY_IMAGE_NAMES="mediatek/k69v1_64_k419"!
# ../scripts/Makefile.dtbinst:32: target 'k69v1_64_k419.dtbo' doesn't match the target pattern
pkgname = "linux-volla-mimameid"
pkgver = "4.19.191"
pkgrel = 0
_commit = "36ea86298e86391ddae818ac2fb39a2158f4168e"
_branch = "halium-12.0"
archs = ["aarch64"]
make_dir = "build"
hostmakedepends = ["base-kernel-devel"]
depends = ["base-kernel"]
provides = ["linux"]
pkgdesc = f"Linux kernel {pkgver[0:pkgver.rfind('.')]}.x for Volla Phone 22"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-only"
# based on https://github.com/HelloVolla/android_kernel_volla_mt6768/tree/volla-12.1
url = "https://gitlab.com/ubports/porting/reference-device-ports/android11/volla-phone-22/kernel-volla-mt6768"
source = f"{url}/-/archive/{_commit}.tar.gz"
sha256 = "2533fe3dfc8d8d2d76d4a6bd1e3a1761ab0314177b68353ea3fb45a3ab6722ee"
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

_flavor = "volla-mimameid"

if self.current_target == "custom:generate-configs":
    hostmakedepends += ["base-cross", "ncurses-devel"]


#if self.profile().cross:
#    broken = "linux-devel does not come out right"


@custom_target("generate-configs", "patch")
def _(self):
    from cbuild.util import linux

    linux.update_configs(self, archs, _flavor)


def configure(self):
    from cbuild.util import linux

    linux.configure(self, _flavor)


def build(self):
    from cbuild.util import linux

    # broken useless symlinks in -devel otherwise
    self.rm("scripts/dtc/include-prefixes/nios2")
    self.rm("scripts/dtc/include-prefixes/powerpc")

    linux.build(self, _flavor)


def install(self):
    from cbuild.util import linux

    linux.install(self, _flavor)


@subpackage("linux-volla-mimameid-devel")
def _(self):
    self.depends += ["clang"]
    self.options = ["foreignelf", "execstack", "!scanshlibs"]
    return ["usr/src", "usr/lib/modules/*/build"]


@subpackage("linux-volla-mimameid-dbg")
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
