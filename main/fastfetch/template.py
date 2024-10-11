pkgname = "fastfetch"
pkgver = "2.28.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_TESTS=ON", "-DENABLE_SYSTEM_YYJSON=ON"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    #"chafa-devel", # armv7 FIXME harfbuzz
    "dbus-devel",
    #"dconf-devel", # armv7 FIXME glib meson.build:2607:2: ERROR: Problem encountered: Running binaries on the build host needs to be supported to build with -Dintrospection=enabled
    #"ddcutil-devel", # armv7 FIXME -> glib
    "elfutils-devel",
    #"libmagick-devel", # armv7 FIXME !cross
    #"libpulse-devel",  # armv7 FIXME -> glib
    "libxrandr-devel",
    "ocl-icd-devel",
    "vulkan-headers",
    #"vulkan-loader-devel", # armv7 FIXME !cross
    "wayland-devel",
    #"xfconf-devel", # armv7 FIXME !cross
    "yyjson-devel",
    "zlib-ng-compat-devel",
    "linux-headers",
]
depends = ["lscpu"]
pkgdesc = "Neofetch-like system information fetching tool"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "MIT"
url = "https://github.com/fastfetch-cli/fastfetch"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "115d9947ee0acf6246894888998db31de024f651123396c6251033390c241dc7"
tool_flags = {"CFLAGS": ["-DNDEBUG"]}
# CFI: dies immediately (ffPlatformPathAddHome at FFlist.c:31:12)
hardening = ["vis", "!cfi"]
