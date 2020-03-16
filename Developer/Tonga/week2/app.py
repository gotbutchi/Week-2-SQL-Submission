from bs4 import BeautifulSoup
from flask import Flask, render_template, url_for, request, redirect

import requests
import sqlite3
import re

app = Flask(__name__)
app.config.from_pyfile('config.cfg')

BASE_URL = 'https://tiki.vn/'

def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 