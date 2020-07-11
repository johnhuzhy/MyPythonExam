from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

#ログイン画面
@app.route('/')
@app.route('/home')
def home():
    return render_template("login.html", title='Login')

@app.route('/login', methods=['get','post'])
def login():
    if request.method == 'POST':
        print(request.form['user'])
        return render_template("top.html")
    else:
        return render_template("login.html", title='Login')

# トップ画面
# app.add_url_rule('/top', view_func=top_page)
@app.route('/top')
def top_page():
    return render_template("top.html")

@app.route('/<name>', methods=['get'])
def name_page(name):
    return render_template("name.html", title='Name', name=name)


# 配置ファイルを読む
app.config.from_object('config')

if __name__ == "__main__":
    app.run(host='localhost', port=2345, debug=app.config['DEBUG'])
