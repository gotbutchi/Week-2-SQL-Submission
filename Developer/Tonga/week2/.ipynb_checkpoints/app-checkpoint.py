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
    r = requests.get(URL)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db