import pandas as pd
import snscrape.modules.twitter as sntwitter
#tweets = []

query = 'from:whyyoutouzhele since:2023-06-01 until:2023-06-09'
limit = 1

tweets = sntwitter.TwitterSearchScraper(query).get_items()
index = 0
df = pd.DataFrame(columns=['Date','URL' ,'Tweet'])

for tweet in tweets:
    if index == limit:
        break
    #URL = "https://twitter.com/{0}/status/{1}".format(tweet.user.username,tweet.id)
    df2 = {'Date': tweet.date, 'URL': tweet.url, 'Tweet': tweet.rawContent}
    df = pd.concat([df, pd.DataFrame.from_records([df2])])
    index = index + 1
    print(tweet.user.username)

# # Converting time zone from UTC to GMT+8
df['Date'] = df['Date'].dt.tz_convert('Etc/GMT+8')
#print(df)

#df.to_csv('../Meta/Twitter/tweets.csv', index = False, encoding='utf_8_sig')