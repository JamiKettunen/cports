pkgname = "linux-android12-5.10"
pkgver = "5.10.230"
pkgrel = 0
_commit = "26acf0ab759bc0b14c076f203a9eb6b0c3a1192b"
archs = ["aarch64"]
make_dir = "build"
hostmakedepends = ["base-kernel-devel"]
depends = ["base-kernel"]
provides = ["linux"]
pkgdesc = f"Linux kernel {pkgver[0:pkgver.rfind('.')]}.x for Android 12 GKI-compatible devices"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-only"
url = (
    "https://android.googlesource.com/kernel/common/+/refs/heads/android12-5.10"
)
source = (
    f"https://android.googlesource.com/kernel/common/+archive/{_commit}.tar.gz"
)
sha256 = "42d470117a95144e4999fd520c710851cfdf73efa01c75139ff981d1052f0311"
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

_flavor = "android12-5.10"

if self.current_target.startswith("custom:"):
    hostmakedepends += ["base-cross", "ncurses-devel"]


# if self.profile().cross:
#     broken = "linux-devel does not come out right"


def post_patch(self):
    self.cp(self.files_path / "*.config", "arch/arm64/configs", glob=True)


@custom_target("generate-configs", "patch")
def _(self):
    from cbuild.util import linux

    linux.update_configs(
        self, archs, _flavor, "gki_defconfig halium.config ut.config"
    )


@custom_target("menuconfig", "patch")
def _(self):
    from cbuild.util import linux

    linux.update_configs(self, archs, _flavor, "menuconfig")


def configure(self):
    from cbuild.util import linux

    linux.configure(self, _flavor)


def build(self):
    from cbuild.util import linux

    linux.build(self, _flavor)


def install(self):
    from cbuild.util import linux

    linux.install(self, _flavor)


@subpackage("linux-android12-5.10-devel")
def _(self):
    self.depends += ["clang"]
    self.options = ["foreignelf", "execstack", "!scanshlibs"]
    return ["usr/src", "usr/lib/modules/*/build"]


@subpackage("linux-android12-5.10-dbg")
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
