import sublime, sublime_plugin

class OnLoad(sublime_plugin.EventListener):
    def on_load(self, view):
        Synt = view.settings().get('syntax')
        if Synt == 'Packages/Tidea/Tidea.tmLanguage':
            view.run_command("fold_by_level", {"level": 3})
