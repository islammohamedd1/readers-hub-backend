from ..db import db


class User(db.Model):
    uid = db.Column(db.String(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), unique=True, nullable=False)
    reviews = db.relationship('review', backref='user')
    progress = db.relationship('ReadingProgress', backref='user')
    challenges = db.relationship('ChallengeParticipants', backref='user')

    def insert(self):
        db.session.add(self)
        db.session.commit()