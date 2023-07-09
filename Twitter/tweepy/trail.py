import tweepy
api_key = 'owjYr5mvQvHv30zyUom7Zb8TT'
api_key_secret = 'ZclerRcrtS5BMxqWVVO9mTvD9xYrofVqco28syvTcXxKXJA4rg'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAO%2FNogEAAAAAYrQBm8t5hmludDv7TePWlh1nVIs%3DyG9bVxkrJONCEOPjEBIDcBqJ6H5ChfTomPfdqnUyHXfbinEUfL'

client = tweepy.Client("AAAAAAAAAAAAAAAAAAAAAO%2FNogEAAAAAYrQBm8t5hmludDv7TePWlh1nVIs%3DyG9bVxkrJONCEOPjEBIDcBqJ6H5ChfTomPfdqnUyHXfbinEUfL")

query = 'from:elonmusk -is:retweet'
tweets = client.search_recent_tweets(query=query, max_results=100)

for tweet in tweets.data:
    print(tweet.text)