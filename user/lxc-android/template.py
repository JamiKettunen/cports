pkgname = "lxc-android"
pkgver = "36_git20241003"
pkgrel = 0
_commit = "82f593eadf11dd8329f11ca20ba790ab0679b5ca"
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
sha256 = "361a22f4dc915874adb6f57f206826d17307fc9330fd1ac11ebc122ca7213ee0"


def install(self):
    self.rm("lib/systemd", recursive=True)
    self.rm("etc/systemd", recursive=True)
    self.rm("etc/udev/rules.d", recursive=True)  # created via tmpfiles

    # install all
    for f in self.cwd.iterdir():
        if "debian" in str(f) or \
           ".circleci" in str(f) or \
           str(f).endswith(".patch"):
            continue
        self.install_files(f, "")

    # custom
    self.install_file(
        self.files_path / "mount-android.wrapper", "usr/libexec", mode=0o755
    )
    self.install_file(
        self.files_path / "lxc-android.wrapper", "usr/libexec", mode=0o755
    )
    self.install_service(self.files_path / "android-mounts")
    self.install_service(self.files_path / "lxc-android")
    self.install_service(self.files_path / "android.target", enable=True)

    # avoid packaged files in /var + udev rule overrides
    self.rename("var/lib/lxc", "usr/lib/lxc", relative=False)
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")

    # make Halium initrd play ball and mount its stuff in a more sensible place (we want all under /android)..
    # this is more or less the ideal cleanest config, rest of the stuff is cleaned up in /usr/lib/lxc-android/mount-android
    # for reference: https://github.com/Halium/initramfs-tools-halium/blob/dynparts/scripts/halium
    self.install_dir("usr/lib/lxc/android/rootfs")
    (self.destdir / "usr/lib/lxc/android/rootfs/MOUNTED_AT_root-android").touch()
