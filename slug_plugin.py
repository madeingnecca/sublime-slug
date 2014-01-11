import sublime_plugin
try:
    # This import method works in Sublime Text 2.
    import slug
except ImportError:
    # While this works in Sublime Text 3.
    from . import slug


class SlugCommand(sublime_plugin.TextCommand):
    separator = '-'

    def run(self, edit):
        def done(value):
            self.separator = value
            self.view.run_command('slug_replace', {'separator': self.separator})

        window = self.view.window()
        window.show_input_panel('Separator', self.separator, done, None, None)


class SlugReplaceCommand(sublime_plugin.TextCommand):
    def run(self, edit, separator):
        for region in self.view.sel():
            val = self.view.substr(region)
            self.view.replace(edit, region, slug.slug(val, -1, separator))
