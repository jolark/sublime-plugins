import sublime, sublime_plugin
import subprocess, shlex
import os

class LatexupdateCommand(sublime_plugin.WindowCommand):
	def run(self):
		filepath = self.window.active_view().file_name()
		filedir  = os.path.dirname(filepath)
		if filepath[-4:] == '.tex':
			self.window.active_view().run_command('save')
			subprocess.call(shlex.split('pdflatex -output-directory=\''+ filedir + '\' ' + filepath + ' > /dev/null'))