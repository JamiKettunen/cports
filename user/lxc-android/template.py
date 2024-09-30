pkgname = "lxc-android"
pkgver = "36_git20240930"
pkgrel = 0
_commit = "c5a12a422f011ada2a19d2adf61feb36dd2a3d56"
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
source = f"https://github.com/JamiKettunen/lxc-android/archive/{_commit}.tar.gz"
sha256 = "f7ae746bfe4bd0711eecd964c446e0794dc060c0ea4c54eccaa84381f6cf02f4"
#file_modes = {"usr/libexec/lxc/lxc-user-nic": ("root", "root", 0o4755)}
#options = ["!distlicense"]


def install(self):
    self.rm("lib/systemd", recursive=True)
    self.rm("etc/systemd", recursive=True)

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
