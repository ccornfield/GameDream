from flask import render_template
from gamedream import app, db
from gamedream.models import Wishlist, Titles

@app.route("/")
def home():
    return render_template("base.html")



@app.route("/add_title", methods=["GET", "POST"])
def add_title():
    if request.method == "POST":
        title = Titles(
            game_title = request.form.get("game_title"),
            publisher = request.form.get("publisher"),
            developer = request.form.get("developer"),
            price = request.form.get("price"),
            genre = request.form.get("genre"),
            platform = request.form.get("platform"),
            description = request.form.get("description")
        )
        db.session.add(title)
        db.session.commit()
        return redirect(url_for("home"))
        
    return render_template("base.html")