from flask import Flask, render_template, Blueprint, redirect, url_for

app = Blueprint('register', __name__)


@app.route('/register_input', methods=['get', 'post'])
def register_input():
    return render_template('register_input.html')


@app.route('/register_back', methods=['get', 'post'])
def register_back():
    return redirect(url_for('home'))
