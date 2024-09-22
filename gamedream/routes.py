from flask import render_template, request, redirect, url_for
from gamedream import app, db
from gamedream.models import Wishlist, Titles

@app.route("/")
def home():
    return render_template("title.html")

@app.route("/wishlist")
def wishlist():
    return render_template("wishlist.html")

@app.route("/add_title", methods=["GET", "POST"])
def add_title():
    if request.method == "POST":
        title = Titles(
            game_title = request.form.get("game_title"),
            publisher = request.form.get("publisher"),
            developer = request.form.get("developer"),
            price = request.form.get("price"),
            genre = request.form.get("genre"),
            description = request.form.get("description")
        )
        db.session.add(title)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add_title.html")

@app.route("/edit_title/<int:title_id>", methods=["GET", "POST"])
def edit_title():
    title = Titles.query.get_or_404("title_id")
    if request.method == "POST":
            title.game_title = request.form.get("game_title"),
            title.publisher = request.form.get("publisher"),
            title.developer = request.form.get("developer"),
            title.price = request.form.get("price"),
            title.genre = request.form.get("genre"),
            title.description = request.form.get("description")
            db.session.commit()
    return render_template("add_title.html", title=title)