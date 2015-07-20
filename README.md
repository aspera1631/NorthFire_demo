# NorthFire_demo
Demo of Twitter datamining for Insight interview

listen_tweets.py: Stream tweets from Twitter, filtering for a certain string. You have to put in your authentication details, like the consumer key and secret. You get those when you register an app.

discard_RT.py: For each tweet, check if it's a retweet. If not, save it to a file. Count the number of original tweets and retweets.

count_frequencies.py: Tokenize the text from all tweets in a file and find the most common words or bigrams using the natural language toolkit.

retweet_stats.py: List the most common retweets in order.

get_timestamps.py: Convert the "created_at" value from each tweet into seconds, and store all of the values to a .txt file.
