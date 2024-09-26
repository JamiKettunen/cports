pkgname = "libhybris"
pkgver = "0.1.0_git20240901"
pkgrel = 0
_commit = "936279916605003fba95a0f3629a6bc5e6caa343"
_branch = "master"
# https://developer.android.com/ndk/guides/abis#sa
archs = ["aarch64", "x86_64", "armv7"]
build_wrksrc = "hybris"
build_style = "gnu_configure"
configure_args = [
    "--enable-experimental",
    "--enable-wayland",
    "--enable-property-cache",
    #"--enable-mesa",
    # bringup etc, TODO: drop later?
    "--enable-debug",
    "--enable-trace",
    "--enable-stub-linker",
]
hostmakedepends = ["automake", "slibtool", "pkgconf", "wayland-progs"]
makedepends = [
    "wayland-devel",
    "android-headers",
    #"vulkan-headers",  # FIXME: needs ifunc...
    "linux-headers",
    "musl-bsd-headers",
    "libx11-devel",
]
pkgdesc = "Support and interface with Android bionic vendor hw drivers"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "Apache-2.0"
url = "https://github.com/libhybris/libhybris"
source = f"https://github.com/libhybris/libhybris/archive/{_commit}.tar.gz"
sha256 = "fac6af6bdde7a7b079eb74fdd27d1d0ac1cc814a0e32a1d06fd4152617018225"
tool_flags = {
    # FIXME: lfs64 removal transition (allows dropping musl-bsd-headers too?), mandatory in the near future
    # FIXME: non-pod-varargs https://paste.c-net.org/xdkwvbbvsczl
    # FIXME: int-conversion https://paste.c-net.org/enrfkfjw53zv
    # TODO: ~940 string-plus-int warnings https://paste.c-net.org/h4o80sk1ootf
    # TODO: 26 -Wmacro-redefined, 3 -Wbuiltin-macro-redefined, 3 -Wparentheses-equality
    "CFLAGS": [
        "-D_LARGEFILE64_SOURCE",
        "-Wno-error=int-conversion",
        "-Wno-string-plus-int",
        # TODO OpenCL:
        # - 2 deprecated-declarations test_opencl.c since 1.2 clCreateCommandQueue/clEnqueueTask
        # - 2 #pragma-messages opencl.c/test_opencl.c (cl_version.h) CL_TARGET_OPENCL_VERSION undefined default to 3.0 (300)
        "-Wno-deprecated-declarations",
        # FIXME: configure: error: C compiler cannot create executables
        #"-Wno-#pragma-messages",
    ],
    "CXXFLAGS": [
        "-D_LARGEFILE64_SOURCE",
        "-Wno-error=non-pod-varargs",
        "-Wno-error=int-conversion",
        "-Wno-string-plus-int",
        # TODO: ~60 format warnings https://paste.c-net.org/cmwoybor7ftc (unsigned long long/void* -> unsigned long/Elf64_Addr)
        "-Wno-format",
        # TODO: 38 old-style-cast warnings from musl_compat.h TEMP_FAILURE_RETRY (used in C++ code)
        "-Wno-old-style-cast",
        # idc about spamming __UNUSED in places (yet) to fix 16 of these
        "-Wunused-value",
        "-Wunused-result",
    ],
}

_arch = self.profile().arch
match _arch:
    case "aarch64" | "armv7":
        configure_args += [
            f"--enable-arch={"arm64" if _arch == "aarch64" else "arm"}",
            "--enable-mali-quirks",
            "--enable-adreno-quirks",
        ]
    case "x86_64":
        configure_args += ["--enable-arch=x86-64"]
    case _:
        self.error(f"unknown architecture {_arch}")

# name | api (| lib = name)( | provides = name)
_pkgs = [
    ("libegl", "EGL", "libEGL"),
    ("libgles1", "OpenGL ES 1.x", "libGLESv1_CM"),
    ("libgles2", "OpenGL ES 2.x", "libGLESv2"),
    ("libopencl", "OpenCL", "libOpenCL"),
    #("libvulkan", "Vulkan"),  # FIXME
]


def post_install(self):
    # move these into a subdir where they won't conflict with the mesa EGL/GLES libs
    # etc so we can also e.g. opt for software rendering via llvmpipe if desired
    d = self.destdir / "usr/lib/hybris"
    self.mkdir(d)
    self.mv(self.destdir / "usr/lib/libEGL.so.*", d, glob=True)
    self.mv(self.destdir / "usr/lib/libGLESv1_CM.so.*", d, glob=True)
    self.mv(self.destdir / "usr/lib/libGLESv2.so.*", d, glob=True)
    #self.mv(self.destdir / "usr/lib/libvulkan.so.*", d, glob=True)  # FIXME
    self.mv(self.destdir / "usr/lib/libOpenCL.so.*", d, glob=True)

    # really not fond of this but it's the only way if we want musl to load the
    # Android GPU drivers via libhybris by default without replacing mesa
    # lib*gl* libs or specifying LD_LIBRARY_PATH globally while leaving
    # software rendering just a LD_LIBRARY_PATH=/usr/lib away
    self.mkdir(self.destdir / "etc")
    _arch = self.profile().arch.replace("armv7", "armhf")
    with open(self.destdir / f"etc/ld-musl-{_arch}.path", "w") as outf:
        outf.write("/usr/local/lib:/usr/lib/hybris:/usr/lib\n")

    # drop junk conflicting with mesa-devel, vulkan-loader-devel & ocl-icd-devel/opencl-headers
    self.uninstall("usr/include/EGL")
    self.uninstall("usr/include/GLES")
    self.uninstall("usr/include/GLES2")
    self.uninstall("usr/include/GLES3")
    self.uninstall("usr/include/KHR")
    self.uninstall("usr/lib/libEGL.so")
    self.uninstall("usr/lib/libGLESv1_CM.so")
    self.uninstall("usr/lib/libGLESv2.so")
    self.uninstall("usr/lib/pkgconfig/egl.pc")
    self.uninstall("usr/lib/pkgconfig/glesv1_cm.pc")
    self.uninstall("usr/lib/pkgconfig/glesv2.pc")
    #self.uninstall("usr/lib/libvulkan.so")  # FIXME
    self.uninstall("usr/include/CL")
    self.uninstall("usr/lib/libOpenCL.so")
    self.uninstall("usr/lib/pkgconfig/OpenCL.pc")


@subpackage("libhybris-progs")
def _(self):
    self.subdesc = "setprop and getprop programs"
    return ["cmd:*prop"]


@subpackage("libhybris-test-progs")
def _(self):
    self.subdesc = "potentially broken test programs"
    return ["cmd:test_*"]


@subpackage("libhybris-devel")
def _(self):
    return self.default_devel()


def _gen_pkg(name, api, lib="", provides=""):
    @subpackage(f"{name}-hybris")
    def _(self):
        self.pkgdesc = "libhybris implementation of the {api} API"
        self.subdesc = "runtime library"
        # NOTE: no provides/replaces to work alongside Mesa libraries which can be used for e.g.
        # troubleshooting via LD_LIBRARY_PATH=/usr/lib
        self.options = ["!scanshlibs"]
        #self.provides = [provides if provides else name]

        return [f"usr/lib/hybris/{lib if lib else name}.so.*"]


# generate subpackages
for _tup in _pkgs:
    _gen_pkg(*_tup)
