#!/usr/bin/env python3.2
# -*- coding: utf-8 -*-

import sublime, sublime_plugin
from collections import defaultdict

class CountmapCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		text = self.view.substr(sublime.Region(0, self.view.size()))
		countmap = defaultdict(lambda: 0)
		for line in text.split('\n'):
			if line != "":
				countmap[line.strip()] += 1
				#print(line.encode('utf-8'))
		self.view.erase(edit, sublime.Region(0, self.view.size()))
		for elem in countmap:
			self.view.insert(edit, 0, elem + ',' + str(countmap[elem]) + '\n')
		self.view.erase(edit, sublime.Region(self.view.size()-1, self.view.size()))
			
