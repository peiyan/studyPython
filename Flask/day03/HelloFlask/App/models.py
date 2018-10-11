from App.ext import db

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    p_name = db.Column(db.String(30))
    p_age = db.Column(db.Integer)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    s_name = db.Column(db.String(30))
    s_age = db.Column(db.Integer)