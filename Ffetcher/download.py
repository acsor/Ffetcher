#!/usr/bin/python

import os
from urllib import URLopener
from fetch import ImageThreadFetcher

class ImageThreadDownloader ():

    def __init__ (self, imageThreadFetcher, dest_dir = None):
        self.imageThreadFetcher = imageThreadFetcher
        self.dest_dir = dest_dir if dest_dir is not None else os.getcwd()

        if not os.access(self.dest_dir, os.W_OK):
            raise EnvironmentError("%s does not have write permissions." % self.dest_dir)

    def __iter__ (self):
        opener = URLopener()

        for filename, url in self.imageThreadFetcher:
            try:
                yield opener.retrieve(url, self.dest_dir + filename)
            except IOError:
                yield None

def main ():
    import sys

    if len(sys.argv) < 2:
        exit(sys.argv[0] + ": <threadurl> [destdir]")

    url = sys.argv[1]
    dest_dir = "./" if (len(sys.argv) < 3) else sys.argv[2]

    for filename, response_headers in ImageThreadDownloader (ImageThreadFetcher(url), dest_dir):
        print "Downloaded %s" % filename

if __name__ == "__main__":
    main()
