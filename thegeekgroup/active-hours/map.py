# -*- tab-width: 4; use-tabs: 1; coding: utf-8 -*-
# vim:tabstop=4:noexpandtab:

def m(doc):
	if doc['event'] in ('message', 'action'):
		yield doc['when'][3], 1
