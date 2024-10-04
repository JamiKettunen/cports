pkgname = "nodejs"
pkgver = "22.9.0"
pkgrel = 0
build_style = "configure"
configure_args = [
    "--ninja",
    "--openssl-use-def-ca-store",
    "--prefix=/usr",
    "--shared-brotli",
    "--shared-cares",
    "--shared-libuv",
    "--shared-nghttp2",
    "--shared-openssl",
    "--shared-zlib",
    "--with-intl=system-icu",
]
make_check_target = "test-only"
hostmakedepends = [
    "ninja",
    "pkgconf",
    "python",
    "python-jinja2",
]
makedepends = [
    "brotli-devel",
    "c-ares-devel",
    "icu-devel",
    "libuv-devel",
    "linux-headers",
    "nghttp2-devel",
    "openssl-devel",
    "zlib-ng-compat-devel",
]
checkdepends = ["procps"]
pkgdesc = "JavaScript runtime based on V8"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://nodejs.org"
source = f"{url}/dist/v{pkgver}/node-v{pkgver}.tar.gz"
sha256 = "296854aa1dca140b0462c2415637d0419e42af91114538a7e6fdf623971a6833"
debug_level = 1  # allow LTO build to not run out of mem
hardening = ["!vis", "!cfi"]
options = ["!cross"]

match self.profile().arch:
    case "ppc64le" | "ppc64" | "riscv64":
        # trap in add_label_offset() (assembler-ppc.cc)
        # also crashes on riscv64
        hardening += ["!int"]
    case "ppc":
        broken = "unsupported"


def post_extract(self):
    self.mv("deps/openssl/nodejs-openssl.cnf", ".")

    for f in [
        "deps/brotli",
        "deps/cares",
        "deps/openssl",
        "deps/zlib",
        "deps/v8/third_party/jinja2",
        "tools/inspector_protocol/jinja2",
    ]:
        self.rm(f, recursive=True)

    self.mkdir("deps/openssl")
    self.mv("nodejs-openssl.cnf", "deps/openssl")


def post_install(self):
    self.install_license("LICENSE")


# real test suite requires network acccess
def check(self):
    npath = self.chroot_cwd / "out/Release"
    nexe = npath / "node"
    self.do(nexe, "-e", "console.log('test')", wrksrc="out/Release")
    self.do(
        nexe,
        "-e",
        f"require('assert').equal(process.versions.node, '{pkgver}')",
        wrksrc="out/Release",
    )


@subpackage("nodejs-devel")
def _(self):
    return self.default_devel()
