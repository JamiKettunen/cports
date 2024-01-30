pkgname = "droid-juicer"
pkgver = "0.2.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo"]
makedepends = ["rust-std", "linux-headers"]
pkgdesc = "Extract firmware from Android vendor partitions"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "MIT"
url = "https://gitlab.com/mobian1/droid-juicer"
source = f"{url}/-/archive/{pkgver}.tar.gz"
sha256 = "5934af76d30e4df629b1e868bd29d189a3e7f9acb999224d2f03af47929e92ae"


def post_install(self):
    # FIXME: manually replicate 2nd part of op5.patch as FreeBSD patch(1) can't cope with symlink creation
    self.ln_s("oneplus,cheeseburger.toml", "configs/oneplus,dumpling.toml")
    self.cp(
        "configs",
        self.destdir / "usr/share/droid-juicer/configs",
        recursive=True,
    )
    self.install_file("config.toml.sample", "usr/share/examples/droid-juicer")
    self.install_file("README.md", "usr/share/doc/droid-juicer")
    self.install_license("LICENSE")


# 	vmkdir etc/runit/core-services
# 	vinstall ${FILESDIR}/02-droid-juicer.sh 644 etc/runit/core-services

# 02-droid-juicer.sh:
# # Setup firmware during first boot before loading kernel modules
#
# [ -f /proc/device-tree/compatible ] || return 0 # pre-requisite for device model detection
# [ -f /var/lib/droid-juicer/status.json ] && return 0 # avoid running on subsequent boots
#
# msg "Extracting firmware from Android vendor partitions...\n"
# grep -q ' / .*ro' /proc/mounts && mount -o remount,rw /
# droid-juicer
# # TODO:
# # - print custom messsage if no config found?
# # - what does the output from this look like?
# # - we don't need to reboot if this is done before kernel modules are loaded correct?
# #echo

# TODO: once plymouth is around (as seen in https://gitlab.com/mobian1/droid-juicer/-/commit/def1459f)
# plymouth display-message --text="Extracting binary firmware..."
