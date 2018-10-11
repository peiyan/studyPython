from flask_sqlalchemy import SQLAlchemy   # 有些老版本的问题flask.ext.SQLAlchemy,现在基本没有了

db = SQLAlchemy()  # 哪里使用哪里创建

def init_db(app):
    db.init_app(app)


# 模型类
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    p_name = db.Column(db.String(30))
    p_age = db.Column(db.Integer)
