pkgname = "sxmo-utils"
pkgver = "1.16.3_git20240720"
pkgrel = 0
#archs = ["x86_64", "aarch64"]
build_style = "makefile"
make_cmd = "gmake"
make_install_args = [
    "OPENRC=0",
    f"VERSION={pkgver}",
    #"EXTERNAL_SERVICES=0",
    #"SERVICEDIR=/usr/lib/dinit.d/user",
    #"install-scripts", "install-docs"
]
make_check_target = "test"
# TODO: busybox before coreutils! maybe even swap ginstall later for bbinstall
hostmakedepends = ["gmake", "scdoc", "libcap-progs", "coreutils"]
makedepends = ["linux-headers"]
# cronie
depends = [
    "bemenu-wayland",
    "mako",
    "wob",
    "lisgd",
    "foot",
    "superd",
    "libpulse-progs",
    "mpv",
    "clickclack",
    "bonsai",
    "wvkbd",
    "inotify-tools",
    "jq", # TODO: gojq no longer needed?
    "swaylockd",
]
pkgdesc = "Scripts and C programs to support Sxmo"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "AGPL-3.0-only"
url = "https://sxmo.org"
_commit = "c5f4abff77a3b1c2ed3b54f7ae79acd0ad904120"
source = f"https://git.sr.ht/~mil/sxmo-utils/archive/{_commit}.tar.gz"
sha256 = "27eec3543f5fb20f907de294f5ab7ad135d16b9ebb5d19e1ecf8d24fff9d5517"
# silence >2k lines of aarch64 build-time spam
#tool_flags = {"CFLAGS": ["-Wno-asm-operand-widths"]}
file_modes = {
    "usr/bin/sxmo_sleep": ("root", "root", 0o755),
}
file_xattrs = {
    "usr/bin/sxmo_sleep": {
        "security.capability": "cap_wake_alarm=ep", # TODO: cap_wake_alarm+ep?
    },
}
hardening = ["vis", "cfi"]
# unpackaged shellspec/shellcheck
options = ["!check"]
# FIXME: patch Makefile to be BSD install(1) compatible & drop coreutils hostmakedep
exec_wrappers = [("/usr/bin/ginstall", "install")]


def post_install(self):
    self.install_license("LICENSE")

    # TODO: drop superd fully once chimera dinit user services are capable of graphical stuff!
    # - rm usr/share/superd? usr/share/sxmo/external-services usr/share/sxmo/services
    # - install_args += EXTERNAL_SERVICES=0 SERVICEDIR=/usr/lib/dinit.d/user
    # TODO: run "pipewire -c filter-chain.conf"?
    for s in ["pipewire-filter-chain", "pipewire-pulse", "pipewire", "wireplumber"]:
        self.rm(self.destdir / f"usr/share/superd/services/{s}.service")
        self.rm(self.destdir / f"usr/share/sxmo/external-services/{s}.service")

    # TODO: X11 (dwm) session subpackage? meh
    self.rm(self.destdir / "usr/bin/sxmo_xinit.sh")
    self.rm(self.destdir / "usr/share/X11/xorg.conf.d/90-monitor.conf")
    self.rm(self.destdir / "usr/share/xsessions/sxmo.desktop")
    self.rm(self.destdir / "usr/share/sxmo/xorg/monitor.conf")
    self.rm(self.destdir / "usr/bin/sxmo_status_xsetroot.sh")
    # usr/share/superd/services/sxmo-x11-status.service
    # usr/share/sxmo/services/sxmo-x11-status.service


@subpackage("sxmo-utils-meta")
def _meta(self):
    self.subdesc = "recommends package"
    self.options = ["empty"]
    self.install_if = [self.parent]
    self.depends = [
        "foot",
        #"modemmanager",
        #"fonts-nerd-fonts", -> only pick one?!
        #"pnc",
        #"mmsd-tng",
        #"swipeguess",
        #"tinydm", # FIXME: missing autologin dep?
        "wayout",
        "fonts-nerd-dejavu-sans-mono",
        "wayout",
    ]
    return []


# FIXME:
# - dinitctl enable sxmo-setpermissions (TODO: add service)
# - sed broken during build ()


# TODO:
# - drop X11 session switch entry entirely (maybe it already is without dwm detected)
# - main/opendoas
#   - add https://gitlab.alpinelinux.org/alpine/aports/-/blob/master/main/doas/configuration-directory.patch to main/opendoas/patches
#   - confkgure with --with-doas-confdir
#   - bump-pkgrel
#   - submit upstream?
# - optional docs? scdoc mandatory now
# - sxmo_vibrate build warning (https://paste.c-net.org/ribxa3tinrru)
# - disable modemmanager integration (and other calls/texting/contacts related stuff), configurable already on non-LTE devices?
#   - set SXMO_NO_MODEM=1 at least, should further tweaks be done
# - enable cronie (crond) by default?
# - post_upgrade message
#   - After an upgrade, it is recommended you reboot and when prompted run sxmo_migrate.sh to check and upgrade your configuration files and custom hooks against the defaults (it will not make any changes unless explicitly told to)
# - hide bar when launching waydroid?
# - clickclack: only audio without vibration?
# - SXMO_DEBUG=1 -> ${XDG_STATE_HOME:-$HOME}/sxmo.log
