import requests
import urllib.request
from bs4 import BeautifulSoup

# 'Visual Studio Code' 는 visual-studio-code
# 'Node.js' 는 Nodejs

class Crawling_Stack:
    def __init__(self, name):
        self.name = name
        self.img = None
        self.detail = None
        self.webpage = None
        self.category = None
        name=name.replace(" ","-")
        name=name.replace(".","")
        self.stackshareLink = f'https://stackshare.io/{name}'

    # 모든걸 크롤링하는 코드
    def crawling_all(self):
        responce = requests.get(self.stackshareLink)
        soup = BeautifulSoup(responce.text, 'html.parser')
        try:
            self.crawling_webpage(soup)
            self.crawling_img(soup)
            self.crawling_detail(soup)
            self.crawling_category(soup)
            return False
        except Exception as e:
            print(f'StackDB-error-occured-name : {e}')
            return True

    # 공식 페이지 크롤링
    def crawling_webpage(self, soup):
        self.webpage = soup.select(
            'div.css-mgyi0p > div.css-ii8qy4 > div > div > div > a'
        )[0].get('href')

    # 이미지를 크롤링
    def crawling_img(self, soup):
        imgSelect = soup.select(
            'img'
        )
        imgURL=imgSelect[0].get('src')
        urllib.request.urlretrieve(imgURL, f'media/icon/{self.name}.{imgURL.split(".")[-1]}')
        self.img = f'icon/{self.name}.{imgURL.split(".")[-1]}'

    # 상세 정보 크롤링
    def crawling_detail(self, soup):
        detailselect = soup.select(
            'div.css-mgyi0p > main > div > div > div:nth-child(1) > \
                div.css-1nbl3qb > div > div:nth-child(2)'
        )
        self.detail = detailselect[0].get_text('div')

    # 스택 카테코리 크롤링
    def crawling_category(self, soup):
        categoryselect = soup.select(
            'div.css-mgyi0p > main > div > div > div:nth-child(1) > \
                div.css-1nbl3qb > div > div:nth-child(3)> strong'
        )
        self.category=categoryselect[0].get_text('strong')