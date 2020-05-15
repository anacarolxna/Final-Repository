# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:57:17 2020

@author: etill
"""

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/favoriteartists")
def favart():
    return render_template("fav_art.html")

@app.route("/mysummer")
def summer():
    return render_template("my_summer.html")

#start the server
if __name__ == "__main__":
    app.run()