from gamedream import db
from flask_login import UserMixin

wishlist_titles = db.Table("wishlist_titles",
                           db.Column('game_wishlist_id', db.Integer, db.ForeignKey('wishlist.id')),
                           db.Column('game_title_id', db.Integer, db.ForeignKey('titles.id')))

class Wishlist(db.Model):
    # schema for the Wishlist model
    id = db.Column(db.Integer, primary_key=True)
    wishlist_name = db.Column(db.String(30), unique=True, nullable=False)
    title_id = db.Column(db.Integer, db.ForeignKey("titles.id", ondelete="CASCADE"), nullable=True)
    game_title = db.Relationship('Titles', secondary=wishlist_titles, backref='game_wishlists')
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    
    def __repr__(self):
        return self.wishlist_name

class Titles(db.Model):
    # schema for the Task model
    id = db.Column(db.Integer, primary_key=True)
    game_title = db.Column(db.String, unique=True, nullable=False)
    publisher = db.Column(db.String, nullable=False)
    developer = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    genre = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=False)
    wishlists = db.Relationship("Wishlist", backref="game_titles", cascade="all, delete", lazy=True)
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    
    def __repr__(self):
        return "#{0} - Name: {1} - Price: {2}". format(
            self.id, self.game_title, self.price
        )

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password =  db.Column(db.String(200), nullable=False)
    title = db.Relationship('Titles', backref='user')
    wishlist = db.Relationship('Wishlist', backref='account')
    
    def __repr__(self):
        return "#{0} - Email: {1} - Password: {2}". format(
            self.id, self.email, self.password
        )