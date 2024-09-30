from flask import render_template, request, redirect, url_for, Blueprint
from gamedream import app, db
from gamedream.models import Wishlist, Titles

auth = Blueprint('auth', __name__)

@app.route("/login")
def login():
    return 'Login'

@app.route("/signup")
def signup():
    return render_template("create_account.html")

@app.route("/logout")
def logout():
    return 'Logout'