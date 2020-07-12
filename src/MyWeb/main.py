from flask import Flask
from flask import render_template
from flask import request
from routes import register_route

app = Flask(__name__)
app.register_blueprint(register_route.app)

@app.route('/')
@app.route('/home')
def home():
    """ログイン画面へ遷移"""
    return render_template("login.html", title='Login')


@app.route('/login', methods=['get', 'post'])
def login():
    """ログイン処理"""
    if request.method == 'POST':
        print(request.form['user'])
        return render_template("top.html")
    else:
        return render_template("login.html", title='Login')


@app.route('/top')
def top_page():
    """トップ画面へ遷移"""
    return render_template("top.html")
# app.add_url_rule('/top', view_func=top_page)

@app.route('/<name>', methods=['get'])
def name_page(name):
    return render_template("name.html", title='Name', name=name)


# 配置ファイルを読む
app.config.from_object('config')

if __name__ == "__main__":
    app.run(host=app.config['SERVER_HOST'],
            port=app.config['SERVER_PORT'],
            debug=app.config['DEBUG'])
