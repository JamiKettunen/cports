pkgname = "coreutils"
pkgver = "9.5"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
#    "--enable-acl",
    "--program-prefix=g",
#    "gl_cv_func_working_acl_get_file=yes",
#    "ac_cv_lib_error_at_line=no",
#    "ac_cv_header_sys_cdefs_h=no",
]
hostmakedepends = ["automake", "gettext-devel"]
# TODO: acl-devel attr-devel utmps-devel openssl-devel perl?
#makedepends = [""]
#checkdepends = ["perl", "bash"]
pkgdesc = "GNU basic file, shell and text manipulation utilities"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-3.0-or-later"
url = "https://www.gnu.org/software/coreutils"
source = f"$(GNU_SITE)/coreutils/coreutils-{pkgver}.tar.xz"
sha256 = "cd328edeac92f6a665de9f323c93b712af1858bc2e0d88f3f7100469470a1b8a"
hardening = ["vis", "cfi"]
# FIXME: chgrp (basic/recurse/posix-H/no-x/default-no-deref) tests fail for now, at least just skip those?
# your system doesn't support changing the owner or group of a symbolic link.
options = ["!check"]
