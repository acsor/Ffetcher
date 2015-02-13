#!/usr/bin/python

import sys, re, json

from Fetcher import Fetcher

class ThreadFetcher (Fetcher):

    # The matching parentheses groups are respectively the board's name and the thread's number.
    # Example: https://boards.4chan.org/lit/thread/6132992/what-do-you-think-of-catholicism#p6132992
    _threadUrlRegex = "^https?://boards.4chan.org/(\w+)/thread/(\d+).*$"
    _jsonUrlTpl = "http://a.4cdn.org/%s/thread/%s.json"

    # These are all JSON keys described here https://github.com/4chan/4chan-API.
    _keyFilename = u"filename"
    _keySrc = u"tim"
    _keyExt = u"ext"
    _keyRoot = u"posts"

    def __init__ (self, threadUrl):
        self.threadUrl = threadUrl
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
        _keyFilename = self._keyFilename     # Can't see why I need to do this, but I have to. Try to delete this line and see what happens.
        
        return (
                {post[self._keyFilename]: self._mediaUrlTpl % (self.boardName, (str(post[self._keySrc]) + post[self._keyExt]))}
                for post in posts
                if _keyFilename in post
        )

def main ():
    if len(sys.argv) == 1:
        exit(sys.argv[0] + ": you must input the thread URL.")

    threadUrl = sys.argv[1]

    for i in ImageThreadFetcher(threadUrl):
        print i

if __name__ == "__main__":
    main()
