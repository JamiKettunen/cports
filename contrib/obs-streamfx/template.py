pkgname = "obs-streamfx"
pkgver = "0.12.0b366"
pkgrel = 0
_cmake_version_gitrev = "3bef96bafab04161991c2cd98a1ed51f6362d670" # 1.4.1
build_style = "cmake"
# FIXME: "-DCOMPONENT_NVIDIA=OFF" should make nvidia stuff optional without any patches,
#        it even defaults to off on non-windows anyway
configure_args = [f"-DVERSION={pkgver}", "-DSTRUCTURE_PACKAGEMANAGER=ON"]
hostmakedepends = ["cmake", "ninja"]
makedepends = [
    "obs-studio-devel",
    "qt6-qtbase-devel",
    "libcurl-devel",
    "ffmpeg-devel",
    "nlohmann-json",
]
pkgdesc = "OBS plugin adds many new effects and lots more"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-only"
url = "https://github.com/Xaymar/obs-StreamFX"
source = [
    f"https://github.com/Xaymar/obs-StreamFX/archive/{pkgver}.tar.gz",
    f"https://github.com/Xaymar/cmake-version/archive/{_cmake_version_gitrev}.tar.gz",
]
source_paths = [
    ".",
    "cmake/version",
]
sha256 = [
    "db96d26770884ea0770f5932c6700a39eeb6776436db8961c144dffab4234b31",
    "802bf11a46b4645a231a85b2ca3ca77a5d1df111f9063dc81c1189f02d7f8407",
]
# FIXME: CFI fails in gladLoadGLUserPtr()'s glad_glGetString assignment in third-party/khronos/glad/src/gl.c
hardening = ["vis", "!cfi"]


#def post_install(self):
#    self.install_doc("README.md")


# TODO: custom -locale subpkg extra usr/share/obs/obs-plugins/StreamFX/locale?


# TODO:
# 1. ability to set version from cmake configure args, 0.12.0b366 tarball + cmake/version FTBFS due to invalid "0.0.0-" version and "error: duplicate case value" in components/mirror/source/sources/source-mirror.cpp:119
# -> see fix-version-FTBFS.patch
# 2. default to STRUCTURE_PACKAGEMANAGER to ON for linux builds, defaults to non-sense /usr/local/plugins location otherwise even when building outside packaging
# 3. NVIDIA stuff shouldn't be mandatory without patches, only working on windows anyway atm
# 4. optional third-party/nlohmann-json if found system-provided json-c++ headers
# 5. building without cmake/version at all?
# 6. drop first launch update check consent dialog for -DSTRUCTURE_PACKAGEMANAGER=ON builds
# -> see no-updater.patch
# 7. fix memory leak shown when exiting OBS with StreamFX installed:
# info: Number of memory leaks: 1
