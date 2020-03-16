from bs4 import BeautifulSoup
from flask import Flask, render_template, url_for, request, redirect, g

import requests
import sqlite3
import re

app = Flask(__name__)
app.config['TESTING'] = True

BASE_URL = 'https://tiki.vn/'

DATABASE = 'tiki.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/')
def index():
    conn = get_db()
    cur = conn.cursor()
    return render_template('index.html')

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 