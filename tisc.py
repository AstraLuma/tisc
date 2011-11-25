# -*- tab-width: 4; use-tabs: 1; coding: utf-8 -*-
# vim:tabstop=4:noexpandtab:
"""
doc string
"""
from __future__ import division, absolute_import, with_statement
import os, json, couchdb.client
__all__ = 'Tisc',

class Tisc(object):
	def __init__(self, root=None):
		if root is None:
			self.root = os.path.dirname(__file__)
		else:
			self.root = root
		
		self.config = json.load(self.file('config.json'))
	
	def filename(self, *p):
		return os.path.join(self.root, *p)
	
	def file(self, fn, *p):
		return open(self.filename(fn), *p)
	
	def option(self, key, default=None):
		return self.config['__options__'].get(key, default)
	
	def views(self):
		for view in os.listdir(self.root):
			viewpath = os.path.join(self.root, view)
			if not os.path.isdir(viewpath) or view[0] in '._':
				continue
			else:
				yield view, viewpath
	
	def sections(self, view):
		for section in os.listdir(os.path.join(self.root, view)):
			sectionpath = os.path.join(self.root, view, section)
			if not os.path.isdir(sectionpath):
				continue
			elif not os.path.exists(os.path.join(sectionpath, "map.py")):
				warnings.warn("No map file for section %s found!" % section)
				continue
			else:
				yield section, sectionpath
	
	def issection(self, view, section):
		return os.path.isdir(os.path.join(self.root, view, section))
	
	_collection = None
	def couch(self):
		if self._collection is None:
			self._collection = couchdb.client.Server()[self.option('collection')]
		return self._collection
	
	def genshipaths(self, view=None, section=None):
		pl = [os.path.join(self.root, "_include")]
		if view is not None:
			pl.append(os.path.join(self.root, view))
			if section is not None:
				pl.append(os.path.join(self.root, view, section))
		pl.reverse()
		return pl
