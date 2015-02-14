#!/usr/bin/python

import urllib, json

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
