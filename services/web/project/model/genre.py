from .. import db
from flask_sqlalchemy import SQLAlchemy

class Genre(db.Model):
    __tablename__ = 'Genre'

    id = db.Column(db.integer, primary_key=True)
    genre_id = db.relationshop('genre_id' , backref='genre' )
    genre = db.Column(db.String(100), nullable=False, unique=True)

    def __init__(self, genre_id,genre):
        self.genre_id = genre_id
        self.genre = genre


db.create_all()
db.session.commit()