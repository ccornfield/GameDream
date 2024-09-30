from flask import render_template, request, redirect, url_for, Blueprint, flash
from werkzeug.security import generate_password_hash, check_password_hash
from gamedream import app, db
from gamedream.models import Wishlist, Titles, User

auth = Blueprint('auth', __name__)

@auth.route("/login")
def login():
    return render_template("login.html")

@auth.route("/signup")
def signup():
    return render_template("create_account.html")

@auth.route("/signup", methods=['POST'])
def signup_post():
    email = request.form.get('email')
    password = request.form.get('password')
    user = User.query.filter_by(email=email).first()
    
    if user: # if a user is found, we want to redirect back to signup page so user can try again
        return redirect(url_for('auth.signup'))
    
    new_user = User(email=email, password=generate_password_hash(password, method='scrypt'))
    
    db.session.add(new_user)
    db.session.commit()
    if user: # if a user is found, we want to redirect back to signup page so user can try again
        flash('Email address already exists')
    return redirect(url_for('auth.login'))

@auth.route("/logout")
def logout():
    return 'Logout'