from App.ext import db


class Dog(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(30))
    color = db.Column(db.String(30))



class Wheel(db.Model):
    __tablename__ = 'axf_wheel'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    img = db.Column(db.String(255))
    name = db.Column(db.String(50))
    trackid = db.Column(db.String(20))