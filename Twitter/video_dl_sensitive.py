import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

class TwitterVideoDownload_Sensitive:
    def __init__(self):
        self.options = Options()
        self.options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)
        self.driver.get('https://ssstwitter.com/')

    def check_if_video_exists(self, url):
        url_input = self.driver.find_element(By.ID, 'main_page_text')
        url_input.send_keys(url)
        url_input.send_keys(Keys.ENTER)
        time.sleep(4)
        try:
            return_button = self.driver.find_element(By.LINK_TEXT, 'OK, I got it')
            return_button.click()
        except NoSuchElementException:
            print(url + ', please try manually.')
                     

    def download_single_video(self, url):
        url_input = self.driver.find_element(By.ID, 'main_page_text')
        url_input.send_keys(url)
        url_input.send_keys(Keys.ENTER)
        time.sleep(4)  # Add a delay to ensure the page has loaded completely
        try:
            download_button_hd = self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Download HD')
        except:
            try:
                download_button_hd = self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Download HD 19')
            except:
                try:
                    download_button_hd = self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Download HD 12')
                except:
                    try:
                        download_button_hd = self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Download 7')
                    except:
                        try:
                            download_button_hd = self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Download 5')
                        except:
                            try:
                                download_button_hd = self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Download 4')
                            except:
                                try:
                                    download_button_hd = self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Download 3')
                                except NoSuchElementException:
                                    print(url + ', please try manually.')
        download_button_hd.click()
        self.driver.quit()

    def download_videos_from_list(self, url_list):
        for url in url_list:
            self.download_single_video(url)

    def close(self):
        self.driver.quit()

if __name__ == '__main__':
    #url_list = ['https://twitter.com/retsu_dao/status/1667490569877348353']
    #twitter_video_download = TwitterVideoDownload_Sensitive()
    #twitter_video_download.download_videos_from_list(url_list)
    #twitter_video_download.close()
    #check test
    url = 'https://twitter.com/QiaoBaby3/status/1532981762447462401'
    twitter_video_download = TwitterVideoDownload_Sensitive()
    twitter_video_download.check_if_video_exists(url)
