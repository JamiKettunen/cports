pkgname = "libadwaita"
pkgver = "1.6_rc"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dexamples=true",
    "-Dtests=true",
    "-Dgtk_doc=false",
    "-Dvapi=true",
    "-Dintrospection=enabled",
]
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "meson",
    "pkgconf",
    "sassc",
    "vala-devel",
]
makedepends = [
    "appstream-devel",
    "glib-devel",
    "gtk4-devel",
    "harfbuzz-devel",
]
checkdepends = ["fonts-cantarell-otf", "xwayland-run"]
pkgdesc = "GTK4 building blocks for modern adaptive applications"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gitlab.gnome.org/GNOME/libadwaita"
source = f"$(GNOME_SITE)/libadwaita/{pkgver[:3]}/libadwaita-{pkgver.replace('_', '.')}.tar.xz"
sha256 = "0b88bbc04e9d68f7e2c3ea886081afe1091e5be44a32d09018cbf78a9ffbb9b7"
options = ["!cross"]


@subpackage("libadwaita-devel")
def _(self):
    return self.default_devel()


@subpackage("libadwaita-demo")
def _(self):
    self.subdesc = "demo application"
    return [
        "usr/bin/adwaita-1-demo",
        "usr/share",
    ]
