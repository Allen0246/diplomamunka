from .. import db


class Movie(db.Model):
    __tablename__ = 'moovie'

    movieId = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, unique=True)


    def __init__(self, movieId,title):
        self.movieId = movieId
        self.title = title


db.create_all()
db.session.commit()