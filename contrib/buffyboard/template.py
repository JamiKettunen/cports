pkgname = "buffyboard"
pkgver = "0.2.0"
_lv_drivers_commit = "33983bcb0a9bfd0a4cf44dba67617b9f537e76f3"
_lvgl_commit = "a2b555e096f7d401b5d8e877a6b5e81ff81c747a"
_squeek2lvgl_commit = "e3ce01bc38020b21bc61844fa1fed1a4f41097c5"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["libinput-devel", "libxkbcommon-devel"]
pkgdesc = "Touch-enabled framebuffer keyboard for TTY"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-3.0-or-later"
url = "https://gitlab.com/cherrypicker/buffyboard"
source = [
    f"{url}/-/archive/{pkgver}/buffyboard-{pkgver}.tar.gz",
    f"https://github.com/lvgl/lv_drivers/archive/{_lv_drivers_commit}/lv_drivers-{_lv_drivers_commit}.tar.gz",
    f"https://github.com/lvgl/lvgl/archive/{_lvgl_commit}/lvgl-{_lvgl_commit}.tar.gz",
    f"https://gitlab.com/cherrypicker/squeek2lvgl/-/archive/{_squeek2lvgl_commit}/squeek2lvgl-{_squeek2lvgl_commit}.tar.gz",
]
source_paths = [
    ".",
    "lv_drivers",
    "lvgl",
    "squeek2lvgl",
]
sha256 = [
    "936cb01609defb26d8f57cd4893d7ad54d1b019e0e735f1e2aece2b8185a4eb8",
    "4605f6aa933049d21d06fc342674057bf97bc4ad343245de08317c7ff6d51289",
    "ccc38659c1fa64df5de84c3fe533afeef50a826dbcd1bdc960348767c0807286",
    "1c4ba6540ecb06eafabe920f1f9c2e95271382873b3f13189c27006527bfd5e7",
]
# FIXME: CFI crashes on launch https://gitlab.com/cherrypicker/buffyboard/-/issues/22
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_service(self.files_path / "buffyboard")


# CONFIGURE FIXME:
# WARNING: You should add the boolean check kwarg to the run_command call.
#          It currently defaults to false,
#          but it will default to true in future releases of meson.
#          See also: https://github.com/mesonbuild/meson/issues/9300

# BUILD FIXME:
# ../lvgl/src/core/lv_obj.c:345:25: warning: variable 'x' set but not used [-Wunused-but-set-variable]
#   345 |         static uint32_t x = 0;
#       |                         ^

# ../lv_drivers/indev/evdev.c:171:33: warning: add explicit braces to avoid dangling else [-Wdangling-else]
#   171 |                                 else if(in.value == 0)
#       |                                 ^

# RUNTIME FIXME:
# OSK cannot be seen until first press of an invisible key

# SERVICE TODO: https://github.com/void-linux/void-packages/pull/35876

# [ -e /dev/uinput ] || modprobe uinput || exit 1 (or is uinput automatically loaded somehow?)

# match current framebuffer rotation if no OPTS specified
# ROTATION=$(cat /sys/class/graphics/fbcon/rotate 2>/dev/null)
# OPTS="-r ${ROTATION:-0}"
