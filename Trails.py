import pandas as pd
import snscrape.modules.twitter as sntwitter
import json

userID = 'user!'
# Check if it is a valid Twitter username.
checker = sntwitter.TwitterProfileScraper.is_valid_username(userID)
print(checker)
# get tweets from a user
tweets = []
limit = 10
index = 0

# define a function to get a json file from tweets for a user
def get_json(userID):
    tweets = []
    limit = 10
    index = 0
    tweets = sntwitter.TwitterProfileScraper(userID).get_items()
    for tweet in tweets:
        if index == limit:
            break
        # store in json file named UserID.json
        with open('../Meta/Twitter/'+userID+'.json', 'a') as f:
            json.dump(tweet.json(), f)
            f.write('\n')
        index = index + 1

get_json(userID)
# define a function to get rawContent from tweets for a user
def get_rawContent(userID):
    tweets = []
    limit = 10
    index = 0
    tweets = sntwitter.TwitterProfileScraper(userID).get_items()
    for tweet in tweets:
        if index == limit:
            break
        print(tweet.rawContent)
        index = index + 1

get_rawContent(userID)