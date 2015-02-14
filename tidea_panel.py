import sublime, sublime_plugin, os, functools, subprocess

class tidea_panel(sublime_plugin.TextCommand):
	def run(self, edit):
		#Get plain string from clipboard
		ahk_exe = sublime.packages_path() + "\\User\\" + "AHK.exe"
		ahk_ahk = sublime.packages_path() + "\\User\\" + "AHK.ahk"
		command = "clipboard = %clipboard%"
		subprocess.Popen([ahk_exe, ahk_ahk, command])

		CursorLocation = self.view.sel()[0]
		ScopeName = self.view.scope_name(CursorLocation.a)
		self.list_items = ["DejaVu Sans Mono", "Consolas", "Arial Unicode MS", "Tahoma"]
		syntax = self.view.settings().get('syntax')
		if syntax == 'Packages/Tidea/Tidea.tmLanguage':
			for item in ["Clear format", "Highlight", "Gray", "Orange", "Red", "Italic", "Bold", "Link"]: self.list_items.insert(0, item)
		if os.path.exists(sublime.get_clipboard()):
			self.list_items.insert(0, "Paste object")
		elif "link.internal" in ScopeName:
			self.list_items.insert(0, "Rename object")
		self.list_items.insert(0, "Split View")

		sublime.active_window().show_quick_panel(self.list_items, self._on_select)

	def _on_select(self, idx):
		if idx > -1:
			selected = self.list_items[idx]
			# if selected == "Toggle font":
			#     font = self.view.settings().get('font_face')
			#     if font == "DejaVu Sans Mono":
			#         self.view.settings().set('font_face', "Arial Unicode MS")
			#         sublime.status_message("Arial Unicode MS")
			#     else:
			#         self.view.settings().set('font_face', "DejaVu Sans Mono")
			#         sublime.status_message("DejaVu Sans Mono")
			if selected == "DejaVu Sans Mono": self.view.settings().set('font_face', "DejaVu Sans Mono")
			elif selected == "Arial Unicode MS": self.view.settings().set('font_face', "Arial Unicode MS")
			elif selected == "Consolas": self.view.settings().set('font_face', "Consolas")
			elif selected == "Tahoma": self.view.settings().set('font_face', "Tahoma")
			elif selected == "Split View":
				current_view = self.view.window().active_view()
				self.view.window().run_command("clone_file")
				self.view.window().run_command("new_pane")
				self.view.window().focus_view(current_view)
				self.view.window().focus_group(1)
			elif selected == "Clear format": self.view.run_command("tidea_clear_format")
			elif selected == "Paste object": self.view.run_command("paste_object")
			elif selected == "Rename object":
				CursorLocation = self.view.sel()[0]
				ScopeText = self.view.substr(self.view.extract_scope(CursorLocation.a)).replace("*", "")
				slash = "\\" if sublime.platform() == "windows" else "/"
				RawText = os.path.expandvars(ScopeText.lstrip('[[').rstrip(']]').strip(' '))
				full_path = RawText.rsplit('#')[0]
				if os.path.exists(full_path) == 0: full_path = os.path.split(self.view.file_name())[0]+slash+full_path
				if os.path.exists(full_path) == 0:
					sublime.message_dialog('File not exist')
				else:
					Path, BaseName = os.path.split(full_path)
					# sublime.message_dialog(full_path)
					view = self.view.window().show_input_panel("New Name:", BaseName, functools.partial(self.rename_file, full_path, Path), None, None)
			else:
				self.view.run_command("tidea_format", {"args": self.list_items[idx]})

	def rename_file(self, old, Path, NewBaseName):
		self.view.window().run_command('hide_panel')
		new_name_path = os.path.join(Path, NewBaseName)
		os.rename(old, new_name_path)
		sublime.set_clipboard(NewBaseName)

class tidea_format(sublime_plugin.TextCommand):
	def run(self, edit, args):
		Dict = {"Bold": "‎", "Italic": "‏", "Red": "​", "Orange": "‪", "Gray": "‬", "Highlight": "‭", "Link": " "}
		for sel in self.view.sel():
			if sel.end() != sel.begin():
				self.view.insert(edit, sel.end(), Dict[args])
				self.view.insert(edit, sel.begin(), Dict[args])

class tidea_clear_format(sublime_plugin.TextCommand):
	def run(self, edit):
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
