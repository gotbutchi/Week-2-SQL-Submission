from bs4 import BeautifulSoup
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import requests
import re

app = Flask(__name__)
app.config['TESTING'] = True

def get_url(URL):
    """Get HTML from URL
    """
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

db=sqlite3.connect('test.db')