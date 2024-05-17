from flask import Flask, send_from_directory
from flask import render_template

app = Flask(__name__)


@app.route('/static/css/<path:path>')
def send_css(path):
    return send_from_directory('static/css', path)


# main page
@app.route('/')
def hi_page():
    return render_template('index.html')