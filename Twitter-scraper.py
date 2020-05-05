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
with open('twitterHandles.txt', mode='r') as csv_file:
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
# 	user_created_account date)
# 	""")

# retrieiving tweets in the order of twitter handles, and by time
for i in name:
	counter = 0
	print("*********************"+i+"*************************")
	print("*********************"+i+"*************************")
	print("*********************"+i+"*************************")
	print("*********************"+i+"*************************")




	for status in limit_handled(tweepy.Cursor(api.user_timeline, id=i).items()):

		check = []

		unique_tweet_id = (status._json['id'])
		tweet_name = (status._json['user']['screen_name'])
		tweet_id = (status._json['user']['name'])
		a = api.get_status(unique_tweet_id, tweet_mode='extended')
		text = a.full_text

		check.append(unique_tweet_id)
		check.append(tweet_id)
		check.append(text)
		check.append(tweet_name)

		c.execute("INSERT INTO tweet VALUES (?,?,?,?)", (check))
		
		conn.commit()
		
		counter+=1
	
	print(counter)

conn.close()

