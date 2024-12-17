from cbuild.util import linux


def configure(self):
    linux.configure(self, self.kernel_flavor)


def build(self):
    linux.build(self, self.kernel_flavor)


def install(self):
    linux.install(self, self.kernel_flavor)


def use(tmpl):
    tmpl.configure = configure
    tmpl.build = build
    tmpl.install = install

    tmpl.build_style_defaults = [
        ("make_dir", "build"),
    ]

    if not tmpl.kernel_flavor:
        tmpl.kernel_flavor = tmpl.pkgname.removeprefix("linux-")

    # if tmpl.profile().cross:
    #     tmpl.broken = "linux-devel does not come out right"

    # TODO: move -dbg @subpackage creation here?


@custom_target("generate-configs", "patch")
def _(self):
    linux.update_configs(
        self, self.archs, self.kernel_flavor, self.kernel_configs
    )


@custom_target("menuconfig", "patch")
def _(self):
    linux.update_configs(self, self.archs, self.kernel_flavor, "menuconfig")
