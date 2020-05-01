import tweepy
import csv
import sqlite3


# twitter error message (doc: https://readthedocs.org/projects/tweepy/downloads/pdf/latest/)
def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.TweepError:
            print("error")
            break

# obtain unique user access tokens from https://developer.twitter.com/en/docs/basics/authentication/oauth-1-0a/obtaining-user-access-tokens
consumer_key=""
consumer_secret=""
access_token=""
access_token_secret=""
# authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

# if you have list of twitter handles as a separate file, read that file
""" name = []
with open('politician.txt', mode='r') as csv_file:
	csv_reader = csv.DictReader(csv_file)
	line_count = 0
	for row in csv_reader:
		if line_count == 0:
			line_count +=1
		name.append(row["name"])
		line_count+=1 """

# if not, create a list of twitterhandles.
name = '@WhiteHouse'

conn = sqlite3.connect('tweet.db')
c = conn.cursor()
# c.execute("""CREATE TABLE tweet (
# 	unique_ID integer,
# 	tweet_ID text,
# 	tweet text,
# 	tweet_dates date,
# 	tweet_place text,
# 	retweet_count integer,
# 	followers integer,
# 	location text,
# 	friends_count integer,
# 	user_created_account date)
# 	""")

