pkgname = "wrapland"
pkgver = "0.601.0"
pkgrel = 0
build_style = "cmake"
make_check_args = [
    "-E",
    "wrapland-(testConnectionThread"  # socket name wayland-2 vs wayland-0
    + "|testSeat"  # segfault in testKeyboard()
    + "|testDataDevice"  # segfault in test_send_selection_on_seat()
    + "|test-data-control"  # segfault in test_set_selection()
    + "|test-external-sources"  # segfault in test_selection()
    + "|testPrimarySelection"  # segfault in testSendSelectionOnSeat()
    + "|test-text-input-v2"  # segfault in test_show_hide_panel()
    + "|test-text-input-v3"  # segfault in test_cursor_rectangle()
    + "|test-text-input-method-sync"  # segfault in test_sync_text_input()
    + "|testSelection"  # segfault in testClearOnEnter()
    + ")",
    # parallel tests cause a bunch of flakes
    "-j1",
]
make_check_wrapper = ["xwfb-run", "--"] # dbus-run-session
hostmakedepends = [
    "cmake",
    "ninja",
    "extra-cmake-modules",
    "pkgconf",
    "wayland-progs",
]
makedepends = [
    "qt6-qtbase-devel",
    "wayland-devel",
    "wayland-protocols",
    "microsoft-gsl",
]
# TODO: is weston needed? what about dbus?
checkdepends = ["weston", "xwayland-run"]
# depends = ["kirigami"]
pkgdesc = "Qt/C++ library wrapping libwayland"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-or-later"
url = "https://github.com/winft/wrapland"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "46b39f09c3fb8f3effb21955d75f26ea6f79d50f516f7116453c3bc4a3a5eb8b"


@subpackage("wrapland-devel")
def _devel(self):
    self.depends += ["microsoft-gsl"]

    return self.default_devel()
