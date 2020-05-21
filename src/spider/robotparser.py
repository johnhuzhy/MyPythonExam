import urllib.robotparser as urobot
import wad.detection as wd
import requests

URL = "https://www.taobao.com/"


def robot_parser(URL):
    """
    RobotFileParser
    """
    rp = urobot.RobotFileParser()
    rp.set_url(URL + "/robots.txt")
    rp.read()
    user_agent = 'EtaoSpider'
    if rp.can_fetch(user_agent, "https://www.taobao.com/product/"):
        site = requests.get(URL)
        print('product sems good')
    elif rp.can_fetch(user_agent, "https://www.taobao.com/article/"):
        site = requests.get(URL)
        print('article sems good')
    else:
        print('Cannot scrap because robots.txt banned you.')


def wad_det(URL):
    """
    wad.detection
    """
    det = wd.Detector()
    print(det.detect(URL))


if __name__ == "__main__":
    robot_parser(URL)
    wad_det('http://www.12306.cn')
