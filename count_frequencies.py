# Imports a JSON file full of tweets and tokenizes the tweets.
# Stop words are generated using standard regexp lists and some custom character strings.
# Most of this code is taken from http://marcobonzanini.com/2015/03/17/mining-twitter-data-with-python-part-3-term-frequencies/

__author__ = 'Brad'

import json
import re
import operator
from collections import Counter
from nltk.corpus import stopwords
import string
from nltk import bigrams


# Pre-process for more accurate tokenization
from nltk.tokenize import word_tokenize

emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""

regex_str = [
    emoticons_str,
    r'<[^>]+>', # HTML tags
    r'(?:@[\w_]+)', # @-mentions
    r'(?:\#+[\w_]+[\w\'_\-]*[\w_]+)', # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs

    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
]

tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)

def tokenize(s):
    return tokens_re.findall(s)

def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens



# block stop-words
punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['rt','RT','via','I']

# Open my tweet file and tokenize the tweets
file_name = 'Northfire_unique.json'

with open(file_name, 'r') as f:
    count_all = Counter()
    for line in f:
        tweet = json.loads(line)
        # Create a list with all the terms
        # terms_all = [term for term in preprocess(tweet['text'])]
        terms_stop = [term for term in preprocess(tweet['text']) if term not in stop]
        terms_bigram = bigrams(terms_stop)
        # Update the counter
        #count_all.update(terms_stop)
        count_all.update(terms_bigram)
    # Print the first n most frequent words
    print(count_all.most_common(10))

