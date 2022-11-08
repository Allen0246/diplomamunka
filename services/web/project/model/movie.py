from sqlalchemy import ForeignKey
from .. import db
from flask_sqlalchemy import SQLAlchemy

class Movie(db.Model):
    __tablename__ = 'movie'

    id = db.Column(db.Integer, primary_key=True)
    movieid = db.Column(db.Integer, nullable=False, unique=True)
    title = db.Column(db.String(100), nullable=False, unique=True)


    def __init__(self,title,genre_id):
        self.title = title
        self.genre_id = genre_id

db.create_all()
db.session.commit()