import pandas as pd
import snscrape.modules.twitter as sntwitter
import timeit
#tweets = []

query = 'from:whyyoutouzhele since:2023-01-01 until:2023-06-09'
limit = 1000

tweets = sntwitter.TwitterSearchScraper(query).get_items()
index = 0
df1 = pd.DataFrame(columns=['Date','URL' ,'Tweet'])
#for tweet in tweets:
#    if index == limit:
#        break
#    #URL = "https://twitter.com/{0}/status/{1}".format(tweet.user.username,tweet.id)
#    dict1 = {'Date': tweet.date, 'URL': tweet.url, 'Tweet': tweet.rawContent}
#    df1 = pd.concat([df1, pd.DataFrame.from_records([dict1])])
#    index = index + 1


# define a function of above
def get_df_from_search(query: str, limit:int) -> pd.DataFrame:
    '''
    Input: limits of the number of tweets
    Output: Dataframe with 'Datetime', 'URL', 'Tweet', 'Username
    '''
    tweets = sntwitter.TwitterSearchScraper(query).get_items()
    index = 0
    df = pd.DataFrame(columns=['Date','URL' ,'Tweet'])
    for tweet in tweets:
        if index == limit:
            break
        dict = {'Date': tweet.date, 'URL': tweet.url, 'Tweet': tweet.rawContent}
        df = pd.concat([df, pd.DataFrame.from_records([dict])])
        index = index + 1
    return df

def get_df_from_search_2(query: str, limit:int) -> pd.DataFrame:
    tweets = sntwitter.TwitterSearchScraper(query).get_items()
    index = 0
    df = pd.DataFrame(columns=['Date','URL' ,'Tweet'])
    for tweet in tweets:
        if index == limit:
            break
        dict = {'Date': tweet.date, 'URL': tweet.url, 'Tweet': tweet.rawContent}
        index = index + 1
    # covert dict to dataframe
    df = pd.DataFrame.from_dict(dict, orient='index')
    return df


# make the function into list comprehension
#df = pd.DataFrame([{'Date': tweet.date, 'URL': tweet.url, 'Tweet': tweet.rawContent} for i, tweet in enumerate(tweets) if i < limit])
#df = pd.DataFrame.from_dict(dict, orient='index')

def get_df_from_search_3(query: str, limit:int) -> pd.DataFrame:
    tweets = sntwitter.TwitterSearchScraper(query).get_items()
    tweet_data = [{'Date': tweet.date, 'URL': tweet.url, 'Tweet': tweet.rawContent} for i, tweet in enumerate(tweets) if i < limit]
    df = pd.DataFrame(tweet_data)
    return df
#print(get_df_from_search_3(query, limit))

starttime = timeit.default_timer()
print("The start time is :",starttime)
get_df_from_search_3(query, limit)
print("The time difference is :", timeit.default_timer() - starttime)
# # Converting time zone from UTC to GMT+8
#df1['Date'] = df1['Date'].dt.tz_convert('Etc/GMT+8')
#print(df)

#df.to_csv('../Meta/Twitter/tweets.csv', index = False, encoding='utf_8_sig')