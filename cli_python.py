import os
import pandas as pd

def download_twitter_video(twitter_url, file_name):
    output_directory = "D:/Twitter_videos"  # Specify the desired output directory path
    output_path = os.path.join(output_directory, file_name)
    command = f"python F:/Meta/Github/twitter-video-dl/video-dl.py {twitter_url} {output_path}"
    os.system(command)

# Example usage
df = pd.read_csv('F:/Meta/Twitter/whyyoutouzhele.csv')
urls = df['URL'].tolist()
for i in range(len(urls)):
    download_twitter_video(urls[i], 'twittervid'+str(i)+'.mp4')