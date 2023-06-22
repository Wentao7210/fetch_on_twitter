import pandas as pd
import snscrape.modules.twitter as sntwitter
import os

class FetchTweets:
    def get_tweets_from_search(self, query: str):
        '''
        Input: 
            1. 'search text since:YYYY-MM-DD until:YYYY-MM-DD'
            2. 'From: userID since:YYYY-MM-DD until:YYYY-MM-DD' (alternative of get user tweets)
        Output: tweets (generator)
        '''
        self.query = query
        self.tweets_from_search = sntwitter.TwitterSearchScraper(self.query).get_items()

    def get_df_from_search(self, limit:int) -> pd.DataFrame:
        '''
        Input: limits of the number of tweets
        Output: Dataframe with 'Datetime', 'URL', 'Tweet', 'Username
        '''
        self.limit = limit
        self.df_from_search = pd.DataFrame(columns=['Datetime', 'URL', 'Tweet', 'Username'])
        index = 0
        for tweet in self.tweets_from_search:
            if index == self.limit:
                break
            #URL = "https://twitter.com/{0}/status/{1}".format(tweet.user.username,tweet.id) -> alternative
            dict_df = {'Datetime': tweet.date, 'URL': tweet.url, 'Tweet': tweet.rawContent, 'Username': tweet.user.username}
            self.df_from_search = pd.concat([self.df_from_search, pd.DataFrame.from_records([dict_df])])
            index = index + 1
        self.df_from_search.to_csv('F:\Meta\Twitter\ADHD.csv', index=False, encoding='utf_8_sig')
        return self.df_from_search

    def get_tweets_from_user(self, userID: str):
        '''
        Input: userID
            E.g.: 'elonmusk'
        Output: tweets (generator)
        '''
        self.user_id = userID
        self.tweets_from_user = sntwitter.TwitterProfileScraper(self.user_id).get_items()
    
    def get_df_from_user(self, limit:int) -> pd.DataFrame:
        '''
        Input: limits of the number of tweets
        Output: Dataframe with 'Datetime', 'URL', 'Tweet', 'Username
        '''
        self.limit = limit
        self.df_from_user = pd.DataFrame(columns=['Datetime', 'URL', 'Tweet', 'Username'])
        index = 0
        for tweet in self.tweets_from_user:
            if index == self.limit:
                break
            #URL = "https://twitter.com/{0}/status/{1}".format(tweet.user.username,tweet.id) -> alternative
            dict_df = {'Datetime': tweet.date, 'URL': tweet.url, 'Tweet': tweet.rawContent, 'Username': tweet.user.username}
            self.df_from_user = pd.concat([self.df_from_user, pd.DataFrame.from_records([dict_df])])
            index = index + 1
        return self.df_from_user
    

class TwitterVideoDownload:
    def __init__(self, output_directory):
        self.output_directory = output_directory
    
    def download_videos_from_list(self, url_list):
        for i, url in enumerate(url_list):
            file_name = f"twittervid{i}.mp4"
            self.download_twitter_video(url, file_name)

    def download_videos_from_csv(self, csv_file):
        df = pd.read_csv(csv_file)
        urls = df['URL'].tolist()
        for i, url in enumerate(urls):
            file_name = f"twittervid{i}.mp4"
            self.download_twitter_video(url, file_name)

    def download_twitter_video(self, twitter_url, file_name):
        output_path = os.path.join(self.output_directory, file_name)
        command = f"python F:/Meta/Github/twitter-video-dl/video-dl.py {twitter_url} {output_path}"
        os.system(command)


### test
fetch_twitter_url = FetchTweets()
fetch_twitter_url.get_tweets_from_search('I was diagnosed with ADHD since:2023-06-10 until:2023-06-19')
fetch_twitter_url.get_df_from_search(3000)
#twitter_video_download = TwitterVideoDownload('D:/Twitter_videos')
#twitter_video_download.download_videos_from_csv('F:/Meta/Twitter/user.csv')
