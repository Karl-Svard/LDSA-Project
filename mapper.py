#!/usr/bin/python3
"""mapper.py"""

import sys
import json

# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()

    # parse json file
    comment = json.loads(line)

    #
    subreddit = comment["subreddit"]
    score = comment["score"]
    gilded = comment["gilded"]

    print("%s\t%s" % (subreddit + "_comments", 1))
    print("%s\t%s" % (subreddit + "_score", score))
    if gilded > 0:
        print("%s\t%s" % (subreddit + "_gilded", gilded))




