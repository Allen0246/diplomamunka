from .. import db


class Moovie(db.Model):
    __tablename__ = 'rating'

    userId = db.Column(db.Integer, primary_key=True)
    moovieid = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.String(100), nullable=False, unique=True)
    timestamp = db.Column(db.String(100), nullable=False, unique = True)


db.create_all()
db.session.commit()