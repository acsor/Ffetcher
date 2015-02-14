#!/usr/bin/python

import os
from urllib import URLopener
from fetch import ImageThreadFetcher

class ImageThreadDownloader ():

    def __init__ (self, threadUrl, dest_dir):
        self.imageThreadFetcher = ImageThreadFetcher(threadUrl)
        self.dest_dir = dest_dir

    def __iter__ (self):
        opener = URLopener()

        for filename, url in self.imageThreadFetcher:
            try:
                # The tuple returned here is a couple of the filename in which the data is stored and the server response headers.
                yield opener.retrieve(url, self.dest_dir + filename)
            except IOError:
                yield None

def main ():
    import sys

    if len(sys.argv) < 2:
        exit(sys.argv[0] + ": <threadurl> [destdir]")

    url = sys.argv[1]
    dest_dir = "./" if (len(sys.argv) < 3) else sys.argv[2]

    if dest_dir[-1] != "/":
        dest_dir += "/"

    if not os.access(dest_dir, os.W_OK):
        raise EnvironmentError("\"%s\" does not have write permissions or does not exist." % dest_dir)

    for filename, response_headers in ImageThreadDownloader(url, dest_dir):
        print "Downloaded %s" % filename

if __name__ == "__main__":
    main()
