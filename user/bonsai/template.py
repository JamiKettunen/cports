pkgname = "bonsai"
pkgver = "1.1.0"
pkgrel = 0
build_style = "makefile"
hostmakedepends = ["hare", "hare-json", "hare-ev"]
pkgdesc = "Finite State Machine structured as a tree that trigger commands"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "AGPL-3.0-or-later"
url = "https://sr.ht/~stacyharper/bonsai"
source = f"https://git.sr.ht/~stacyharper/bonsai/archive/v{pkgver}.tar.gz"
sha256 = "de4f7c3bbc7e6eafc41108d448207fa8409087119fd7328173eaf8aca1928123"
# FIXME: any better way to deal with this?
tools = {"AS": f"{self.profile().triplet}-as"}


def post_install(self):
    self.install_license("LICENSE")
