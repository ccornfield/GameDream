from gamedream import db

class Wishlist(db.Model):
    # schema for the Wishlist model
    id = db.Column(db.Integer, primary_key=True)
    wishlist_name = db.Column(db.String(30), unique=True, nullable=False)
    title_id = db.Column(db.Integer, db.ForeignKey("titles.id", ondelete="CASCADE"), nullable=True)
    
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
    wishlists = db.relationship("Wishlist", backref="titles", cascade="all, delete", lazy=True)
    
    def __repr__(self):
        return "#{0} - Name: {1} - Price: {2}". format(
            self.id, self.game_title, self.price
        )

# class Login(db.Model):
    # email =
    # password = 
    # user_id = random string