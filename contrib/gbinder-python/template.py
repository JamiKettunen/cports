pkgname = "gbinder-python"
pkgver = "1.1.2"
pkgrel = 0
build_style = "python_pep517"
make_build_env = {"WITH_CYTHON": "true"}
hostmakedepends = [
    "python-build",
    "python-setuptools",
    "python-cython",
    "python-installer",
    "pkgconf",
]
makedepends = ["python-devel", "libgbinder-devel"]
#depends = ["libgbinder"] # python
pkgdesc = "Python bindings for libgbinder"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-3.0-or-later"
url = "https://github.com/erfanoabdi/gbinder-python"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "2dc424d5c2594146612e4bd752964f8928a62eec7c5ce6046f4c582079d0b537"
# no testsuite
# !cross TODO: re-check if still looks for headers on host and refuses to find gutil_types.h regardless of where libglibutil-devel is added
options = ["!check"]


# TODO: might later need https://github.com/erfanoabdi/gbinder-python/pull/12 (setuptools migration)
