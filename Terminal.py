from gamedream import create_app

with app.app_context():
    db.create_all()

print("Database Updated!")