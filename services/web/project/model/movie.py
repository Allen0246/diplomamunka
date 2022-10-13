from .. import db


class Movie(db.Model):
    __tablename__ = 'moovie'

    moovieId = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, unique=True)


    def __init__(self, moovieId,title):
        self.moovieId = moovieId
        self.title = title


db.create_all()
db.session.commit()