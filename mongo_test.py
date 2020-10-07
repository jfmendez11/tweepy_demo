import pymongo
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import datetime
import pprint

load_dotenv()

# Initialization
host = os.getenv("MONGO_DB_HOST")
port = int(os.getenv("MONGO_DB_PORT"))

client = MongoClient(host, port)

# Getting a database
db = client["test_twitter"]

# Getting a document
tweets = db["tweet"]

# Inserting a document
tweet = {
    'tweet_id': "123456789",
    'name': "Juan Felipe",
    'screen_name': "jfmendezp",
    'retweet_count': 10000,
    'text': "Solo millos loks!",
    'mined_at': datetime.datetime.now(),
    'created_at': datetime.datetime.now(),
    'favourite_count': 10000,
    'hashtags': ["millos", "tu papa"],
    'status_count': 100000,
}

tweet_id = tweets.insert_one(tweet).inserted_id

# print(tweet_id)

# print(db.list_collection_names())

# Getting a single document
retrieved_tweet = tweets.find_one({"_id": tweet_id})

pprint.pprint(retrieved_tweet)
print("------------------------------------------------\n")

# Bulk inserts
new_tweets = [
    {
        'tweet_id': "123456789",
        'name': "Millos David",
        'screen_name': "millostupapa",
        'retweet_count': 10000,
        'text': "Solo millos loks!",
        'mined_at': datetime.datetime.now(),
        'created_at': datetime.datetime.now(),
        'favourite_count': 10000,
        'hashtags': ["millos", "tu papa"],
        'status_count': 100000,
    },
{
        'tweet_id': "123456789",
        'name': "James 10",
        'screen_name': "jamesdavid",
        'retweet_count': 10000,
        'text': "Siempre quise jugar en millos!",
        'mined_at': datetime.datetime.now(),
        'created_at': datetime.datetime.now(),
        'favourite_count': 10000,
        'hashtags': ["millos", "dreamteam"],
        'status_count': 100000,
    },
]

result = tweets.insert_many(new_tweets)
for id in result.inserted_ids:
    tweet_from_bulk_insert = tweets.find_one({"_id": id})
    pprint.pprint(tweet_from_bulk_insert)

print("------------------------------------------------\n")

# Querying many docs
for tweet_ in tweets.find():
    pprint.pprint(tweet_)


print("------------------------------------------------\n")
# Counting
count = tweets.count_documents({})
print(count)
print("------------------------------------------------\n")

# Range queries
# Advanced queries at: https://docs.mongodb.com/manual/reference/operator/
for tweet_ in tweets.find({"favourite_count": {"$gt": 10001}}).sort("screen_name"):
    pprint.pprint(tweet_)
print("------------------------------------------------\n")
# Indexing
result = db.tweets.create_index([('mined_at', pymongo.ASCENDING)], unique=True) # Se debería usar el tweet_id ya que esto previene que se duplique
pprint.pprint(sorted(list(db.tweets.index_information())))