#!/usr/bin/python

import urllib, json, sys, re

class Fetcher:

    def __iter__ (self):
        return self.translateJsonStep (
            self.__fetchJsonStep (
                self.getJsonUrlStep()
            )
        )

    def getJsonUrlStep (self):
        raise NotImplementedError()

    def fetchJsonStep (self, jsonUrl):
        try:
            f = urllib.urlopen(jsonUrl)

            if f is not None:
                response = f.read()
            else:
                return None
        finally:
            if f is not None:
                f.close()

        return json.loads(response)

    def translateJsonStep (self, jsonDecodedData):
        raise NotImplementedError()

    __fetchJsonStep = fetchJsonStep

class ThreadFetcher (Fetcher):

    # The matching parentheses groups are respectively the board's name and the thread's number.
    # Example: https://boards.4chan.org/lit/thread/6132992/WHATEVER
    _threadUrlRegex = "^https?://boards.4chan.org/(\w+)/thread/(\d+).*$"
    _jsonUrlTpl = "http://a.4cdn.org/%s/thread/%s.json"

    # These are all JSON keys described here https://github.com/4chan/4chan-API.
    _keyFilename = u"filename"
    _keySrc = u"tim"
    _keyExt = u"ext"
    _keyRoot = u"posts"

    def __init__ (self, threadUrl):
        self.threadUrl = threadUrl

        if not re.match(self._threadUrlRegex, self.threadUrl):
            raise EnvironmentError("\"%s\" is not a valid URL." % self.threadUrl)

        self.boardName = re.match(self._threadUrlRegex, threadUrl).group(1)
        self.threadNo = re.match(self._threadUrlRegex, threadUrl).group(2)

    def getJsonUrlStep (self):
        match = re.match(self._threadUrlRegex, self.threadUrl)

        return self._jsonUrlTpl % (match.group(1), match.group(2))

    def translateJsonStep (self, jsonDict):
        raise NotImplementedError()

class ImageThreadFetcher (ThreadFetcher):

    _mediaUrlTpl = "https://i.4cdn.org/%s/%s"

    def translateJsonStep (self, jsonDict):
        posts = jsonDict[self._keyRoot]
        
        return (
                (
                    post[self._keyFilename] + post[self._keyExt],   # Filename + extension
                    self._mediaUrlTpl % (self.boardName, (str(post[self._keySrc]) + post[self._keyExt]))    # URL to fetch
                )
                for post in posts
                if self._keyFilename in post
        )

class ArchivedThreadFetcher (Fetcher):

    _jsonUrlTpl = "https://a.4cdn.org/%s/archive.json"

    def __init__ (self, boardName):
        self.boardName = boardName

    def getJsonUrlStep (self):
        return self._jsonUrlTpl % self.boardName

    def translateJsonStep (self, jsonDecodeData):
        return jsonDecodeData.__iter__()

class BoardFetcher (Fetcher):

    _jsonUrlTpl = "https://a.4cdn.org/boards.json"
    _boardUrlTpl = "https://boards.4chan.org/%s/"

    _keyRoot = u"boards"
    _keyBoardName = u"board"
    _keyBoardTitle = u"title"

    def getJsonUrlStep (self):
        return self._jsonUrlTpl

    def translateJsonStep (self, jsonDecodedData):
        boards = jsonDecodedData[self._keyRoot]

        return (
                {board[self._keyBoardTitle]: self._boardUrlTpl % board[self._keyBoardName]}
                for board in boards
        )

class CatalogFetcher (Fetcher):

    _jsonUrlTpl = "https://a.4cdn.org/%s/catalog.json"

    _keyRoot = u"posts"

    def __init__ (self, boardName):
        self.boardName = boardName

    def getJsonUrlStep (self):
        return self._jsonUrlTpl % self.boardName

    def translateJsonStep (self, jsonDecodedData):
        """Incomplete"""
        print jsonDecodedData
        return jsonDecodedData[self._keyRoot]
