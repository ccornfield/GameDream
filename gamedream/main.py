from flask import render_template, request, redirect, url_for, Blueprint, flash
from flask_login import login_required, current_user
from gamedream import db
from gamedream.models import Wishlist, Title, User

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
    titles = list(Title.query.order_by(Title.id).all())
    users = list(User.query.order_by(User.id).all())
    return render_template("title.html", titles=titles, users=users)

@main.route("/wishlist")
def wishlist():
    
    wishlists = list(Wishlist.query.order_by(Wishlist.id).all())
    titles = Title.query.all()
    users = list(User.query.order_by(User.id).all())
        
    return render_template("wishlist.html", wishlists=wishlists, titles=titles, users=users)

@main.route("/add_title", methods=["GET", "POST"])
@login_required
def add_title():
    if request.method == "POST":
        title = Title(
            game_title = request.form.get("game_title"),
            publisher = request.form.get("publisher"),
            developer = request.form.get("developer"),
            price = request.form.get("price"),
            genre = request.form.get("genre"),
            description = request.form.get("description"),
            author_id = current_user.id
        )
        db.session.add(title)
        flash('Title added successfully!')
        db.session.commit()
        return redirect(url_for("main.title"))
    return render_template("add_title.html", name=current_user.name)

@main.route("/edit_title/<int:title_id>", methods=["GET", "POST"])
@login_required
def edit_title(title_id):
    title = Title.query.get_or_404(title_id)
    if title.author_id != current_user.id: 
        flash('You are not authorized to change this title')
        return redirect(url_for('main.title'))
    
    if request.method == "POST":
            title.game_title = request.form.get("game_title"),
            title.publisher = request.form.get("publisher"),
            title.developer = request.form.get("developer"),
            title.price = request.form.get("price"),
            title.genre = request.form.get("genre"),
            title.description = request.form.get("description")
            flash('Title edited successfully!')
            db.session.commit()
            return redirect(url_for("main.title"))
        
    return render_template("edit_title.html", title=title, name=current_user.name)

@main.route("/delete_title/<int:title_id>", methods=["GET","POST"])
@login_required
def delete_title(title_id):
    title = Title.query.get_or_404(title_id)
    if title.author_id != current_user.id:
        flash('You are not authorized to change this title')
        return redirect(url_for('main.title'))
    
    db.session.delete(title)
    flash('Title deleted successfully!')
    db.session.commit()
    
    return redirect(url_for("main.title"))

@main.route("/add_wishlist", methods={"GET","POST"})
@login_required
def add_wishlist():
    all_titles = Title.query.all()
    if request.method == "POST":
        wishlist_name = request.form["wishlist_name"]
        selected_title_ids = request.form.getlist("titles[]")
        
        wishlist = Wishlist(wishlist_name=wishlist_name, author_id=current_user.id)
        
        titles = Title.query.filter(Title.id.in_(selected_title_ids)).all()
        wishlist.titles.extend(titles)
        
        db.session.add(wishlist)
        flash('Wishlist added successfully!')
        db.session.commit()
        return redirect(url_for("main.wishlist"))
    return render_template("add_wishlist.html", all_titles=all_titles, name=current_user.name)

@main.route("/edit_wishlist/<int:wishlist_id>", methods=["GET","POST"])
@login_required
def edit_wishlist(wishlist_id):
    all_titles = Title.query.all()
    wishlist = Wishlist.query.get_or_404(wishlist_id)
    if wishlist.author_id != current_user.id: 
        flash('You are not authorized to change this wishlist')
        return redirect(url_for('main.wishlist'))
    
    if request.method == "POST":
        wishlist.wishlist_name = request.form["wishlist_name"]
        
        selected_title_ids = request.form.getlist("titles[]")
        selected_titles = Title.query.filter(Title.id.in_(selected_title_ids)).all()
        
        wishlist.titles.clear()
        wishlist.titles = selected_titles
        
        db.session.commit()
        
        flash('Wishlist edited successfully!')
        return redirect(url_for("main.wishlist"))

    return render_template("edit_wishlist.html", wishlist=wishlist, all_titles=all_titles)

@main.route("/delete_wishlist/<int:wishlist_id>", methods=["GET","POST"])
@login_required
def delete_wishlist(wishlist_id):
    wishlist = Wishlist.query.get_or_404(wishlist_id)
    if wishlist.author_id != current_user.id:
        flash('You are not authorized to change this wishlist')
        return redirect(url_for('main.wishlist'))
    
    db.session.delete(wishlist)
    flash('Wishlist deleted successfully!')
    db.session.commit()
    
    return redirect(url_for("main.wishlist"))