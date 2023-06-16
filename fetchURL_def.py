import pandas as pd
import snscrape.modules.twitter as sntwitter
import os


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
fetch_twitter_url = FetchTwitterUrl('from:elonmusk since:2023-06-01 until:2023-06-16', 100000)
fetch_twitter_url.get_tweets()
fetch_twitter_url.get_df()
fetch_twitter_url.get_csv()
#twitter_video_download = TwitterVideoDownload('D:/Twitter_videos')
#twitter_video_download.download_videos_from_csv('F:/Meta/Twitter/user.csv')
