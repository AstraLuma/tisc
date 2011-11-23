# -*- tab-width: 4; use-tabs: 1; coding: utf-8 -*-
# vim:tabstop=4:noexpandtab:
"""
doc string
"""
from __future__ import division, absolute_import, with_statement
import os
__all__ = 'Tisc',

class Tisc(object):
	def __init__(self, root=None):
		if root is None:
			self.root = os.path.dirname(__file__)
		else:
			self.root = root
	
	def pages(self):
		for page in os.listdir(self.root):
			pagepath = os.path.join(self.root, page)
			if not os.path.isdir(pagepath) or page[0] in '._':
				continue
			else:
				yield page
	
	def sections(self, page):
		for section in os.listdir(os.path.join(self.root, page)):
			sectionpath = os.path.join(self.root, page, section)
			if not os.path.isdir(sectionpath):
				continue
			elif not os.path.exists(os.path.join(sectionpath, "map.py")):
				warnings.warn("No map file for section %s found!" % section)
				continue
			else:
				yield section

