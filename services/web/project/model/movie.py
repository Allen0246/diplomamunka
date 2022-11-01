from .. import db


class Movie(db.Model):
    __tablename__ = 'moovie'

    movieId = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, unique=True)
    genre_id = db.Column(db.Integer, nullable=False, unique=True)


    def __init__(self,title,genre_id):
        self.title = title
        self.genre_id = genre_id

db.create_all()
db.session.commit()