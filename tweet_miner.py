import tweepy
import datetime
import time
import json

class TweetMiner(object):
  result_limit = 20
  data = []
  api = False

  twitter_keys = {}

  def __init__(self, keys_dict=twitter_keys, api=api, result_limit=20):
    self.twitter_keys = keys_dict
    
    auth = tweepy.OAuthHandler(keys_dict['consumer_key'], keys_dict['consumer_secret'])
    auth.set_access_token(keys_dict['access_token'], keys_dict['access_token_secret'])
    
    self.api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    self.result_limit = result_limit

  def append_replies(self, data, user, since_id):
    replies = tweepy.Cursor(self.api.search, q='to:{}'.format(user), since_id=since_id, tweet_mode='extended').items(50)
    for reply in replies:
      try:
        if not hasattr(reply, 'in_reply_to_status_id_str'):
          continue
        if reply.in_reply_to_status_id_str == since_id:
          reply_mined_object = self.mined_object(reply)
          data.append(reply_mined_object)
          print("reply of tweet:{}".format(reply.full_text))
      except Exception as e:
        print("Failed while fetching replies {}".format(e))
        break

  def mined_object(self, item):
    mined = {
      'tweet_id': item.id_str,
      'name': item.user.name,
      'screen_name': item.user.screen_name,
      'retweet_count': item.retweet_count,
      'text': item._json["full_text"],
      'mined_at': datetime.datetime.now().strftime("%a %b %d %H:%M:%S %Y"),
      'created_at': item._json["created_at"],
      'favourite_count': item.favorite_count,
      'hashtags': item.entities['hashtags'],
      'status_count': item.user.statuses_count,
    }
    return mined

  def mine_user_tweets(self, user="dril", max_pages=5):
    data = []
    tweets = tweepy.Cursor(self.api.user_timeline, screen_name=user, tweet_mode="extended").items(max_pages*self.result_limit)
    for tweet in tweets:
      if tweet.in_reply_to_status_id == None and not hasattr(tweet, 'retweeted_status'):
        mined = self.mined_object(tweet)
        data.append(mined)
        self.append_replies(data, user, tweet.id_str)
    return data