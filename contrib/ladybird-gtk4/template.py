pkgname = "ladybird-gtk4"
pkgver = "0_git20230926"
pkgrel = 0
# FIXME: holy crap the amount of vendoring
_commit = "f28d7925c20e19a354b3a3893a467510581ada4d"
_serenity_commit = "614ff9c46e91bd5aa4188c0a8aeb1f97404080f2"
_publicsuffix_list_commit = "4f5cba7853d1067a858ef27eb3368c00e4148480"
_cldr_version = "43.1.0"
_ucd_version = "15.1.0"
_cacert_version = "2023-05-30"
_commonmark_version = "0.30"
_tzdb_version = "2023c"
build_style = "cmake"
configure_args = [
    "-DSERENITY_SOURCE_DIR=serenity",
    f"-DSERENITY_CACHE_DIR=/builddir/{pkgname}-{pkgver}/caches",
    "-DENABLE_NETWORK_DOWNLOADS=OFF",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
    "glib-devel",
    "blueprint-compiler",
    "gettext",
    "libxml2-progs",
    "unicode-emoji",
]
makedepends = ["libadwaita-devel", "libsoup-devel", "libpulse-devel"]
pkgdesc = f"GTK 4 UI for the SerenityOS web browser (git {_commit[0:7]}, serenity {_serenity_commit[0:7]})"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "BSD-2-Clause"
url = "https://github.com/bugaevc/ladybird-gtk4"
source = [
    f"{url}/archive/{_commit}.tar.gz>ladybird-gtk4-{_commit}.tar.gz",
    f"https://github.com/SerenityOS/serenity/archive/{_serenity_commit}.tar.gz>serenity-{_serenity_commit}.tar.gz",
    f"https://github.com/unicode-org/cldr-json/releases/download/{_cldr_version}/cldr-{_cldr_version}-json-modern.zip",
    f"https://www.unicode.org/Public/{_ucd_version}/ucd/UCD.zip",
    f"!https://www.unicode.org/Public/emoji/{_ucd_version[:_ucd_version.rfind('.')]}/emoji-test.txt",
    f"!https://raw.githubusercontent.com/publicsuffix/list/{_publicsuffix_list_commit}/public_suffix_list.dat",
    f"!https://curl.se/ca/cacert-{_cacert_version}.pem",
    f"!https://spec.commonmark.org/{_commonmark_version}/spec.json",
    f"https://data.iana.org/time-zones/releases/tzdata{_tzdb_version}.tar.gz",
]
source_paths = [
    ".",
    "serenity",
    "caches/CLDR",
    "caches/UCD",
    "", # caches/UCD
    "", # caches/PublicSuffix
    "", # caches/CACERT
    "", # caches/commonmark.spec.json
    "caches/TZDB",
]
sha256 = [
    "3d57243e98042d7a1a6910277d18d63c0535a7704be456f24b7384f59a10a908",
    "3c0b3e93a9f8e351a47ef7ec69ecab5405d70c2121b8821b93b419e1e5c58a45",
    "5b770d59f052f19573d5e0783b6581269f6c86a193cc6e84ebd0796e143153cd",
    "cb1c663d053926500cd501229736045752713a066bd75802098598b7a7056177",
    "d876ee249aa28eaa76cfa6dfaa702847a8d13b062aa488d465d0395ee8137ed9",
    "faae37f3ecff7d919e2b8e50c5c9be734ce66873df916a679686c5c31ff0065f",
    "5fadcae90aa4ae041150f8e2d26c37d980522cdb49f923fc1e1b5eb8d74e71ad",
    "ae6129f3ce3caf4f99cf4f9a5ad3558a309652b5b887171013e2bf0797289b98",
    "3f510b5d1b4ae9bb38e485aa302a776b317fb3637bdb6404c4adf7b6cadd965c",
]
# serenity lagom FTBFS with: Could not find incbin file 'LibCompress/BrotliDictionaryData.bin'
# -> TODO: https://github.com/SerenityOS/serenity/issues/new
options = ["!lto"]


def post_extract(self):
    self.mkdir("caches/PublicSuffix")
    self.mkdir("caches/CACERT")
    self.cp(self.sources_path / "emoji-test.txt", "caches/UCD")
    self.cp(self.sources_path / "public_suffix_list.dat", "caches/PublicSuffix")
    self.cp(self.sources_path / f"cacert-{_cacert_version}.pem", "caches/CACERT")
    self.cp(self.sources_path / "spec.json", "caches/commonmark.spec.json")
    self.do("sh", "-c", f"printf '%s' {_cldr_version} > caches/CLDR/version.txt")
    self.do("sh", "-c", f"printf '%s' {_ucd_version} > caches/UCD/version.txt")
    self.do("sh", "-c", f"printf '%s' {_cacert_version} > caches/CACERT/version.txt")
    self.do("sh", "-c", f"printf '%s' {_tzdb_version} > caches/TZDB/version.txt")


def post_install(self):
    self.install_license("LICENSE")


# FIXME: .desktop file not launching from gnome but "gio launch" does???
