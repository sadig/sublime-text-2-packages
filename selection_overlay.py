#coding=utf-8
import sublime_plugin

class SelectionOverlayCommand(sublime_plugin.TextCommand):
    "ctrl+ü => find that file with overlay"
    def run(self, edit):
        selection = self.view.substr(self.view.sel()[0])
        self.view.window().run_command(
            "show_overlay",
            {
                "overlay": "goto",
                "show_files": True,
                "text": selection.lower()
            }
        )

