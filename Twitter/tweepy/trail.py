import tweepy


client = tweepy.Client("BEARER_TOKEN")

query = 'from:elonmusk -is:retweet'
tweets = client.search_recent_tweets(query=query, max_results=100)

for tweet in tweets.data:
    print(tweet.text)