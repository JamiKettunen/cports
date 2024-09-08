# mirrors the gtk3 webkitgtk template
pkgname = "webkitgtk4"
pkgver = "2.45.92"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DPORT=GTK",
    "-DCMAKE_SKIP_RPATH=ON",
    f"-DCMAKE_LINKER={self.profile().triplet}-clang",
    # -DUSE_*
    "-DUSE_GTK4=ON",
    "-DUSE_LD_LLD=ON",
    "-DUSE_LIBBACKTRACE=OFF",
    "-DUSE_SOUP2=OFF",
    "-DUSE_WOFF2=ON",
    "-DUSE_SYSTEM_SYSPROF_CAPTURE=NO",
    # -DENABLE_*
    "-DENABLE_BUBBLEWRAP_SANDBOX=ON",
    "-DENABLE_DOCUMENTATION=OFF",
    "-DENABLE_INTROSPECTION=ON",
    "-DENABLE_JOURNALD_LOG=OFF",
    "-DENABLE_MINIBROWSER=ON",
    "-DENABLE_SAMPLING_PROFILER=OFF",  # unavailable on musl
    "-DENABLE_WAYLAND_TARGET=ON",
    # conflicts with the gtk3 one
    "-DENABLE_WEBDRIVER=OFF",
    "-DENABLE_X11_TARGET=ON",
]
hostmakedepends = [
    "bubblewrap",
    "cmake",
    "flex",
    "geoclue",
    "gettext",
    "glib-devel",
    "gobject-introspection",
    "gperf",
    "ninja",
    "perl",
    "pkgconf",
    "python",
    "ruby",
    "unifdef",
    "wayland-progs",
    "xdg-dbus-proxy",
]
makedepends = [
    "at-spi2-core-devel",
    "enchant-devel",
    "freetype-devel",
    "geoclue-devel",
    "gst-plugins-bad-devel",
    "gst-plugins-base-devel",
    "gstreamer-devel",
    "gtk4-devel",
    "harfbuzz-devel",
    "hyphen-devel",
    "icu-devel",
    "icu-devel",
    "lcms2-devel",
    "libavif-devel",
    "libepoxy-devel",
    "libgcrypt-devel",
    "libjpeg-turbo-devel",
    "libjxl-devel",
    "libmanette-devel",
    "libnotify-devel",
    "libpng-devel",
    "libpsl-devel",
    "libseccomp-devel",
    "libsecret-devel",
    "libsoup-devel",
    "libtasn1-devel",
    "libwebp-devel",
    "libwpe-devel",
    "libxcomposite-devel",
    "libxdamage-devel",
    "libxkbcommon-devel",
    "libxml2-devel",
    "libxslt-devel",
    "libxt-devel",
    "mesa-devel",
    "openjpeg-devel",
    "sqlite-devel",
    "wayland-devel",
    "wayland-protocols",
    "woff2-devel",
    "wpebackend-fdo-devel",
]
depends = [
    "bubblewrap",
    "gst-plugins-bad",
    "gst-plugins-good",
    "xdg-dbus-proxy",
]
pkgdesc = "GTK4 port of the WebKit browser engine"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later AND BSD-2-Clause"
url = "https://webkitgtk.org"
source = f"{url}/releases/webkitgtk-{pkgver}.tar.xz"
sha256 = "753f6c638c72633f22305a606dbd6c825b8fde3a7d01184a8f18f740493ca79f"
debug_level = 1  # otherwise LTO link runs out of memory + fat debuginfo
tool_flags = {
    "CFLAGS": ["-DNDEBUG"],
    "CXXFLAGS": [
        # also silence some really loud warnings...
        "-DNDEBUG",
        "-Wno-deprecated-declarations",
        "-Wno-deprecated-copy",
    ],
}
env = {
    # WebKitCCache.cmake
    "CCACHE_SLOPPINESS": "time_macros,include_file_mtime"
}
# FIXME: crashes in libpas (seems compiler-generated, not code bugs)
hardening = ["!int"]
# huge testsuite
options = ["!check"]

match self.profile().arch:
    case "x86_64" | "aarch64":
        configure_args += ["-DENABLE_JIT=ON", "-DENABLE_C_LOOP=OFF"]
    case _:
        configure_args += [
            "-DENABLE_JIT=OFF",
            "-DENABLE_C_LOOP=ON",
            "-DENABLE_WEBASSEMBLY=OFF",
        ]

# LTO broken on aarch64 (JIT segfault) and on riscv64 (broken in LLVM)
match self.profile().arch:
    case "aarch64" | "riscv64":
        options += ["!lto"]
    case _:
        configure_args += ["-DLTO_MODE=thin"]


def post_install(self):
    self.install_license("Source/WebCore/LICENSE-APPLE")
    self.install_license("Source/WebCore/LICENSE-LGPL-2.1")
    self.install_license("Source/WebCore/LICENSE-LGPL-2")


@subpackage("webkitgtk4-devel")
def _(self):
    return self.default_devel()
