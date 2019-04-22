# Ffetcher

## Description
`Ffetcher` is a small collection of Python scripts aimed at fetching media
files from 4chan's threads.
It uses the APIs described [here](https://github.com/4chan/4chan-API).
If you're looking for a full-fledged 4chan Python's API, use
[py-4chan](https://github.com/bibanon/py-4chan) instead.

## Usage
`./main.py: <threadurl> [destdir]`

## Brief documentation
`fetcher.py` defines `Fetcher` as the base class used for fetching. Each
subclass defines a new JSON URL to fetch and the way to translate/filter it.  
For each link listed
[here](https://github.com/4chan/4chan-API#welcome), there's usually a new
subclass with the specified URL, and with its own method for translating the
JSON. Pretty simple.
Consider these classes to represent the data model.

`main.py` contains classes aimed at downloading the data provided from the
`fetcher` module. As of now, only `ImageThreadDownloader` is available.
