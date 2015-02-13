4fetcher
=======

## Description ##

`4fetcher` uses the APIs described [here](https://github.com/4chan/4chan-API).
If you're looking for a full-fledged 4chan python's API, [py-4chan](https://github.com/bibanon/py-4chan) is the right choice.

## Usage ##

Three scripts:

1. `fetch.py` outputs a dictionary whose pair are `filename`: `URL to fetch`.
2. `download.py` actually downloads them.
3. `main.py` starts the whole thing. The only argument required, if you're launching
it from the shell, is the thread URL. Dive into the code for more.
