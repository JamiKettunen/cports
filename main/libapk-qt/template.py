pkgname = "libapk-qt"
pkgver = "0.4.6"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_TESTING=ON"]
# no network
make_check_args = ["-E", "test_(db_update|add)"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["apk-tools-devel", "qt6-qtbase-devel"]
pkgdesc = "Qt bindings for Alpine Package Keeper"
license = "GPL-2.0-only"
url = "https://gitlab.postmarketos.org/postmarketOS/libapk-qt"
source = f"{url}/-/archive/v{pkgver}/libapk-qt-v{pkgver}.tar.gz"
sha256 = "b58cee4cd66b63a44ebcf4b74ff34fd62d0aed06fb866ff6ec12853122807bee"


@subpackage("libapk-qt-devel")
def _(self):
    return self.default_devel()
