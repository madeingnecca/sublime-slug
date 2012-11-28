import sublime
import sublime_plugin
import slug


class SlugCommand(sublime_plugin.TextCommand):
    separator = '-'

    def run(self, edit):
        window = self.view.window()
        done = lambda(value): self.slug(edit, value)

        window.show_input_panel('Separator', self.separator, done, None, None)

    def slug(self, edit, value):
        view = self.view
        # Remember last separator used.
        self.separator = value

        for region in view.sel():
            val = view.substr(region).encode('utf-8')
            view.replace(edit, region, slug.slug(val, -1, self.separator))
