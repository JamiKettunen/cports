pkgname = "libgbinder"
pkgver = "1.1.40"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_build_args = ["release", "pkgconfig", "KEEP_SYMBOLS=1"]
make_install_target = "install-dev"
make_check_target = "test"
# TODO: ensure hardening flags etc are properly passed
# https://github.com/chimera-linux/cports/blob/master/Packaging.md#makefile
make_use_env = True
hostmakedepends = ["gmake", "pkgconf"]
makedepends = ["libglibutil-devel", "linux-headers"]
pkgdesc = "GLib-style interface to binder, the Android IPC mechanism"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "BSD-3-Clause"
url = "https://github.com/mer-hybris/libgbinder"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "9e86243df6502ffd0a68ee8384c5c36b9cd4093733ea620313f1947f312abbd1"
# FIXME: vis hides gbinder_bridge_free symbol required by gbinder-python,
#        cfi makes unit_bridge etc SIGILL, see similar libglibutil commits
hardening = ["!vis", "!cfi"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libgbinder-devel")
def _devel(self):
    return self.default_devel()
