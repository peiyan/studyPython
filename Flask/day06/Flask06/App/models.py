from App.ext import db

class Goods(db.Model):
    # 商品id，主键
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 商品名称
    name = db.Column(db.String(20))
    # 商品图片
    icon = db.Column(db.String(255))
    # 商品价格
    price = db.Column(db.Integer)
    # 商品描述
    detail = db.Column(db.String(255))



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    u_name = db.Column(db.String(30))
    u_password = db.Column(db.String(30))
    u_email = db.Column(db.String(30), unique=True)
    isdelete = db.Column(db.Boolean, default=False)
