# all the imports
import sqlite3
from flask import Flask, request, sessions, g, redirect, url_for, abort, render_template, flash

# configuration
DATABASE = 'db/flaskr.db'
DEBUG = True
SECURET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'admin'

# create our little application
app = Flask(__name__)
app.config.from_object(__name__)


# create db connection
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


if __name__ == '__main__':
    app.run()
