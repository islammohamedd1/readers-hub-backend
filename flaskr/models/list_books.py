from ..db import db


class ListBooks(db.Model):
    list_id = db.Column(db.ForeignKey('list.id'), primary_key=True)
    book_id = db.Column(db.ForeignKey('book.id'), primary_key=True)
    time_added = db.Column(db.DateTime(), nullable=False)

    def insert(self):
        db.session.add(self)
        db.session.commit()
