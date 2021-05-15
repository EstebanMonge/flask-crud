from app import db

class Person(db.Model):
    person_id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(64), index=True, nullable=False)
    lname = db.Column(db.String(64), index=True, nullable=False)
    email = db.Column(db.String(64), index=True, nullable=False)
    username = db.Column(db.String(64), index=True, nullable=False)
    is_active = db.Column(db.Boolean, default=False)
    role = db.Column(db.Integer, default=False)
    platform = db.Column(db.Integer, default=False)
    shift = db.Column(db.Integer, default=False)
    group = db.Column(db.Integer, default=False)

class Role(db.Model):
    role_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, nullable=False)

class Platform(db.Model):
    platform_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, nullable=False)

class Shift(db.Model):
    shift_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, nullable=False)
    start_hour = db.Column(db.Integer, default=False)
    end_hour = db.Column(db.Integer, default=False)
    sunday = db.Column(db.Boolean, default=False)
    monday = db.Column(db.Boolean, default=False)
    tuesday = db.Column(db.Boolean, default=False)
    wednesday = db.Column(db.Boolean, default=False)
    thursday = db.Column(db.Boolean, default=False)
    friday = db.Column(db.Boolean, default=False)
    saturday = db.Column(db.Boolean, default=False)

class Group(db.Model):
    group_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, nullable=False)
