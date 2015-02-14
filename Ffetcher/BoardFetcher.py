#!/usr/bin/python

from Fetcher import Fetcher
import sys

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

def main ():
    for i in BoardFetcher():
        print i

if __name__ == "__main__":
    main()
