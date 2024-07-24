pkgname = "superd"
pkgver = "0.7.1"
pkgrel = 0
build_style = "go"
make_build_args = [
    f"-ldflags=-X main.Version={pkgver}",
    "./cmd/superd",
    "./cmd/superctl",
]
hostmakedepends = ["go", "scdoc"]
pkgdesc = "Lightweight user service supervising daemon"
maintainer = "Jami Kettunen <jami.kettuenen@protonmail.com>"
license = "GPL-3.0-or-later"
url = "https://sr.ht/~craftyguy/superd"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "59de58f43bd237c12d0e73425df954eb14dd4e87e11d990e8191aa6921ee08d3"


# FIXME: call installmisc {bash,zsh} completion & man pages
#def post_install(self):
    #from cbuild.util import make
    #make.Make(pkg)
    #make.install()
    #make.invoke(
    #    None,
    #    [
    #        "installmisc",
    #        "PREFIX=/usr",
    #        "DESTDIR=" + str(self.chroot_destdir),
    #    ]
    #)

    # TODO: make /etc/superd/services 0755 root root?
