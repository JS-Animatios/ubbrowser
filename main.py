import os
from flask import Flask
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import browser.py

app = Flask(__name__)
@app.route("/")
def browse():
        browser.__init__()
if __name__ == "__main__":
    app.run()