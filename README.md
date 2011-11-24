TGG IRC Stats Creator
=====================

TISC is an IRC log parser and statistics generator. It feeds data into a CouchDB collection, and then uses a series of MapReduce queries to generate a statistics page.

It's written to be very configurable and pretty much query/template driven with a little bit of glue code.

Dependencies:

* CouchDB
* couchdb-python
* Genshi

Scripts:

* `init-couchdb` initializes the CouchDB collection, setting up the views.
* `feed-couchdb` adds an item to the collection
* `generate-pages` runs all the views, feeds results into the templates, and produces your files.

I'm basing the statistics to implement on <http://elanor.mine.nu/daeron/script.fi.html>.