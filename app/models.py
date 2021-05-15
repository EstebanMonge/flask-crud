from app import db

class Person(db.Model):
    person_id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(64), index=True, nullable=False)
    lname = db.Column(db.String(64), index=True, nullable=False)
    email = db.Column(db.String(64), index=True, nullable=False)
    username = db.Column(db.String(64), index=True, nullable=False)
    is_active = db.Column(db.Boolean, default=False)
