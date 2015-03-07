import sublime, sublime_plugin

class new_file(sublime_plugin.TextCommand):
	def run(self, view):
		new_view = self.view.window().new_file()
		new_view.set_syntax_file("Packages/Tidea/Tidea.tmLanguage")
		# new_view.settings().set('default_encoding', 'UTF-16 LE with BOM')