from flask import render_template, request, redirect, url_for, Blueprint
from gamedream import app, db
from gamedream.models import Wishlist, Titles

main = Blueprint('main', __name__)

@main.route("/")
def home():
    return render_template("index.html")

@main.route("/profile")
def profile():
    return render_template("profile.html")

@main.route("/title")
def title():
    titles = list(Titles.query.order_by(Titles.id).all())
    return render_template("title.html", titles=titles)

@main.route("/wishlist")
def wishlist():
    wishlists = list(Wishlist.query.order_by(Wishlist.id).all())
    titles = list(Titles.query.order_by(Titles.game_title).all())
    return render_template("wishlist.html", wishlists=wishlists, titles=titles)

@main.route("/add_title", methods=["GET", "POST"])
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

@main.route("/edit_title/<int:title_id>", methods=["GET", "POST"])
def edit_title(title_id):
    title = Titles.query.get_or_404(title_id)
    if request.method == "POST":
            title.game_title = request.form.get("game_title"),
            title.publisher = request.form.get("publisher"),
            title.developer = request.form.get("developer"),
            title.price = request.form.get("price"),
            title.genre = request.form.get("genre"),
            title.description = request.form.get("description")
            db.session.commit()
            return redirect(url_for("home"))
    return render_template("edit_title.html", title=title)

@main.route("/delete_title/<int:title_id>", methods=["GET","POST"])
def delete_title(title_id):
    title = Titles.query.get_or_404(title_id)
    db.session.delete(title)
    db.session.commit()
    return redirect(url_for("home"))

@main.route("/add_wishlist", methods={"GET","POST"})
def add_wishlist():
    titles = list(Titles.query.order_by(Titles.game_title).all())
    if request.method == "POST":
        wishlist = Wishlist(
            wishlist_name = request.form.get("wishlist_name"),
            title_id = request.form.get("title_id")
        )
        db.session.add(wishlist)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add_wishlist.html", titles=titles)

@main.route("/edit_wishlist/<int:wishlist_id>", methods=["GET","POST"])
def edit_wishlist(wishlist_id):
    titles = list(Titles.query.order_by(Titles.game_title).all())
    wishlist = Wishlist.query.get_or_404(wishlist_id)
    if request.method == "POST":
        wishlist.wishlist_name = request.form.get("wishlist_name"),
        wishlist.title_id = request.form.get("title_id")
        db.session.commit()
        return redirect(url_for("wishlist"))
    return render_template("edit_wishlist.html", wishlist=wishlist, titles=titles)

@main.route("/delete_wishlist/<int:wishlist_id>", methods=["GET","POST"])
def delete_wishlist(wishlist_id):
    wishlist = Wishlist.query.get_or_404(wishlist_id)
    db.session.delete(wishlist)
    db.session.commit()
    return redirect(url_for("home"))