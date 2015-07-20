__author__ = 'Brad'

# make a list of timestamps from a JSON twitter file. Save this list to ASCII file.

import json
import time
import datetime

timestamps = [] # empty list
file_in = 'Northfire2.json'
file_out = 'timestamps2.txt'

with open(file_in,'r') as f:
    for line in f:
        # Load single line from file
        tweet = json.loads(line)
        # Tag the quantities in Twitter timestamp
        pt =datetime.datetime.strptime(tweet['created_at'],'%a %b %d %H:%M:%S +0000 %Y')
        # Convert to seconds
        total_seconds = pt.day*3600*24 + pt.second + pt.minute*60 + pt.hour*3600
        with open(file_out,'a') as fout:
            # Record the timestamp by appending to file
            fout.write("%s\n" % total_seconds)

        # Optional: check what the tweets looked like at particular times
        #if total_seconds > 1571815 + 338*60 and total_seconds < 1571815 + 348*60: