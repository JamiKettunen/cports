pkgname = "sxmo-utils"
pkgver = "1.16.3_git20240721"
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
depends = [
    "opendoas", # TODO: base-full-misc?
    "bc-gh", # TODO: base-full-misc?
    "less", # TODO: base-full-misc?
    "iproute2", # TODO: base-full-net-tools?
    "networkmanager",
    "xdg-user-dirs",
    "lisgd",
    "superd",
    "libpulse-progs",
    "clickclack",
    "inotify-tools",
    "jq", # TODO: gojq no longer needed?
    "mpv",
    "brightnessctl",
    "libnotify",
    "upower",
    #iio-utils # TODO: proximitylock
    #geoclue # TODO: does this even work?
    "cronie",
    "mnc", # suspend/cron, FIXME: package!
]
triggers = ["/usr/share/sxmo"]
pkgdesc = "Scripts and C programs to support Sxmo"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "AGPL-3.0-only"
url = "https://sxmo.org"
_commit = "c5f4abff77a3b1c2ed3b54f7ae79acd0ad904120"
source = f"https://git.sr.ht/~mil/sxmo-utils/archive/{_commit}.tar.gz"
sha256 = "27eec3543f5fb20f907de294f5ab7ad135d16b9ebb5d19e1ecf8d24fff9d5517"
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

    # TODO: prevent logind from handling the power button
    self.install_files(self.files_path / "10-sxmo-powerkey.conf", "etc/elogind/logind.conf.d")

    # TODO: drop superd fully once chimera dinit user services are capable of graphical stuff!
    # - rm usr/share/superd? usr/share/sxmo/external-services usr/share/sxmo/services
    # - install_args += EXTERNAL_SERVICES=0 SERVICEDIR=/usr/lib/dinit.d/user
    # - https://aur.archlinux.org/cgit/aur.git/tree/0005-Add-hook-to-manage-services.patch?h=sxmo-utils-git
    # - https://github.com/dreemurrs-embedded/Pine64-Arch/blob/master/PKGBUILDS/sxmo/sxmo-utils/0001-avoid-conflicting-with-systemd-services.patch
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

    # TODO: Allow user access to manage ModemManager
    # -> /usr/share/polkit-1/rules.d/50-org.freedesktop.NetworkManager.rules already installed by networkmanager pkg
    #self.install_files(self.files_path / "00-sxmo-nm-mm.rules", "usr/share/polkit-1/rules.d")

    # TODO: sxmo_setpermissions.sh service (seems to now be removed?! https://gitlab.com/postmarketOS/pmaports/-/merge_requests/4659/diffs)
    # - FIXME: remove stale reference from source Makefile


# TODO: -cellullar-meta subpackage depending on modemmanager/callaudiod/pnc/mmsd-tng


@subpackage("sxmo-utils-meta")
def _meta(self):
    self.subdesc = "recommends package"
    self.options = ["empty"]
    self.install_if = [self.parent]
    self.depends = [
        "yt-dlp", # play online videos
        "sfeed", # rss/atom feeds
        #"pipewire", TODO: leave base-* pkgs to take care of this?
        "fonts-nerd-dejavu-sans-mono", # fonts-nerd-fonts
        #terminus-font (TODO: not packaged)
        #fonts-dejavu
        #alsa-utils # TODO: package for sxmo_record.sh appscript?
        "mediainfo",
        "clickclack",
        "tinydm",
        "firefox",
        # mobile-config-firefox (https://gitlab.com/postmarketOS/mobile-config-firefox) / mobile-friendly-firefox (https://codeberg.org/user0/Mobile-Friendly-Firefox)?
        #"w3m",
        #screen
        "bluez",
        "curl", # what about wget2/aria2 in sxmo_urlhandler.sh?
        #(arch only? highlight)
        #unzip
        "gawk", # yt/rss scripts
        "bemenu-curses", # sxmo menus over ssh
        "bonsai", # modern multikey daemon (compat in sxmo_swayinitconf.sh)
        #codemadness-frontends # yt/reddit scripts
        #"vim", # default editor
        #ffmpeg ffplay # ??
    ]
    return []


@subpackage("sxmo-utils-sway")
def _sway(self):
    self.subdesc = "sway session"
    self.options = ["empty"]
    self.install_if = [self.parent]
    self.depends = [
        "sway", # TODO: what other sway deps?!
        # swaybg
        # swayidle
        # (swaync swaylock swayimg wlr-randr xdg-desktop-portal-wlr pinentry-bemenu)
        "bemenu-wayland",
        "foot",
        "wvkbd",
        #"swipeguess", # FIXME:
        "wayout",
        "swaylockd",
        "wtype",
        #"xwayland", # TODO: ?
        "mako",
        "wob",
        "wl-clipboard",
        "grim",
        "slurp",
    ]
    return []


# TODO: X11 variant instead with i3lock/conky/dwm/svkbd/autocutsel/sxiv/xrandr/feh/dunst


# FIXME:
# - dinitctl enable sxmo-setpermissions (TODO: add service)


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
# - hide bar when launching waydroid?
# - SXMO_DEBUG=1 -> ${XDG_STATE_HOME:-$HOME}/sxmo.log
# - fix sxmo_autorotate.sh to read monitor-sensor (iio-sensor-proxy) output
#   - see sxmo_battery_monitor.sh which already does this with upower
# - do something with ambient light sensor (iio) and change brightness which GNOME couldn't get right? including smooth transitions over 1 second at least
# - auto-open gnome keyring?
# - tweak top bar right side to show power draw in watts etc
# - audio volume shown always as muted?!
# - swayfx? what about wlroots-git/sway-git
# - /usr/share/sxmo/default_hooks/sxmo_hook_desktop_widget.sh not auto-started?
# - cannot type '|' for some reason (even tho layout looks correct mostly)?!
# - better lockscreen theming
# - better overall theming (https://wiki.postmarketos.org/wiki/Sxmo/Tips_and_Tricks#wayland/sway / https://porkyofthepine.org/blog/rice_sxmo_sway.html)
# - what's the deal with stuff printed in top panel right side status? "!:       0"
# - holding keys (especially backspace) is annoying with wvkbd: need to have finger still the whole damn time
