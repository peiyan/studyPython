import random
from flask import Blueprint, render_template
from App.ext import db
from App.models import Person,Student

blue = Blueprint('blue', __name__)

def init_blue(app):
    app.register_blueprint(blueprint=blue)

@blue.route('/')
def index():
    return render_template('index.html')


@blue.route('/createtable/')
def createtable():
    db.create_all()

    return '创建表单成功'

@blue.route('/adddata/')
def adddata():
    person = Person()
    person.p_name = '隔壁老王-%d' % random.randrange(1000)
    person.p_age = random.randrange(100)

    db.session.add(person)
    db.session.commit()

    return '创建: %s' % person.p_name

@blue.route('/showdata/')
def showdata():
    persons = Person.query.all()

    return render_template('showdata.html', persons=persons)

