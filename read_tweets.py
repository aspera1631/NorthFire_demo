# Imports a JSON file full of tweets and displays the text

__author__ = 'Brad'

import json
import re
import operator
from collections import Counter



file_name = 'my_tweets.json'


#with open(file_name, 'r') as f:
#    for line in f:
#        tweet = json.loads(line)
#        print(json.dumps(tweet, indent=4)) # pretty-print
        #print(tweet)


with open(file_name, 'r') as f:
    for line in f:
        tweet = json.loads(line)
        print(json.dumps(tweet, indent=4, sort_keys=True))