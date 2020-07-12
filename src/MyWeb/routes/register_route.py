from flask import Flask, render_template, Blueprint, redirect, url_for, request

app = Blueprint('register', __name__)


@app.route('/register_input', methods=['get', 'post'])
def register_input():
    return render_template('register_input.html')


@app.route('/register', methods=['get', 'post'])
def register():
    if request.method == 'POST':
        print(request.form)
        if request.form.get('Exec') == '会員登録':
            return render_template("top.html")
        elif request.form.get('Back') == '戻\u3000る':
            return redirect(url_for('home'))
        else:
            print('入力エラー')
            return redirect(url_for('home'))
    else:
        return render_template('register_input.html')
