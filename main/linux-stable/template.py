# update linux-stable-zfs-bin when bumping
pkgname = "linux-stable"
pkgver = "6.7.0"
pkgrel = 0
archs = ["aarch64", "ppc64le", "ppc64", "riscv64", "x86_64"]
make_dir = "build"
hostmakedepends = ["base-kernel-devel"]
depends = ["base-kernel"]
provides = ["linux"]
pkgdesc = f"Linux kernel {pkgver[0:pkgver.rfind('.')]}.x"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://kernel.org"
source = f"https://cdn.kernel.org/pub/linux/kernel/v{pkgver[0]}.x/linux-{pkgver[:-2]}.tar.xz"
sha256 = "ef31144a2576d080d8c31698e83ec9f66bf97c677fa2aaf0d5bbb9f3345b1069"
# no meaningful checking to be done
options = [
    "!check",
    "!debug",
    "!strip",
    "!scanrundeps",
    "!scanshlibs",
    "!linkparallel",
    "!lto",
    "textrels",
    "execstack",
    "foreignelf",  # vdso32
]

_flavor = "generic"
# set to True to refresh kernel configs
_conf = False

if _conf:
    hostmakedepends += ["base-cross", "ncurses-devel"]


def init_configure(self):
    # generate scriptlets for packaging, just hooking to base-kernel helpers
    from cbuild.util import linux

    if not _conf:
        linux.generate_scriptlets(self, _flavor)


def do_configure(self):
    from cbuild.util import linux

    if _conf:
        linux.update_configs(self, archs, _flavor)
    else:
        linux.configure(self, _flavor)


def do_build(self):
    from cbuild.util import linux

    linux.build(self, _flavor)


def do_install(self):
    from cbuild.util import linux

    linux.install(self, _flavor)

    if self.profile().cross:
        # -devel does not come out right for crossbuilds
        self.rm(self.destdir / "usr/src", recursive=True)
        self.rm(self.destdir / f"usr/lib/modules/*/build", glob=True)

    if not self.build_dbg:
        self.rm(self.destdir / "usr/lib/debug", recursive=True)
        self.rm(self.destdir / f"boot/System.map-*", glob=True)


@subpackage("linux-stable-devel", not self.profile().cross)
def _devel(self):
    self.depends += ["clang"]
    self.options = ["foreignelf", "execstack", "!scanshlibs"]
    return ["usr/src", "usr/lib/modules/*/build"]


@subpackage("linux-stable-dbg", self.build_dbg)
def _dbg(self):
    self.pkgdesc += " (debug files)"
    self.options = [
        "!scanrundeps",
        "!strip",
        "!scanshlibs",
        "foreignelf",
        "execstack",
        "textrels",
    ]
    return ["usr/lib/debug", "boot/System.map-*"]
