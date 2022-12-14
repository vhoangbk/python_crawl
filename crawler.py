import logging
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

logging.basicConfig(
    format='%(asctime)s %(levelname)s:%(message)s',
    level=logging.INFO)

class Crawler:

    def __init__(self, url):
        self.url = url

    def download_url(self, url):
        return requests.get(url).text

    def download_image(self, image_url, name):
        print('{} downloading... '.format(name))
        img_data = requests.get(image_url).content
        with open('{}.jpg'.format(name), 'wb') as handler:
            handler.write(img_data)

    def get_new_feeds(self, url, html):
        soup = BeautifulSoup(html, 'html.parser')
        return soup.find(class_='kds-new-stream-wrapper').find(class_='knsw-list').find_all('li')

    def parser_new_feeds(self, new_feeds):
        for i,news in enumerate(new_feeds):
            title = news.find(class_='knswli-left fl').find('a').get('title')
            href = news.find('a').get('href')
            img = news.find('img').get('src')

            # print(i)
            # print(title)
            print(self.url + href)
            # print(img)

            # self.download_image(img, '{}'.format(i+1))

    

    def crawl(self, url):
        html = self.download_url(url)
        new_feeds = self.get_new_feeds(url, html)
        self.parser_new_feeds(new_feeds)

    def run(self):
        logging.info(f'Crawling: {self.url}')
        try:
            self.crawl(self.url)
        except Exception:
            logging.exception(f'Failed to crawl: {self.url}')

if __name__ == '__main__':
    Crawler(url = 'https://genk.vn').run()