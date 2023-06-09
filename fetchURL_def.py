import pandas as pd
import snscrape.modules.twitter as sntwitter


# wirte a class for these codes above
class FetchTwitterUrl:
    def __init__(self, query, limit):
        '''
        query: query = 'from:userID since:YYYY-MM-DD until:YYYY-MM-DD'
        limit: int
        '''
        self.query = query
        self.limit = limit
        self.tweets = []
        self.df = pd.DataFrame(columns=['Date','URL' ,'Tweet'])

    def get_tweets(self):
        self.tweets = sntwitter.TwitterSearchScraper(self.query).get_items()

    def get_df(self):
        index = 0
        for tweet in self.tweets:
            if index == self.limit:
                break
            URL = "https://twitter.com/{0}/status/{1}".format(tweet.user.username,tweet.id)
            df2 = {'Date': tweet.date, 'URL': URL, 'Tweet': tweet.rawContent}
            self.df = pd.concat([self.df, pd.DataFrame.from_records([df2])])
            index = index + 1
        return self.df

    def get_csv(self):
        # extract userID from query str
        self.userID = self.query.split(' ')[0].split(':')[1]
        self.df.to_csv('../Meta/Twitter/'+self.userID+'.csv', index = False, encoding='utf_8_sig')

### test
# fetch_twitter_url = FetchTwitterUrl('from:whyyoutouzhele since:2023-06-01 until:2023-06-09', 1000)
# fetch_twitter_url.get_tweets()
# fetch_twitter_url.get_df()
# fetch_twitter_url.get_csv()