pkgname = "libomp"
pkgver = "18.1.8"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DLIBOMP_ENABLE_SHARED=ON",
    "-DLIBOMP_INSTALL_ALIASES=ON",
    "-DCMAKE_POSITION_INDEPENDENT_CODE=ON",
]
hostmakedepends = ["clang-tools-extra", "cmake", "ninja", "perl", "python"]
makedepends = [
    "libffi-devel",
    "linux-headers",
    "llvm-devel",
    "ncurses-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "LLVM OpenMP runtime"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0 WITH LLVM-exception AND NCSA"
url = "https://llvm.org"
source = f"https://github.com/llvm/llvm-project/releases/download/llvmorg-{pkgver}/llvm-project-{pkgver}.src.tar.xz"
sha256 = "0b58557a6d32ceee97c8d533a59b9212d87e0fc4d2833924eb6c611247db2f2a"
# no lit
options = ["!check"]

cmake_dir = "openmp"


def post_install(self):
    for f in (self.destdir / "usr/lib").glob("libomp.so.*"):
        self.install_link("usr/lib/libomp.so", f.name)
    self.install_license("LICENSE.TXT")


# armv7 CROSS FIXME:
#-- LIBOMP: Use OMPT-support     -- FALSE
#-- LIBOMP: Use OMPD-support     -- FALSE
#-- LIBOMP: Use Adaptive locks   -- FALSE
#-- check-openmp does nothing.
@subpackage("libomp-devel-static", False)
def _(self):
    self.depends = []
    self.install_if = []

    return ["usr/lib/*.a"]


@subpackage("libomp-devel")
def _(self):
    #self.depends = [self.with_pkgver("libomp-devel-static")]

    # keep libomptarget symlinks in main
    return [
        "usr/include",
        "usr/lib/libomp.so",
        "usr/lib/libgomp.so",
        "usr/lib/libiomp5.so",
        #"usr/lib/libomptarget*.bc", # FIXME
        "usr/lib/cmake/openmp",
    ]
