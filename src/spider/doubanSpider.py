from urllib import request
import re


class Spider():
    """♠主に教材と同じように練習する♠"""
    url = 'https://market.douban.com/book/?utm_campaign=book_nav_freyr&utm_source=douban&utm_medium=pc_web'
    item_path = '<li class="book-item">([\s\S]*?)</li>'
    price_path ='<i>([\d|\.]*?)</i>'
    name_path = '<h3>([\w\W]*?)</h3>'

    def __fetch_content(self):
        res = request.urlopen(Spider.url)
        htm = res.read()
        ht = str(htm, encoding='UTF-8')
        return ht

    def __analysis(self, ht):
        item_html = re.findall(Spider.item_path, ht)
        for ih in item_html:
            name = re.findall(Spider.name_path, ih)
            price = re.findall(Spider.price_path, ih)
            print(name, "⇒", price)

    def go(self):
        ht = self.__fetch_content()
        self.__analysis(ht)


if __name__ == "__main__":
    spider = Spider()
    spider.go()
