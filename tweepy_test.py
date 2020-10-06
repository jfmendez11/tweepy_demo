import tweepy
from dotenv import load_dotenv
import os
import json
from tweet_miner import TweetMiner

load_dotenv()

twitter_keys = {
    "consumer_key": os.getenv("TWITTER_API_KEY"),
    "consumer_secret": os.getenv("TWITTER_API_SECRET_KEY"),
    "access_token": os.getenv("TWITTER_ACCESS_TOKEN"),
    "access_token_secret": os.getenv("TWITTER_ACCESS_TOKEN_SECRET"),
}

miner = TweetMiner(keys_dict=twitter_keys, result_limit=20)
data = miner.mine_user_tweets(user="agaviriau", max_pages=10)

print(json.dumps(data, indent=2))
#consumer_key = twitter_keys["consumer_key"]
#consumer_secret = twitter_keys["consumer_secret"]

#access_token = twitter_keys["access_token"]
#access_token_secret = twitter_keys["access_token_secret"]

#auth1 = tweepy.OAuthHandler(consumer_key, consumer_secret)
#auth1.set_access_token(access_token, access_token_secret)

#auth2 = tweepy.AppAuthHandler(consumer_key, consumer_secret)

#api1 = tweepy.API(auth1)
#api2 = tweepy.API(auth2)

#public_tweets = api1.user_timeline("agaviriau")
#for tweet in tweepy.Cursor(api1.user_timeline, screen_name="agaviriau").items(3):
#    print(json.dumps(tweet._json, indent=2))
#    print("--------------------------------------------------------------------")
#status = public_tweets[0]

#rint(status.quoted_status)
"""
json_str = json.dumps(status._json)
parsed = json.loads(json_str)
print(json.dumps(parsed, indent=4, sort_keys=True))
"""

#timeline = api2.user_timeline("agaviriau")
#l = dir(timeline)
#print(l)
#for attr in l:
#    print(attr, type(attr))

#print(timeline.index)
#print(timeline.ids)
#user = api2.get_user("agaviriau")
#print(user.name, user.screen_name, user.id, user.id_str, user.verified, user.profile_image_url, user.profile_image_url_https)
#print(api2.user_timeline("agaviriau"))

#for tweet in tweepy.Cursor(api.search, q='tweepy').items(10):
#    print(tweet.text)

# Code snippets
# http://docs.tweepy.org/en/latest/code_snippet.html
