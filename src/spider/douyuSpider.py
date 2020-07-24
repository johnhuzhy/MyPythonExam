from bs4 import BeautifulSoup
import pandas as pd
import requests
import datetime


class Spider():
    url = 'https://www.douyu.com/g_How'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"}

    def __fetch_content(self):
        try:
            res = requests.get(Spider.url, headers=Spider.headers)
        except requests.ConnectionError as e:
            print('Request Error!!!')
        soup = BeautifulSoup(res.text, 'lxml')
        return soup

    def __analysis(self, soup):
        anchors = soup.find_all('div', {'class': 'DyListCover-content'})
        self.titles = []
        self.names = []
        self.numbers = []
        for anchor in anchors:
            # title
            anchor_title = anchor.find(
                'h3', {'class': 'DyListCover-intro'}).get('title')
            self.titles.append(anchor_title)

            # name
            anchor_name = anchor.find(
                'h2', {'class': 'DyListCover-user'}).get_text()
            self.names.append(anchor_name)

            # number
            anchor_number = anchor.find(
                'span', {'class': 'DyListCover-hot'}).get_text()
            if '万' in anchor_number:
                temp = anchor_number[0:-1]
                anchor_number = float(temp) * 10000
            else:
                anchor_number = float(anchor_number)
            self.numbers.append(anchor_number)

    def conv_CSV(self, filename):
        self.result = pd.DataFrame()
        self.result['names'] = self.names
        self.result['titles'] = self.titles
        self.result['numbers'] = self.numbers
        self.result.to_csv(filename, index=None)

    def go(self):
        soup = self.__fetch_content()
        self.__analysis(soup)


if __name__ == "__main__":
    spider = Spider()
    spider.go()
    file_name = './prop/' + datetime.datetime.now().strftime('%Y%m%d%H%M') + 'dy.csv'
    print("Save Anchor Data ⇒", file_name)
    spider.conv_CSV(file_name)
