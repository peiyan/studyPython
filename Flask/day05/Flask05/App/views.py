from flask import Blueprint, render_template, request
from App.models import *

blue = Blueprint('blue', __name__)

def init_blue(app):
    app.register_blueprint(blue)



# 手动分页
# @blue.route('/<int:num>/<int:per>')
# def index(num,per):
#     # 1, 5  ==>  0,5
#     # 2, 5  ==>  1,5
#     # 3, 5  ==>  2,5
#     goodslist = Goods.query.offset((num-1)*per).limit(per)
#
#     return render_template('index1.html', goodslist=goodslist)



# flask自带
# @blue.route('/<int:num>/<int:per>')
# def index(num,per):
#     paginate = Goods.query.paginate(num,per)
#
#     # iter_pages
#     # 假设有100页
#     # 当前30
#     # 1,2,None,28,29,30,31,32,33,34,None,98,99,100
#
#     return render_template('index2.html', paginate=paginate)



# flask自带,宏定义处理页码
# 请求方式要改为get
# @blue.route('/')
# def index():
#     page = int(request.args.get('page'))
#     paginate = Goods.query.paginate(page,5)
#
#     return render_template('index3.html', paginate=paginate)



# flask自带,宏定义处理页码
# 请求方式要改为get
@blue.route('/')
def index():
    page = int(request.args.get('page'))
    paginate = Goods.query.paginate(page,5)

    return render_template('index4.html', paginate=paginate)