from flask import Blueprint, render_template, request, abort, g, redirect, url_for, session, jsonify
from flask_restful import Resource

from App.ext import cache, api
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
# @cache.cached(timeout=20)
def index():
    print('################ 首页 ################')
    page = int(request.args.get('page') or 1)
    paginate = Goods.query.paginate(page,5)

    # 获取用户对象
    # userid = session.get('userid')
    # if userid:
    #     user = User.query.get(userid)
    # else:
    #     user = None
    # return render_template('index4.html', paginate=paginate, user=user)

    return render_template('index4.html', paginate=paginate, user=g.user)

# 请求钩子 --- 应用1,简单的反爬
# @blue.before_request()
# @blue.before_app_first_request()
# @blue.after_request()

# @blue.before_request
# def before_request():
#     print('请求之前!!!');
#
#     # 获取IP 【key】
#     key = 'before:' + request.remote_addr
#
#     # 从缓存中获取数据
#     value = cache.get(key)
#
#     if value: # 缓存中有数据
#         # return '小伙子，你有点过了哈。 '
#         abort(404)
#     else:   # 缓存中没有数据
#         cache.set(key, '我是害虫!', timeout=5)


# 请求钩子 -- flask内置对象
# g -- global
# @blue.before_request
# def before_request():
#     # 将要传递的数据,放置在全局变量g中
#     g.name = '张三'
#     g.age = 18
#     g.score = 90
#
#
# @blue.route('/test/')
# def test():
#     print(g.name)
#     print(g.age)
#     print(g.score)
#     return render_template('test.html')


# 请求钩子 -- 请求钩子和视图之间的数据共享 【例如: 登录信息】
# 钩子 + g的结合使用
@blue.before_request
def before_request():
    userid = session.get('userid')
    if userid:
        user = User.query.get(userid)
    else:
        user = None

    g.user = user

# 注册
@blue.route('/register/', methods=['POST'])
def register():
    user = User()
    user.u_email = request.form.get('email')
    user.u_name = request.form.get('username')
    user.u_password = request.form.get('password')

    try:
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        return '用户邮箱已存在'

    # session
    session['userid'] = user.id

    return redirect(url_for('blue.index'))

# 退出
@blue.route('/quit/')
def quit():
    session.pop('userid')

    return redirect(url_for('blue.index'))

# 登录
@blue.route('/login/', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    users = User.query.filter(User.u_email == email).filter(User.u_password == password)
    if users.count():
        user = users.first()
        # 设置session
        session['userid'] = user.id

        return redirect(url_for('blue.index'))
    else:
        return '账号或密码错误'


# 关于我们
@blue.route('/about/')
def about():
    # userid = session.get('userid')
    # if userid:
    #     user = User.query.get(userid)
    # else:
    #     user = None
    # return render_template('about.html', user=user)

    return render_template('about.html', user=g.user)

# 购物车
@blue.route('/cart/')
def cart():
    # userid = session.get('userid')
    # if userid:
    #     user = User.query.get(userid)
    # else:
    #     user = None
    # return render_template('cart.html', user=user)

    return render_template('cart.html', user=g.user)





##########################  返回json数据  ##########################
@blue.route('/getjson/')
def getjson():
    datadir = {
        'status': 200,
        'msg': '获取数据成功',
        'data': 'hello world!'
    }

    return jsonify(datadir)




##########################  前后端分离初步体验  ##########################
@blue.route('/getscore/')
def getscore():
    datadir = {
        'status':200,
        'msg':'获取学生成绩单成功',
        'data': [100,21,56,89,54,89,92,39]
    }

    return jsonify(datadir)




##################################### RESTful #####################################
# https://www.douban.com
# https://www.douban.com/api/v1/test

# https://api.douban.com/v1/test


# REST 表现层状态转换
# 表现层 》》 资源

# 数据  增删改查   >>  get/post/put/delete
# 资源  状态改变


@blue.route('/api/v1/students/')
def students1():
    datadir = {
        'data' : ['张三','李四','王五']
    }
    return jsonify(datadir)


@blue.route('/api/v2/students/')
def students2():
    datadir = {
        'data': ['张三', '李四', '王五'],
        'status': 200,
        'msg': '获取数据成功',
        'error': ''
    }
    return jsonify(datadir)




##################################### RESTful 原生 #####################################
@blue.route('/api/v1/user/', methods=['POST','GET','PUT','DELETE'])
def user():
    if request.method == 'GET': # 获取用户
        userid = request.args.get('userid')

        datadir = {
            'status': 404,
            'msg': '获取用户失败',
            'data': ''
        }

        if userid:  # 有userid
            user = User.query.get(userid)

            if user:    # 有用户
                datadir['status'] = 200
                datadir['msg'] = '获取数据成功'
                datadir['data'] = {
                    'name': user.u_name,
                    'email': user.u_email
                }

            return jsonify(datadir)
        else:   # 无userid
            datadir['msg'] = '(get)需要提供userid参数'
            return jsonify(datadir)


    elif request.method == 'POST': # 创建用户
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')

        datadir = {
            'status': 400,
            'msg':'更新用户失败',
            'data': ''
        }

        # 不能未空
        if not username:
            datadir['msg'] = 'username用户名不能为空'
            return jsonify(datadir)

        if not password:
            datadir['msg'] = 'password密码不能为空'
            return jsonify(datadir)

        if not email:
            datadir['msg'] = 'email不能为空'
            return jsonify(datadir)

        # 添加
        user = User()
        user.u_name = username
        user.u_password = password
        user.u_email = email

        try:
            datadir['status'] = 200
            datadir['msg'] = '添加用户成功'
            datadir['data'] = {
                'name': user.u_name,
                'email': user.u_email
            }

            db.session.add(user)
            db.session.commit()
            return jsonify(datadir)
        except Exception as e:
            datadir['msg'] = '用户(email)已存在！'
            datadir['data'] = ''
            return  jsonify(datadir)

    elif request.method == 'DELETE':    # 删除用户
        pass
    elif request.method == 'PUT':   # 更新用户
        pass
    else:
        abort(404)


# datadir = {
#     'status':200,
#     'msg':'获取数据成功',
#     'data':[
#         {},
#         {},
#         {},
#         ...
#     ]
# }

# datadir = {
#     'status':200,
#     'msg':'获取数据成功',
#     'data': goodslist
# }


##################################### flask-restful插件 #####################################
# 定义资源
class HelloWorld(Resource):
    def get(self):
        return {'msg': '[get] hello world!'}

    def post(self):
        return {'msg': '[post] hello world!'}

# 添加资源
# api.add_resource(HelloWorld, '/api/v1/hello/')
api.add_resource(HelloWorld, '/api/v1/hello/', endpoint='hello')
