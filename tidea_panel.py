import sublime, sublime_plugin

class tidea_panel(sublime_plugin.TextCommand):
    def run(self, edit):
        self.list_items = ["Toggle font"]
        syntax = self.view.settings().get('syntax')
        if syntax == 'Packages/Tidea/Tidea.tmLanguage':
            for item in ["Clear format", "Highlight", "Gray", "Orange", "Red", "Italic", "Bold", "Link"]: self.list_items.insert(0, item)
        self.list_items.insert(0, "Split View")

        sublime.active_window().show_quick_panel(self.list_items, self._on_select)

    def _on_select(self, idx):
        if idx > -1:
            selected = self.list_items[idx]
            if selected == "Toggle font":
                font = self.view.settings().get('font_face')
                if font == "CONSOLAS":
                    self.view.settings().set('font_face', "VERDANA")
                    sublime.status_message("VERDANA")
                else:
                    self.view.settings().set('font_face', "CONSOLAS")
                    sublime.status_message("CONSOLAS")
            elif selected == "Split View":
                current_view = self.view.window().active_view()
                self.view.window().run_command("clone_file")
                self.view.window().run_command("new_pane")
                self.view.window().focus_view(current_view)
                self.view.window().focus_group(1)
            elif selected == "Clear format": self.view.run_command("tidea_clear_format")
            else:
                self.view.run_command("tidea_format", {"args": self.list_items[idx]})

class tidea_format(sublime_plugin.TextCommand):
    def run(self, edit, args):
        Dict = {"Bold": "‎", "Italic": "‏", "Red": "​", "Orange": "‪", "Gray": "‬", "Highlight": "‭", "Link": " "}
        for sel in self.view.sel():
            if sel.end() != sel.begin():
                self.view.insert(edit, sel.end(), Dict[args])
                self.view.insert(edit, sel.begin(), Dict[args])

class tidea_clear_format(sublime_plugin.TextCommand):
    def run(self, edit):
        sublime.message_dialog('JumpTo')
        for sel in self.view.sel():
            content = self.view.substr(sel)
            content = content.replace('‭', '')  #Highlight
            content = content.replace('‬', '')  #Gray
            content = content.replace('‪', '')  #Orange
            content = content.replace('​', '')  #Red
            content = content.replace('‏', '')  #Italic
            content = content.replace('‎', '')  #Bold
            content = content.replace(' ', '') #Link
            self.view.replace(edit, sel, content)
