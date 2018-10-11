import random

from flask import Blueprint, render_template
from Meituan.models import Person, db

blue = Blueprint('blue',__name__)   # 实例蓝图是需要第二个参数的,不然报错



########################### 表单操作 ###########################
@blue.route('/')
def index():
    return render_template('index.html')


# 创建表单(sqlite会自动创建对应数据库)
@blue.route('/createtable/')
def createtable():
    db.create_all()

    return '创建表单成功'

# 添加数据
@blue.route('/adddata/')
def adddata():
    person = Person()
    person.p_name = '赵总-%d' % random.randrange(1000)
    person.p_age = random.randrange(100)

    # 存储到数据库
    db.session.add(person)
    db.session.commit()

    return '添加输入: %s' % person.p_name

# 查询数据
@blue.route('/showdata/')
def showdata():
    persons = Person.query.all()

    return render_template('showdata.html', persons=persons)