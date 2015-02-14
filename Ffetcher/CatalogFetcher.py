#!/usr/bin/python

from .Fetcher import Fetcher

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
