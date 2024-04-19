pkgname = "protobuf"
pkgver = "27.0_rc1"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=ON",
    "-Dprotobuf_USE_EXTERNAL_GTEST=ON",
    "-Dprotobuf_ABSL_PROVIDER=package",
]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["zlib-devel", "gtest-devel", "abseil-cpp-devel"]
pkgdesc = "Protocol buffers library"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "BSD-3-Clause"
url = "https://protobuf.dev"
source = f"https://github.com/protocolbuffers/protobuf/archive/v{pkgver.replace('_', '-')}.tar.gz"
sha256 = "ee79528aa438d1d65c98f6d0a7bbcf62f3dd1f3411c170118a5668b432040887"
# FIXME cfi entirely breaks protoc (even just --help or --version SIGILL)
hardening = ["vis", "!cfi"]

if self.profile().cross:
    hostmakedepends += ["protoc"]  # needs host protoc
    broken = "generated protobuf-targets.cmake looks for protoc in target sysroot, cannot cross-build android-tools etc"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("protobuf-lite")
def _lite(self):
    self.pkgdesc = f"{pkgdesc} (lite version)"

    return ["usr/lib/libprotobuf-lite.so.*"]


@subpackage("protoc")
def _protoc(self):
    self.pkgdesc = "Protocol buffers compiler and its library"

    return [
        "usr/bin",
        "usr/lib/libprotoc.so.*",
    ]


@subpackage("protobuf-devel")
def _devel(self):
    return self.default_devel()
