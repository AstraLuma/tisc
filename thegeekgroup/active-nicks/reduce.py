# -*- tab-width: 4; use-tabs: 1; coding: utf-8 -*-
# vim:tabstop=4:noexpandtab:

def r(keys, values, rereduce):
	data = {
		'nick': values[0]['nick'],
		'lines': 0,
		'blue': 0,
		'green': 0,
		'yellow': 0,
		'red': 0,
		'words': 0,
		'chars': 0,
		'oldest': values[0]['oldest'],
		'newest': values[0]['newest'],
		'random': __import__('random').choice([v['random'] for v in values]),
		}
	for value in values:
		data['lines'] += value['lines']
		data['blue'] += value['blue']
		data['green'] += value['green']
		data['yellow'] += value['yellow']
		data['red'] += value['red']
		data['words'] += value['words']
		data['chars'] += value['chars']
		if value['oldest'] < data['oldest']:
			data['oldest'] = value['oldest']
		if value['newest'] < data['newest']:
			data['newest'] = value['newest']
	return data

