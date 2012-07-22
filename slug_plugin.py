import sublime
import sublime_plugin
import slug


class SlugCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        for region in view.sel():
            val = view.substr(region).encode('utf-8')
            view.replace(edit, region, slug.slug(val, '_'))
