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
* `generate-files` runs all the views, feeds results into the templates, and produces your files.
* `feed-tgglog` downloads given days from the log file at <http://irclog.perlgeek.de/thegeekgroup/> and saves them to CouchDB. Note that downloading the same day multiple times won't cause duplication.
* `seed-tgglog` runs `feed-tgglog` for all known days, basically initializing your database.

I'm basing the statistics to implement on <http://elanor.mine.nu/daeron/script.fi.html>.

Installation
------------

1. Download and install dependencies
    * Debian, Ubuntu: `couchdb`, `python-couchdb`, and `python-genshi`
    * Source: [CouchDB](http://couchdb.apache.org/downloads.html), [CouchDB Python](http://code.google.com/p/couchdb-python/), [Genshi](http://genshi.edgewall.org/wiki/Download)
2. Clone TISC's repository. See the top of the page.
3. Check `config.json`, especially the destination directory.
4. Run `init-couchdb`
5. Run `seed-tgglog`. This will take a while.
6. Run `generate-files`. This will take a long time while CouchDB generates the views.

You should then have statistics pages in your destination directory. By default, the only file generated is `index.html`.