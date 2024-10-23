pkgname = "gdb"
pkgver = "15.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-werror",
    "--disable-nls",
    "--with-system-zlib",
    "--with-system-zstd",
    "--with-system-readline",
    "--with-system-gdbinit=/etc/gdb/gdbinint",
    #"--with-python=/usr/bin/python",
]
# needs autoconf 2.69
configure_gen = []
hostmakedepends = ["gsed", "pkgconf", "texinfo"]#, "python-devel"
makedepends = [
    "elfutils-devel",
    "gettext-devel",
    "gmp-devel",
    "libexpat-devel",
    "linux-headers",
    "mpfr-devel",
    "ncurses-devel",
    #"python-devel",
    "readline-devel",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
depends = [self.with_pkgver("gdb-common")]
pkgdesc = "GNU debugger"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://www.gnu.org/software/gdb"
source = f"$(GNU_SITE)/gdb/gdb-{pkgver}.tar.xz"
sha256 = "83350ccd35b5b5a0cba6b334c41294ea968158c573940904f00b92f76345314d"
# weird autotools bullshittery
env = {"SED": "gsed"}
# massive
options = ["!check"]
# cross FIXME:
#checking for python... no
#configure: error: no usable python found at /usr/bin/python
#make[1]: *** [Makefile:11025: configure-gdb] Error 1
#make[1]: Leaving directory '/builddir/gdb-15.2/build'
#make: *** [Makefile:1028: all] Error 2



#def init_build(self):
#    if self.profile().cross:
#        # fix python detection
#        self.configure_env = {"CPPFLAGS": f"-I{self.profile().sysroot}/usr/include/python{self.python_version}"}


def post_install(self):
    #from cbuild.util import python

    self.uninstall("usr/lib")
    self.uninstall("usr/include")
    # may conflict with binutils
    self.uninstall("usr/share/info/bfd.info")
    self.uninstall("usr/share/info/ctf-spec.info")
    self.uninstall("usr/share/info/sframe-spec.info")

    #python.precompile(self, "usr/share/gdb/python")


@subpackage("gdb-common")
def _(self):
    self.subdesc = "common files"

    return ["usr/share"]
