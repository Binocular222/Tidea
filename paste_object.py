import sublime, sublime_plugin, subprocess, os, shutil, functools

class paste_object(sublime_plugin.TextCommand):
	def run(self, edit):
		source_path = sublime.get_clipboard()
		ObjPath, ObjBase = os.path.split(source_path)
		view = self.view.window().show_input_panel("Paste as:", ObjBase, self.on_done, None, None)

	def on_done(self, NewBaseName):
		cur_file = self.view.file_name()
		CurPath, CurBase = os.path.split(cur_file)
		old_source_path = sublime.get_clipboard()
		OldObjPath, OldObjBase = os.path.split(old_source_path)
		new_source_path = os.path.join(OldObjPath, NewBaseName)
		sublime.set_clipboard(new_source_path)
		os.rename(old_source_path, new_source_path)
		shutil.copy(new_source_path, CurPath)
		self.view.window().run_command("paste_simple", {"string": "[[" + NewBaseName + "]]"})
		self.window.run_command('hide_panel')
