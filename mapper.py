#!/usr/bin/python3

import sys
import json
import re

#sys.path.append('.')

pronouns = ['hen','hon','den','det','denna','denne','han']

def read_input(file):
    for line in file:
        if line.strip():
           json_line = json.loads(line)
           if len(json_line['body']) <= 150:
              yield json_line['body'].split(' ')

#def match_word(word):
    #Match the pronoun for each word of the tweet text
 #   for i in range(len(pronouns)):
  #      raw_string = "\\b" + pronouns[i] + "\\b"
   #     regex_name = re.compile(raw_string,re.IGNORECASE)
    #    x = regex_name.search(word)
     #   if x:
      #     return i,x
   # return i,0

def main():
            data = read_input(sys.stdin)
            for words in data:
                for word in words:
                    word = re.sub("[^a-zA-Z]+", "", word)
                    if word.strip() and len(word)>0 and len(word)<=10:
                       print("%s\t%d" % (word, 1))
                    #i,x = match_word(word)
                    #if x:
                    #print '%s%s%d' % (pronouns[i],separator,1)
#                    	print '%s%s%d' % (word,separator,1)


if __name__ == "__main__":
    main()
#for line in sys.stdin:
    # Supprimer les espaces
#    line = line.strip()
    # recupérer les mots
#    words = line.split()

    # operation map, pour chaque mot, generer la paire (mot, 1)
 #   for word in words:
  #      print("%s\t%d" % (word, 1))
