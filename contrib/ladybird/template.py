pkgname = "ladybird"
pkgver = "0.0.1_git20240604"
pkgrel = 0
build_wrksrc = "Ladybird"
build_style = "cmake"
hostmakedepends = ["cmake", "ninja"]
makedepends = ["qt6-qtmultimedia-devel", "libpulse-devel"]
pkgdesc = "SerenityOS web browser Qt6 chrome"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "BSD-2-Clause"
url = "https://ladybird.dev"
_commit = "0ab4722cee11d27da79bb05c1d53693f39938cf6"
# TODO: any possibility to avoid all the vendoring?
_ucd = "15.1.0"  # Meta/CMake/unicode_data.cmake:3
_tzdb = "2024a"  # Meta/CMake/time_zone_data.cmake:3
_cldr = "45.0.0"  # Meta/CMake/locale_data.cmake:3
_cacert = "2023-12-12"  # Meta/CMake/ca_certificates_data.cmake:3
_publicsuffix_list = (
    # Meta/CMake/public_suffix.cmake:6, tip of https://github.com/publicsuffix/list/commits/master :/
    "903a83ff7bfc3148e3692e09396f9f3bdc9462ef"
)
_commonmark_spec = "0.30"  # Meta/CMake/commonmark_spec.cmake:4
# TODO: avoid checksumming adobe icc due to no versioning?!
source = [
    f"https://github.com/LadybirdWebBrowser/ladybird/archive/{_commit}.tar.gz",
    f"https://www.unicode.org/Public/{_ucd}/ucd/UCD.zip",
    f"!https://www.unicode.org/Public/emoji/{_ucd[:_ucd.rfind('.')]}/emoji-test.txt",
    f"!https://www.unicode.org/Public/idna/{_ucd}/IdnaMappingTable.txt",
    f"https://data.iana.org/time-zones/releases/tzdata{_tzdb}.tar.gz",
    f"https://github.com/unicode-org/cldr-json/releases/download/{_cldr}/cldr-{_cldr}-json-modern.zip",
    "https://download.adobe.com/pub/adobe/iccprofiles/win/AdobeICCProfilesCS4Win_end-user.zip",
    f"!https://curl.se/ca/cacert-{_cacert}.pem",
    f"!https://raw.githubusercontent.com/publicsuffix/list/{_publicsuffix_list}/public_suffix_list.dat",
    f"!https://spec.commonmark.org/{_commonmark_spec}/spec.json",
]
source_paths = [
    ".",
    "caches/UCD",
    None,  # caches/UCD/emoji-test.txt
    None,  # caches/UCD/IdnaMappingTable.txt
    "caches/TZDB",
    "caches/CLDR",
    "caches/AdobeICCProfiles/Adobe ICC Profiles (end-user)",
    None,  # caches/CACERT/cacert-{_cacert}.pem
    None,  # caches/PublicSuffix/public_suffix_list.dat
    None,  # caches/commonmark.spec.json
]
sha256 = [
    "0492c6b2d2accc15fad839e5b4f96927524fa546118f4491b62aaa9daf46d9c4",
    "cb1c663d053926500cd501229736045752713a066bd75802098598b7a7056177",
    "d876ee249aa28eaa76cfa6dfaa702847a8d13b062aa488d465d0395ee8137ed9",
    "402cbd285f1f952fcd0834b63541d54f69d3d8f1b8f8599bf71a1a14935f82c4",
    "0d0434459acbd2059a7a8da1f3304a84a86591f6ed69c6248fffa502b6edffe3",
    "ba934cdd40ad4fb6439004c7e746bef97fe2b597db1040fcaa6c7d0647742c1b",
    "92043b7c3ca5a25a0f6975d0cdc57db60a67dcb9ebdfb15b16267311beb58f94",
    "ccbdfc2fe1a0d7bbbb9cc15710271acf1bb1afe4c8f1725fe95c4c7733fcbe5a",
    "3437b41cd4007b419f40ddf2fb30ec69ca9c33c60360112bd85fe89a389fedff",
    "ae6129f3ce3caf4f99cf4f9a5ad3558a309652b5b887171013e2bf0797289b98",
]
# FIXME:
# - !lto: lagom FTBFS with error: Could not find incbin file 'Userland/Libraries/LibCompress/BrotliDictionary.cpp.dict.bin'
#   -> https://github.com/SerenityOS/serenity/issues/new
# - !check: none of the 199 test binaries are built?
options = ["!lto", "!check"]


def init_configure(self):
    self.configure_args = [
        "-DENABLE_NETWORK_DOWNLOADS=OFF",
        f"-DSERENITY_CACHE_DIR={self.chroot_builddir}/{self.wrksrc}/caches",
    ]


def post_extract(self):
    self.mkdir("caches/CACERT")
    self.mkdir("caches/PublicSuffix")
    self.cp(self.sources_path / "emoji-test.txt", "caches/UCD")
    self.cp(self.sources_path / "IdnaMappingTable.txt", "caches/UCD")
    self.cp(self.sources_path / f"cacert-{_cacert}.pem", "caches/CACERT")
    self.cp(self.sources_path / "public_suffix_list.dat", "caches/PublicSuffix")
    self.cp(self.sources_path / "spec.json", "caches/commonmark.spec.json")
    self.do("sh", "-c", f"printf '%s' {_ucd} > caches/UCD/version.txt")
    self.do("sh", "-c", f"printf '%s' {_tzdb} > caches/TZDB/version.txt")
    self.do("sh", "-c", f"printf '%s' {_cldr} > caches/CLDR/version.txt")
    self.do("sh", "-c", f"printf '%s' {_cacert} > caches/CACERT/version.txt")


def post_install(self):
    self.install_license("../LICENSE")
    # TODO: install empty /usr/local/share/fonts to at least silence FontDatabase::load_all_fonts_from_uri() log spam


@subpackage("ladybird-devel")
def _devel(self):
    return self.default_devel(extra=["usr/share/Ladybird/*.cmake"])


# FIXME: "WebContent process crashed" on any site (RequestServer segfaults in libc.so)
# -> works when launched with "Ladybird --enable-qt-networking ..."

# TODO: add .desktop file (only Ladybird bin exists atm)
