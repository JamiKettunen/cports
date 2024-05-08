pkgname = "libxml++-2.6"
pkgver = "2.42.3"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["libxml2-devel", "glibmm2.4-devel"]
pkgdesc = "XML parsing library C++ bindings"
license = "LGPL-2.1-only"
url = "https://libxmlplusplus.github.io/libxmlplusplus"
source = f"$(GNOME_SITE)/libxml++/{pkgver[:pkgver.rfind('.')]}/libxml++-{pkgver}.tar.xz"
sha256 = "74b95302e24dbebc56e97048e86ad0a4121fc82a43e58d381fbe1d380e8eba04"
# FIXME: failed to apply 'kill-auto_ptr.patch'
patch_style = "patch"
# silence some really loud warnings...
tool_flags = {"CXXFLAGS": ["-Wno-deprecated-declarations"]}


@subpackage("libxml++-2.6-devel")
def _(self):
    return self.default_devel()
