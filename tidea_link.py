import sublime, sublime_plugin, os, re, subprocess, webbrowser

class tidea_link(sublime_plugin.TextCommand):
	def run(self, edit):
		CurBase = os.path.basename(self.view.file_name())
		CurPath = os.path.split(self.view.file_name())[0]
		ParentPath = os.path.split(CurPath)[0]
		window = self.view.window()
		slash = "\\" if sublime.platform() == "windows" else "/"
		CursorLocation = self.view.sel()[0].a
		ScopeName = self.view.scope_name(CursorLocation)
		if "link." not in ScopeName and "text.Tidea Alternatives" not in self.view.scope_name(self.view.sel()[0].a - 1):
			CursorLocation = self.view.sel()[0].a - 1
			ScopeName = self.view.scope_name(CursorLocation)
		ScopeText = self.view.substr(self.view.extract_scope(CursorLocation))

		if "link.external" in ScopeName:
			if "http:" not in ScopeText and "ftp:" not in ScopeText and "https:" not in ScopeText:
				ScopeText = 'http://' + ScopeText
			window.run_command('open_url', {"url": ScopeText})
			# webbrowser.open(ScopeText, autoraise=True)
		elif "link.email" in ScopeName:
			window.run_command('open_url', {"url": "mailto:"+ScopeText})
		elif "link.internal" in ScopeName:
			JumpTo = ""
			RawText = os.path.expandvars(ScopeText.lstrip('[[').rstrip(']]').strip(' '))
			if '#' in RawText:
				JumpTo = RawText.rsplit('#')[1]
				Path = RawText.rsplit('#')[0]
			else: Path = RawText

			if Path != '' and os.path.isdir(Path) == 1:			#Absolute path lead to a folder, then do nothing
				Path = Path
			elif Path != '' and os.path.isfile(Path) == 0:		#Relative path
				temp = CurPath+slash+Path
				if os.path.isdir(temp) == 1:					#Relative path lead to a folder
					Path = temp+slash+Path
				elif os.path.isfile(temp) == 1:					#Relative path lead to a file
					Path = CurPath+slash+Path
				elif os.path.basename(CurPath) == CurBase:		#Current file is nested inside a folder with same name
					temp = ParentPath+slash+Path
					if os.path.isdir(temp) == 1:				#Relative path lead to a folder
						Path = temp+slash+Path
					elif os.path.isfile(temp) == 1:				#Relative path lead to a file
						Path = ParentPath+slash+Path

			if os.path.exists(Path) == 0:						#Totally failed to located target file,
				Path = ""
				JumpTo = RawText

			if JumpTo != "":									#Jump to inside current file
				self.view.window().run_command("expand_selection", {"to": "scope"})
				if ' ' in ScopeText:    #Thin space U+2009
					begin = self.view.sel()[0].begin() + 1
					b = self.view.sel()[0].end() - 1
				else:
					begin = self.view.sel()[0].begin()
					b = self.view.sel()[0].end()
				if '#' in RawText:
					a = self.view.find('#', begin).end()
				else:
					a = begin
				self.view.sel().clear
				self.view.sel().subtract(sublime.Region(begin, self.view.sel()[0].end()))
				self.view.sel().add(sublime.Region(a, b))
				self.view.window().run_command("slurp_find_string")

			# Path and JumpTo is ready, open it now!
			if Path != '' and os.path.exists(Path):
				base_name, file_extension = os.path.splitext(Path)
				if file_extension == "":    #it's folder => open in XY
					self.view.window().run_command("reveal_in_xyplorer", {"FilePath": base_name})
					# ahk_exe = sublime.packages_path() + "\\User\\" + "AHK.exe"
					# ahk_ahk = sublime.packages_path() + "\\User\\" + "AHK.ahk"
					# command = "winactivate, ahk_class ThunderRT6FormDC"
					# subprocess.Popen(['E:\\7Utilities\\XYplorer\\XYplorer.exe', base_name])
					# subprocess.Popen([ahk_exe, ahk_ahk, command])
				elif file_extension == ".chm" and JumpTo != "":
					arg = Path + JumpTo
					subprocess.Popen(["hh.exe", arg])
				elif file_extension in [".txt", ".ini", ".py"] or "sublime" in file_extension or ".tm" in file_extension:
					view = window.open_file(Path)
				else:
					if sublime.platform() == "windows":
						# xypath = self.view.settings().get('xypath')
						# arg = " /script=::open " + str('"') + Path + str('"')
						# sublime.message_dialog(arg)
						# subprocess.Popen([xypath + '\\XYplorer.exe', arg])
						os.startfile(Path)
					else:
						subprocess.call(["xdg-open", Path])  #Linux
			elif Path != '':
				new_view = window.new_file()
				new_view.insert(edit,0,"New file created")
				if RawPath.find('.') != -1:
					new_view.set_name(RawPath)
				else:
					new_view.set_name("%s.txt" % RawPath)
				new_view.set_syntax_file("Packages/Tidea/Tidea.tmLanguage")
			if JumpTo != "":
				sublime.set_timeout(lambda: self.view.window().run_command("find_next"), 150)
		elif "text.Tidea Alternatives" in ScopeName:
			# sublime.message_dialog(ScopeText)
			if ScopeText == "/":
				ScopeText = self.view.substr(self.view.extract_scope(self.view.sel()[0].a - 1))
			CursorLocationA = self.view.sel()[0].b
			CursorLocationB = CursorLocationA
			while self.view.substr(CursorLocationA) != "[":
				CursorLocationA = CursorLocationA - 1
			while self.view.substr(CursorLocationB) != "]":
				CursorLocationB = CursorLocationB + 1
			self.view.sel().clear
			self.view.sel().add(sublime.Region(CursorLocationA, CursorLocationB+1))
			self.view.replace(edit, self.view.sel()[0], ScopeText.strip("]"))
		else:
			window.run_command('goto_definition')
			# window.run_command("move_to", {"to": "hardeol"})        # Add new line
			# window.run_command("insert", {"characters": "\n"})      # Add new line

