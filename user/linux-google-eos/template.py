pkgname = "linux-google-eos"
pkgver = "5.15.144"
pkgrel = 0
_commit = "97af53830f6a88ca03cb2c987ff75f845d32fdef"
_branch = "halium-13.0"
archs = ["aarch64"]
make_dir = "build"
hostmakedepends = ["base-kernel-devel"]
depends = ["base-kernel"]
provides = ["linux"]
pkgdesc = f"Linux kernel {pkgver[0:pkgver.rfind('.')]}.x for Google Pixel Watch 2"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-only"
# based on https://android.googlesource.com/kernel/msm/+/refs/heads/android-msm-eos-android13-wear-kr3-pixel-watch
url = "https://gitlab.com/ubports/porting/community-ports/android13/google-eos/kernel-for-google-eos"
source = f"{url}/-/archive/{_commit}.tar.gz"
sha256 = "5322ed10d6db8deca3c908cefba39259056f5a1c3eeb7061a3d0b07393b2d282"
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

_flavor = "google-eos"

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


@subpackage("linux-google-eos-devel")
def _(self):
    self.depends += ["clang"]
    self.options = ["foreignelf", "execstack", "!scanshlibs"]
    return ["usr/src", "usr/lib/modules/*/build"]


@subpackage("linux-google-eos-dbg")
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
