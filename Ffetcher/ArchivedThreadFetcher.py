#!/usr/bin/python

from Fetcher import Fetcher
import sys

class ArchivedThreadFetcher (Fetcher):

    _jsonUrlTpl = "https://a.4cdn.org/%s/archive.json"

    def __init__ (self, boardName):
        self.boardName = boardName

    def getJsonUrlStep (self):
        return self._jsonUrlTpl % self.boardName

    def translateJsonStep (self, jsonDecodeData):
        return jsonDecodeData.__iter__()

def main ():
    if len(sys.argv) == 1:
        exit(sys.argv[0] + ": you must input the board name.")

    boardName = sys.argv[1]

    for i in ArchivedThreadFetcher(boardName):
        print i

if __name__ == "__main__":
    main()
