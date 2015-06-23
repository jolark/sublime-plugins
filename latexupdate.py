import sublime, sublime_plugin
import subprocess, shlex
import os

class LatexupdateCommand(sublime_plugin.WindowCommand):
	def run(self):
		filepath = self.window.active_view().file_name()
		filedir  = os.path.dirname(filepath)
		if filepath[-4:] == '.tex':
			os.chdir(filedir)
			self.window.active_view().run_command('save')
			# subprocess.call(shlex.split('pdflatex -input-directory=\''+ filedir + '\' ' + '-output-directory=\''+ filedir + '\' ' + filepath + ' > /dev/null'))
			subprocess.call(shlex.split('pdflatex ' + filepath + ' > /dev/null'))
			with open(filepath[:-4] + '.log', 'r') as f:
				# read_data = f.read()
				for line in f:
					if 'LaTeX Error' in line:
						print(line)
			f.closed