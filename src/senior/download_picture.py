# cooding=utf-8
import datetime
import requests


def get_picture(cache_dir='./prop/'):
    """
    衛星画像をダウンロードする
    """
    url_base = 'http://himawari8-dl.nict.go.jp/himawari8/img/D531106/1d/550/'
    date = datetime.datetime.utcnow().strftime('%Y/%m/%d/')
    hour = str(int(datetime.datetime.utcnow().strftime('%H')) - 1).zfill(2)
    minute = str(datetime.datetime.utcnow().strftime('%M'))[0] + '0'
    second = '00'
    ext = '_0_0.png'
    # URL
    picture_url = url_base + date + hour + minute + second + ext
    print("Download Picture URL⇒", picture_url)
    # 名前
    picture_name = cache_dir + datetime.datetime.utcnow().strftime('%Y%m%d%H%M') + '.png'
    print("Save Picture Name⇒", picture_name)
    # ダウンロード
    res = requests.get(picture_url)
    # ファイル書き込み
    try:
        with open(picture_name, 'wb') as f:
            f.write(res.content)
    except FileNotFoundError:
        print("ファイルは書き込まれない:", picture_name)
    finally:
        f.close()


if __name__ == "__main__":
    get_picture()
