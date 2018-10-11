import random

from flask import Blueprint, render_template
from App.models import *

blue = Blueprint('blue', __name__)

def init_blue(app):
    app.register_blueprint(blueprint=blue)


# 首页
@blue.route('/')
def hello_world():
    return render_template('index.html')


# 创建表单
@blue.route('/addtable/')
def addtable():
    db.create_all()

    return '创建表单成功'


# 删除表单
@blue.route('/deletetable/')
def deletetable():
    db.drop_all()

    return '删除表单成功'

# 添加商品
@blue.route('/addgoods/')
def addgoods():
    goods = Goods()
    goods.g_name = 'iPhone X-%d' % random.randrange(1000)
    goods.g_price = random.randrange(10000)

    db.session.add(goods)
    db.session.commit()

    return '添加商品: %s' % goods.g_name

# 显示商品
@blue.route('/showgoods/')
def showgoods():
    # 获取所有
    goods = Goods.query.all()

    # 模型类.query.all()
    # 模型类.query.filter(模型类.属性 运算符 值)
    # 价格大于5000
    # goods = Goods.query.filter(Goods.g_price > 5000)
    # goods = Goods.query.filter(Goods.id == 3)

    # 价格以3开头的
    # goods = Goods.query.filter(Goods.g_price.startswith('3'))

    # 商品以6结尾
    # goods = Goods.query.filter(Goods.g_name.endswith('6'))

    # 价格中包含8
    # goods = Goods.query.filter(Goods.g_price.contains('8'))

    # 在[xx,xx,xx]其中一个
    # goods = Goods.query.filter(Goods.id.in_([1,3,5,7,9]))

    # 限制个数
    # goods = Goods.query.limit(5)
    # goods = Goods.query.filter(Goods.id>5).limit(3)

    # 多个条件
    # goods = Goods.query.filter(Goods.id>5).filter(Goods.g_price.contains('3'))

    # 排序
    # goods = Goods.query.order_by(-Goods.g_price)
    # goods = Goods.query.order_by('-id') # 不是特别推荐
    # goods = Goods.query.order_by('price')

    # 偏移
    # goods = Goods.query.offset(3)

    # 每一页3个数据
    # goods = Goods.query.offset(0*3).limit(3)  # 第一页
    # goods = Goods.query.offset(1*3).limit(3)  # 第二页
    # goods = Goods.query.offset(2*3).limit(3)    # 第三页


    # limit都是最后执行!!!
    # goods = Goods.query.order_by('-id').limit(5).offset(5)
    # goods = Goods.query.order_by('-id').offset(5).limit(5)


    # goods = Goods.query.limit(3).order_by('-id')

    return render_template('showgoods.html', goods=goods)



# 显示单个商品
@blue.route('/goods/')
def goods():
    # 单个数据
    # goods = Goods.query.first()

    # goods = Goods.query.order_by(-Goods.id).first()

    # 获取的是主键
    # goods = Goods.query.get(3)

    return render_template('goods.html', goods=goods)


# 添加班级
@blue.route('/addgrade/')
def addgrade():
    grade = Grade()
    temp = random.randrange(1,6)
    if temp == 1:
        str = 'Python'
    elif temp == 2:
        str ='Java'
    elif temp == 3:
        str = 'Web'
    elif temp == 4:
        str = 'Android'
    elif temp == 5:
        str = 'iOS'
    else:
        str = '软件测试'

    # python1805
    grade.g_name = '{}18{}'.format(str,random.randrange(10,100))

    db.session.add(grade)
    db.session.commit()

    return '添加班级: %s' % grade.g_name

# 显示班级
@blue.route('/showgrade/')
def showgrade():
    grades = Grade.query.all()

    return render_template('showgrade.html', grades=grades)

# 显示班级对应的学生
@blue.route('/getstudents/<int:gradeid>/')
def getstudents(gradeid):
    # 方式一: 直接过滤
    # students = Student.query.filter(Student.s_grade == gradeid)
    # return render_template('showstudent.html', students=students)

    # 方式二: 级联方式
    grade = Grade.query.get(gradeid)

    return render_template('showstudent.html', students=grade.g_students)

# 添加学生
@blue.route('/addstudent/')
def addstudent():
    student = Student()
    student.s_name = '王总-%d' % random.randrange(1000)
    student.s_score = random.randrange(1000)
    student.s_detail = '%d-我住隔壁,我姓王,你有事情,我帮忙! 好人一生平安!' % random.randrange(1000)

    # 添加到最后的班级中
    grade = Grade.query.order_by(-Grade.id).first()
    student.s_grade = grade.id

    db.session.add(student)
    db.session.commit()

    return '添加学生: %s' % student.s_name

# 显示学生
@blue.route('/showstudent/')
def showstudent():
    students = Student.query.all()

    return render_template('showstudent.html',students=students)


# 更新学生信息
@blue.route('/updatestudent/')
def updatestudent():
    student = Student.query.order_by(-Student.id).first()
    student.s_name = '测试-%d' % random.randrange(1000)

    db.session.add(student)
    db.session.commit()

    return '更新学生信息成功'


# 删除学生信息
@blue.route('/deletestudent/')
def deletestudent():
    student = Student.query.order_by(-Student.id).first()

    db.session.delete(student)
    db.session.commit()

    return '删除学生成功'
