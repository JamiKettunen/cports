pkgname = "hare-json"
pkgver = "0.24.2"
pkgrel = 0
build_style = "makefile"
hostmakedepends = ["hare"]
pkgdesc = "JSON support for Hare"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "MPL-2.0"
url = "https://git.sr.ht/~sircmpwn/hare-json"
source = f"https://git.sr.ht/~sircmpwn/hare-json/archive/{pkgver}.tar.gz"
sha256 = "3b3087b7abbdf67a87592122335ebfbebf5588314c43330fef11512296e83507"
# FIXME: any better way to deal with this?
tools = {"AS": f"{self.profile().triplet}-as"}
