# Extracting Tweets using Twitter API (Tweepy)

* Last modified date: 2020.05.05

## 1. Description


Extract tweets using the official Twitter API. Note that a user needs to create unique API key and access token to use this script. To request, visit [https://developer.twitter.com/en/docs/basics/authentication/oauth-1-0a/obtaining-user-access-tokens](https://developer.twitter.com/en/docs/basics/authentication/oauth-1-0a/obtaining-user-access-tokens). Also note that twitter API has rate limit [https://developer.twitter.com/en/docs/basics/rate-limiting](https://developer.twitter.com/en/docs/basics/rate-limiting).


## 2. Details


To use, enter your credentials for following part.


```python
consumer_key=""
consumer_secret=""
access_token=""
access_token_secret=""
```


and set up authentication


```python
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
```





## 3. Results (Example)


