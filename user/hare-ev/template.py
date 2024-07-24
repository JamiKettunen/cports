pkgname = "hare-ev"
pkgver = "0_git20240711"
pkgrel = 0
build_style = "makefile"
hostmakedepends = ["hare"]
pkgdesc = "Event loop for Hare"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "MPL-2.0"
url = "https://git.sr.ht/~sircmpwn/hare-json"
_commit = "ed023beb4b4db88e22f608aa001682ac18cad230"
source = f"https://git.sr.ht/~sircmpwn/hare-ev/archive/{_commit}.tar.gz"
sha256 = "19ea194583802f8b21c37a650151ae84c7863344da17cff4515690f60c688875"
# FIXME: any better way to deal with this?
tools = {"AS": f"{self.profile().triplet}-as"}
