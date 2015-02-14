Ffetcher
=======

## Description ##

`Ffetcher`, pronounced `four fetcher`, is a Python package primarly aimed at fetching pics from 4chan's threads.
It uses the APIs described [here](https://github.com/4chan/4chan-API).
If you're looking for a full-fledged 4chan python's API, use [py-4chan](https://github.com/bibanon/py-4chan) instead.

## Brief documentation ##

`fetch.py` defines `Fetcher` as the base class used for fetching. Each subclass defines a new JSON URL to fetch and the way to translate/filter it.
Practically, for each link listed [here](https://github.com/4chan/4chan-API#welcome), there's usually a new subclass with the specified URL, and with its own method for translating the JSON. Pretty simple.
Consider these classes to represent the data model.

`download.py` contains classes aimed at downloading the data provided from the `fetch` module. As for now, only `ImageThreadDownloader` is available.
