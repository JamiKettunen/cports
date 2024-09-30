pkgname = "linux-mainline"
pkgver = "6.11_rc6"
#pkgver = "6.10_git20240723"
pkgrel = 0
archs = ["x86_64"]
make_dir = "build"
hostmakedepends = ["base-kernel-devel"]
depends = ["base-kernel"]
provides = ["linux"]
pkgdesc = f"Linux mainline kernel v{pkgver.replace('_', '-')}"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://kernel.org"
source = f"https://git.kernel.org/torvalds/t/linux-{pkgver.replace('_', '-')}.tar.gz"
#source = "https://github.com/torvalds/linux/archive/66ebbdfdeb093e097399b1883390079cd4c3022b.tar.gz"
sha256 = "681eaab679a6c9675270f45ccea69c2ed406c140dd8935cae8a825d653e2b545"
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

_flavor = "generic"

if self.current_target == "custom:generate-configs":
    hostmakedepends += ["base-cross", "ncurses-devel"]

if self.profile().cross:
    broken = "linux-devel does not come out right"


@custom_target("generate-configs", "patch")
def _(self):
    from cbuild.util import linux

    linux.update_configs(self, archs, _flavor)


def init_configure(self):
    # generate scriptlets for packaging, just hooking to base-kernel helpers
    from cbuild.util import linux

    linux.generate_scriptlets(self, _flavor)


def configure(self):
    from cbuild.util import linux

    linux.configure(self, _flavor)


def build(self):
    from cbuild.util import linux

    linux.build(self, _flavor)


def install(self):
    from cbuild.util import linux

    linux.install(self, _flavor)

    if not self.build_dbg:
        self.uninstall("usr/lib/debug", recursive=True)
        self.uninstall(f"boot/System.map-{pkgver}-{pkgrel}-{_flavor}")

@subpackage("linux-mainline-devel")
def _(self):
    self.depends += ["clang"]
    self.options = ["foreignelf", "execstack", "!scanshlibs"]
    return ["usr/src", "usr/lib/modules/*/build"]


@subpackage("linux-mainline-dbg", self.build_dbg)
def _(self):
    self.options = [
        "!scanrundeps",
        "!strip",
        "!scanshlibs",
        "foreignelf",
        "execstack",
        "textrels",
    ]
    return ["usr/lib/debug", "boot/System.map-*"]
