from App.ext import db


# class City(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     parentId = db.Column(db.Integer, default=0)
#     regionName = db.Column(db.String(50))
#     cityCode = db.Column(db.Integer)
#     pinYin = db.Column(db.String)
#     letter = db.Column(db.String(10))


# 一对多
# 一个字母对应多个城市
class Letter(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(3))
    # 对应的城市
    l_citys = db.relationship('City', backref='letter', lazy=True)

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    parentId = db.Column(db.Integer, default=0)
    regionName = db.Column(db.String(50))
    cityCode = db.Column(db.Integer)
    pinYin = db.Column(db.String(50))
    # 属于哪个字母[外键]
    c_letter = db.Column(db.Integer, db.ForeignKey(Letter.id))




# 用户模型类
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(255))
    email = db.Column(db.String(50), unique=True)
    phone = db.Column(db.String(20))
    icon = db.Column(db.String(30), default='head.png')
    token = db.Column(db.String(255))
    permission = db.Column(db.Integer, default=1)
    isactive = db.Column(db.Boolean, default=False)
    isdelete = db.Column(db.Boolean, default=False)




