from App.ext import db


class Goods(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    g_name = db.Column(db.String(30))
    g_price = db.Column(db.Float)
    g_img = db.Column(db.String(30), default='/static/img/head.png')
    isdelete = db.Column(db.Boolean, default=False)


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    p_name = db.Column(db.String(30))


# 10个班级
# 每个班级1000个学生信息


# 10 * 1000 = 1W个学生

# 普通方式
# 显示班级: 将每个班级的学生都加载进来 (1W)

# 懒加载
# 只班级,当点击查看班级的学生信息时,才加载对应班级学生信息


# 班级
class Grade(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    g_name = db.Column(db.String(30))
    isdelete = db.Column(db.Boolean, default=False)

    # 班级对应的学生 (不会在表单中生成)
    # lazy 懒加载
    # db.relationship('声明级数据', backref='表明', lazy=True)
    g_students = db.relationship('Student', backref='grade', lazy=True)


# 学生
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    s_name = db.Column(db.String(30))
    s_score = db.Column(db.Integer)
    s_detail = db.Column(db.String(50))
    isdelete = db.Column(db.Boolean, default=False)

    # 外键 (班级的id)
    s_grade = db.Column(db.Integer, db.ForeignKey(Grade.id))
