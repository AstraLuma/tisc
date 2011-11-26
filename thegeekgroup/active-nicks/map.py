# -*- tab-width: 4; use-tabs: 1; coding: utf-8 -*-
# vim:tabstop=4:noexpandtab:

def m(doc):
	if doc['event'] in ('message', 'action'):
		data = {
			'nick': doc['sender'],
			'lines': 1,
			'blue': 0,
			'green': 0,
			'yellow': 0,
			'red': 0,
			'words': len(doc['text'].split()),
			'chars': len(doc['text']),
			'oldest': doc['when'],
			'newest': doc['when'],
			'random': doc['text'],
			}
		color = ['blue', 'green', 'yellow', 'red'][doc['when'][3]//6]
		data[color] = 1
		yield doc['sender'].lower(), data
