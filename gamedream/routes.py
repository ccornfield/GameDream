from flask import render_template
from gamedream import app, db

@app.route("/")
def home():
    return render_template("base.html")

@app.route("/add_title")
def add_title():
    return render_template("add_title.html")