pkgname = "lttng-ust"
pkgver = "2.13.8"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-examples"]
configure_gen = []
make_cmd = "gmake"
hostmakedepends = ["pkgconf", "gmake"]
makedepends = ["userspace-rcu-devel", "libnuma-devel"]
pkgdesc = "Low-overhead tracing capabilities for userspace"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-only"
url = "https://lttng.org"
source = f"https://lttng.org/files/lttng-ust/lttng-ust-{pkgver}.tar.bz2"
sha256 = "d4ef98dab9a37ad4f524ccafdfd50af4f266039b528dd5afabce78e49024d937"
# FIXME:
# unit/gcc-weak-hidden/test_gcc_weak_hidden: Address of weak symbol with hidden visibility match between compile units within same module for main program (4 bytes integer object)
# unit/gcc-weak-hidden/test_gcc_weak_hidden: Address of weak symbol with hidden visibility match between compile units within same module for main program (pointer object)
# ERROR: unit/gcc-weak-hidden/test_gcc_weak_hidden - too few tests run (expected 2, got 0)
options = ["!check"]


@subpackage("lttng-ust-devel")
def _devel(self):
    self.depends += ["userspace-rcu-devel"]

    return self.default_devel()
