from flask import render_template, request, redirect, url_for, Blueprint, flash
from flask_login import login_required, current_user
from gamedream import db
from gamedream.models import Wishlist, Titles, User

main = Blueprint('main', __name__)

@main.route("/")
def home():
    return render_template("index.html")

@main.route("/profile")
@login_required
def profile():
    return render_template("profile.html", name=current_user.name)

@main.route("/title")
def title():
    titles = list(Titles.query.order_by(Titles.id).all())
    users = list(User.query.order_by(User.id).all())
    return render_template("title.html", titles=titles, users=users)

@main.route("/wishlist")
def wishlist():
    wishlists = list(Wishlist.query.order_by(Wishlist.id).all())
    titles = list(Titles.query.order_by(Titles.game_title).all())
    users = list(User.query.order_by(User.id).all())
    return render_template("wishlist.html", wishlists=wishlists, titles=titles, users=users)

@main.route("/add_title", methods=["GET", "POST"])
@login_required
def add_title():
    if request.method == "POST":
        title = Titles(
            game_title = request.form.get("game_title"),
            publisher = request.form.get("publisher"),
            developer = request.form.get("developer"),
            price = request.form.get("price"),
            genre = request.form.get("genre"),
            description = request.form.get("description"),
            author_id = current_user.id
        )
        db.session.add(title)
        db.session.commit()
        return redirect(url_for("main.home"))
    return render_template("add_title.html", name=current_user.name)

@main.route("/edit_title/<int:title_id>", methods=["GET", "POST"])
@login_required
def edit_title(title_id):
    title = Titles.query.get_or_404(title_id)
    if title.author_id == current_user.id: 
        if request.method == "POST":
                title.game_title = request.form.get("game_title"),
                title.publisher = request.form.get("publisher"),
                title.developer = request.form.get("developer"),
                title.price = request.form.get("price"),
                title.genre = request.form.get("genre"),
                title.description = request.form.get("description")
                db.session.commit()
                return redirect(url_for("main.home"))
    else:
            flash('You are not authorized to change this title')
            return redirect(url_for('main.title'))
    return render_template("edit_title.html", title=title, name=current_user.name)

@main.route("/delete_title/<int:title_id>", methods=["GET","POST"])
@login_required
def delete_title(title_id):
    title = Titles.query.get_or_404(title_id)
    if title.author_id == current_user.id:
        db.session.delete(title)
        db.session.commit()
        return redirect(url_for("main.home"))
    else:
        flash('You are not authorized to change this title')
        return redirect(url_for('main.title'))
    return redirect(url_for("main.title"), name=current_user.name)

@main.route("/add_wishlist", methods={"GET","POST"})
@login_required
def add_wishlist():
    titles = list(Titles.query.order_by(Titles.game_title).all())
    if request.method == "POST":
        wishlist = Wishlist(
            wishlist_name = request.form.get("wishlist_name"),
            title_id = request.form.get("title_id"),
            author_id = current_user.id
        )
        db.session.add(wishlist)
        db.session.commit()
        return redirect(url_for("main.home"))
    return render_template("add_wishlist.html", titles=titles, name=current_user.name)

@main.route("/edit_wishlist/<int:wishlist_id>", methods=["GET","POST"])
@login_required
def edit_wishlist(wishlist_id):
    titles = list(Titles.query.order_by(Titles.game_title).all())
    wishlist = Wishlist.query.get_or_404(wishlist_id)
    if wishlist.author_id == current_user.id: 
        if request.method == "POST":
            wishlist.wishlist_name = request.form.get("wishlist_name"),
            wishlist.title_id = request.form.get("title_id")
            db.session.commit()
            return redirect(url_for("main.wishlist"))
    else:
        flash('You are not authorized to change this wishlist')
        return redirect(url_for('main.wishlist'))
    
    return render_template("edit_wishlist.html", wishlist=wishlist, titles=titles, name=current_user.name)

@main.route("/delete_wishlist/<int:wishlist_id>", methods=["GET","POST"])
@login_required
def delete_wishlist(wishlist_id):
    wishlist = Wishlist.query.get_or_404(wishlist_id)
    if wishlist.author_id == current_user.id:
        db.session.delete(wishlist)
        db.session.commit()
        return redirect(url_for("main.home"))
    else:
        flash('You are not authorized to change this wishlist')
        return redirect(url_for('main.wishlist'))
    return redirect(url_for("main.wishlist"), name=current_user.name)