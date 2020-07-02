from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello Shanshan!'


def top_page():
    return render_template("top.html", title='Top')


# トップ画面
app.add_url_rule('/top', view_func=top_page)


@app.route('/<name>', methods=['get'])
def name_page(name):
    return render_template("name.html", title='Name', name=name)


# 配置ファイルを読む
app.config.from_object('config')

if __name__ == "__main__":
    app.run(host='localhost', port=2345, debug=app.config['DEBUG'])
