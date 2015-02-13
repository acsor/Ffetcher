#!/usr/bin/python

import sys, re, urllib, json

class TranslationProcess:

    def __init__ (self, threadUrl):
        self.threadUrl = threadUrl
        self.boardName = self.getBoardName(threadUrl)

    def __iter__ (self):
        return self.translateJsonStep (
            self.fetchJsonStep (
                self.getJsonUrlStep (self.threadUrl)
            )
        )

    def getBoardName (self, srcThreadUrl):
        """Returns the name of the board."""
        raise NotImplementedError()

    def getJsonUrlStep (self, srcThreadUrl):
        """Returns the URL to fetch the JSON from."""
        raise NotImplementedError()

    def fetchJsonStep (self, jsonUrl):
        """Downloads the JSON from the API center."""
        raise NotImplementedError()

    def translateJsonStep (self, jsonDict):
        """
        This is where you get the decoded JSON data returned by the fetchJsonStep() method.
        You can do whatever you want with it.
        """

        raise NotImplementedError()

class TranslationProcessV1 (TranslationProcess):

    # The matching parentheses groups are respectively the board's name and the thread's number.
    # Example: https://boards.4chan.org/lit/thread/6132992/what-do-you-think-of-catholicism#p6132992
    _threadUrlRegex = "^https?://boards.4chan.org/(\w+)/thread/(\d+).*$"
    _jsonUrlTpl = "http://a.4cdn.org/%s/thread/%s.json"
    _mediaUrlTpl = "https://i.4cdn.org/%s/%s"

    # These are all JSON keys described here https://github.com/4chan/4chan-API.
    _keyFilename = u"filename"
    _keySrc = u"tim"
    _keyExt = u"ext"
    _keyRoot = u"posts"

    def getBoardName (self, srcThreadUrl):
        return re.match(self._threadUrlRegex, srcThreadUrl).group(1)

    def getJsonUrlStep (self, srcThreadUrl):
        match = re.match(self._threadUrlRegex, srcThreadUrl)

        return self._jsonUrlTpl % (match.group(1), match.group(2))

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

    for i in TranslationProcessV1(threadUrl):
        print i

if __name__ == "__main__":
    main()
