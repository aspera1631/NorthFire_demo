# Saves a new file that only includes non-retweets
# Also optionally saves them in different files.

__author__ = 'Brad'

import json

in_file = 'Northfire2.json'
out_file = 'Northfire_unique.json'

retweets = 0;
unique = 0;


with open(in_file, 'r') as f:
    for line in f:
        tweet = json.loads(line)
        if tweet['text'][0:2] == 'RT': # Count retweets (sanity check)
            retweets += 1
        if tweet['text'][0:2] != 'RT': # Count original tweets
            with open(out_file,'a') as fout:
                fout.write(line)
                fout.write('\n')
                #print(tweet.json['text'])
            unique += 1

print('Retweets = %s' % retweets)
print('Unique tweets = %s' % unique)
