from .. import db
from flask_sqlalchemy import SQLAlchemy

movie_genre = db.table('movie_genre',
    db.Column('movie_id', db.Integer, db.ForeignKey('movie.id')),
    db.Column('genre_id', db.Integer, db.ForeignKey('genre.id'))
)

class Genre(db.Model):
    __tablename__ = 'genre'

    id = db.Column(db.Integer, primary_key=True)
    movies = db.relationship("Child", secondary=movie_genre, backref="genres") 
    genre = db.Column(db.String(100), nullable=False, unique=True)
 

    def __init__(self, genre_id,genre):
        self.genre_id = genre_id
        self.genre = genre


db.create_all()
db.session.commit()