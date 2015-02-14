Ffetcher
=======

## Description ##

`Ffetcher`, pronounced `four fetcher`, is a Python package primarly aimed at fetching pics from 4chan's threads.
It uses the APIs described [here](https://github.com/4chan/4chan-API).
If you're looking for a full-fledged 4chan python's API, use [py-4chan](https://github.com/bibanon/py-4chan) instead.

## Usage ##

1. `Fetcher.py` defines the Fetcher class.
2. `ThreadFetcher.py` defines subclasses of Fetcher providing access to threads' content.
3. `CatalogFetcher.py` defines subclasses of Fetcher providing access to catalogs.
