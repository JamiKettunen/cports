pkgname = "lxc-android"
pkgver = "36"
pkgrel = 0
depends = [
    "lxc",
    "parse-android-dynparts",
    "halium-wrappers",
    "lsof",
    "android-libhybris-users",
]
pkgdesc = "Configuration to start Android inside an LXC container"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "custom:none"
url = "https://github.com/droidian/lxc-android"
source = f"{url}/archive/refs/tags/droidian/next/1%25{pkgver}.tar.gz"
sha256 = "b88de056356f9a123755aed784744c9edabac439d7d33b5c23502f496eaa89a2"
#file_modes = {"usr/libexec/lxc/lxc-user-nic": ("root", "root", 0o4755)}
#options = ["!distlicense"]


def install(self):
    self.rm("lib/systemd", recursive=True)
    self.rm("etc/systemd", recursive=True)

    # fix forbidden paths not applied due to bsdpatch
    self.mv("lib/udev", "usr/lib")
    self.mkdir("usr/bin")
    self.mv("usr/sbin/mount-android.sh", "usr/bin")
    self.mv("etc/udev/rules.d/90-btdevice-cursorfix.rules", "usr/lib/udev/rules.d")
    self.mv("etc/udev/rules.d/90-touchscreen.rules", "usr/lib/udev/rules.d")

    # legacy kernel 3.4 firmware loader crap gone from modern udev
    self.rm("etc/udev/rules.d/50-firmware.rules")
    # alsa-utils remains unpackaged (for now)
    self.rm("etc/udev/rules.d/90-alsa-restore.rules")
    self.rm("etc/udev/rules.d/90-alsa-ucm.rules")
    # FIXME: /usr/lib/udev/rules.d/60-persistent-v4l.rules already exists and should be overridden with nothing...
    # TODO: move these to /run/udev/rules.d creating the /dev/null symlinks at runtime?
    self.rm("etc/udev/rules.d/60-persistent-v4l.rules")

    # install all
    for f in self.cwd.iterdir():
        if "debian" in str(f) or \
           ".circleci" in str(f) or \
           str(f).endswith(".patch"):
            continue
        self.install_files(f, "")

    self.install_file(
        self.files_path / "mount-android.wrapper", "usr/libexec", mode=0o755
    )
    self.install_file(
        self.files_path / "lxc-android.wrapper", "usr/libexec", mode=0o755
    )
    self.install_service(self.files_path / "android-mounts")
    self.install_service(self.files_path / "lxc-android")
    self.install_service(self.files_path / "android.target", enable=True)

    # FIXME: /var/lib/lxc/android/{config,post-stop.sh,pre-start.sh} now invalid path


#@subpackage("lxc-android-emmc")
#def _(self):
#    self.subdesc = "hint mmcblk0 as UDISKS_SYSTEM"
#    # FIXME: autosplit to lxc-android-udev already
#    return ["usr/lib/udev/rules.d/99-android.rules"]
