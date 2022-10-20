from .. import db

class Genre(db.Model):
    __tablename__ = 'Genre'

    genre_id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True)
    genre = db.Column(db.String(100), nullable=False, unique=True)

    def __init__(self, genre_id,genre):
        self.genre_id = genre_id
        self.genre = genre

db.create_all()
db.session.commit()