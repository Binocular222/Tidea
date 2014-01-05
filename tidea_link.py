import sublime, sublime_plugin, os, re, subprocess, webbrowser

class tidea_link(sublime_plugin.TextCommand):
    def run(self, view):
        CurPath = os.path.split(self.view.file_name())[0]
        window = self.view.window()
        slash = "\\" if sublime.platform() == "windows" else "/"
        CursorLocation = self.view.sel()[0]
        ScopeName = self.view.scope_name(CursorLocation.a)
        ScopeText = self.view.substr(self.view.extract_scope(CursorLocation.a)).replace("*", "")

        if "link.external" in ScopeName:
            if "http:" not in ScopeText and "ftp:" not in ScopeText and "https:" not in ScopeText:
                ScopeText = 'http://' + ScopeText
            window.run_command('open_url', {"url": ScopeText})
            # webbrowser.open(ScopeText, autoraise=True)
        elif "link.email" in ScopeName:
            window.run_command('open_url', {"url": "mailto:"+ScopeText})
        elif "link.internal" in ScopeName:
            RawText = ScopeText.lstrip('[[').rstrip(']]').lstrip(' ').rstrip(' ')
            if '#' in RawText:
                JumpTo = RawText.rsplit('#')[1]
                Path = RawText.rsplit('#')[0]
                if Path != '' and os.path.exists(Path) == 0: Path = CurPath+slash+Path
                if os.path.exists(Path) == 0:
                    Path = ""
                    JumpTo = RawText    #can be improved: Ask to create new file if there's dot character
            else:
                if os.path.exists(RawText) == 0:
                    Path = CurPath+slash+RawText
                    if os.path.exists(Path) == 0:
                        Path = ""       #can be improved: Ask to create new file if there's dot character
                        JumpTo = RawText
                    else:
                        JumpTo = ""
                else:
                    Path = RawText
                    JumpTo = ""
            if JumpTo != "":
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
                # subprocess.Popen(['E:\\7Utilities\\Launcher\\AutoHotkey\\AutoHotkey_noAdmin.exe', 'E:\\7Utilities\\Sublime Text\\Data\\Packages\\Tidea\\JumpTo.ahk', JumpTo], bufsize=0, executable=None, stdin=None, stdout=None, stderr=None, preexec_fn=None, close_fds=False, shell=False, cwd=None, env=None, universal_newlines=False, startupinfo=None, creationflags=0)
            if Path != '' and os.path.exists(Path):
                if Path[-4:] in [".txt", ".ini"] or Path[-3:] == ".py":
                    view = window.open_file(Path)
                else:
                    if sublime.platform() == "windows":
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
                sublime.set_timeout(lambda: self.view.window().run_command("find_next"), 100)
        else:
            window.run_command("move_to", {"to": "hardeol"})        # Add new line
            window.run_command("insert", {"characters": "\n"})      # Add new line
            # Position =  self.view.RawPath.find('.')   #self.view.file_name()[-4:]
            # sublime.status_message(Position)

