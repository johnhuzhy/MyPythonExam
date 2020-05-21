import lxml.html
import requests

url = 'https://www.python.org/dev/peps/pep-0020/'
xpath = '//*[@id="the-zen-of-python"]/pre/text()'
if __name__ == "__main__":
    res = requests.get(url)
    ht = lxml.html.fromstring(res.text)
    print(ht)
    text = ht.xpath(xpath)
    print('Hello, Python!', ''.join(text))
