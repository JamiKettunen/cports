pkgname = "autologin"
pkgver = "1.0.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson"]
makedepends = ["linux-pam-devel", "linux-headers"]
pkgdesc = "Automatically login as a user"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-3.0-or-later"
url = "https://git.sr.ht/~kennylevinsen/autologin"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "eb084620e660c3d1708beb58cd3520220ad05b5f628378c3118c36379b33221a"
hardening = ["vis", "!cfi"]
# no tests defined
#options = ["!check"]


# TODO: patch turnstiled pam stuff in like GDM:
# -session optional pam_turnstile.so
# -session optional pam_elogind.so

# FIXME: create /etc/pam.d/autologin (or use /etc/pam.d/login)

# TODO: test with tinydm!
