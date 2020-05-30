#!/usr/bin/python3

import sys
import json
import re

def read_input(file):
    for line in file:
        if line.strip():
           json_line = json.loads(line)
           if len(json_line['body']) <= 150:
              yield json_line['body'].split(' ')

def main():
            data = read_input(sys.stdin)
            for words in data:
                for word in words:
                    word = re.sub("[^a-zA-Z]+", "", word)
                    if word.strip() and len(word)>0 and len(word)<=10:
                       print("%s\t%d" % (word, 1))


if __name__ == "__main__":
    main()
