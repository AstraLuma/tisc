def m(doc):
    if doc['event'] in ('message', 'action'):
        yield doc['when'][3], 1
