pkgname = "linux-volla-vidofnir"
pkgver = "5.10.160"
pkgrel = 0
_commit = "afbc07373d40cc083933134815250bd14cc7afa4"
_branch = "halium-12.0-gx4pro"
archs = ["aarch64"]
make_dir = "build"
hostmakedepends = ["base-kernel-devel"]
depends = ["base-kernel"]
provides = ["linux"]
pkgdesc = f"Linux kernel {pkgver[0:pkgver.rfind('.')]}.x for Volla Phone X23"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-only"
# based on https://github.com/HelloVolla/android_kernel_volla_mt6789/tree/volla-12.1
url = "https://gitlab.com/ubports/porting/reference-device-ports/halium12/volla-x23/kernel-volla-mt6789"
source = f"{url}/-/archive/{_commit}.tar.gz"
sha256 = "08cdfb3fb29634ac6bf4ec7e5d992168f654bcfbe666c1d2e9847473056a95d6"
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

_flavor = "volla-vidofnir"

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

    linux.build(self, _flavor)


def install(self):
    from cbuild.util import linux

    linux.install(self, _flavor)


@subpackage("linux-volla-vidofnir-devel")
def _(self):
    self.depends += ["clang"]
    self.options = ["foreignelf", "execstack", "!scanshlibs"]
    return ["usr/src", "usr/lib/modules/*/build"]


@subpackage("linux-volla-vidofnir-dbg")
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
