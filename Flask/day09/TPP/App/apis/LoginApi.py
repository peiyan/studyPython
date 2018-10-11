import uuid

from flask import render_template
from flask_mail import Message
from flask_restful import fields,Resource,marshal_with,reqparse

# 请求格式定
from werkzeug.security import check_password_hash

from App.ext import mail, cache, db
from App.models import User

parser = reqparse.RequestParser()
parser.add_argument('username', type=str, required=True, help='请提供用户名username')
parser.add_argument('password', type=str, required=True, help='请提供密码password')


# 自定义字段
class UserIcon(fields.Raw):
    def format(self, value):
        return '/staitc/img/' + value


# 响应格式定制
user_fileds = {
    'name': fields.String,
    # 'icon': fields.String,
    'icon': UserIcon(attribute='icon'),
    'token': fields.String,
    'permission': fields.String
}

result_fileds = {
    'status': fields.Integer,
    'msg': fields.String,
    'err': fields.String(default=''),
    'data': fields.Nested(user_fileds, default='')
}


class Login(Resource):
    @marshal_with(result_fileds)
    def post(self):
        parse = parser.parse_args()
        username = parse.get('username')
        password = parse.get('password')

        users = User.query.filter(User.name == username)
        datadir = {}

        if users.count():   # 用户名存在
            # 用户
            user = users.first()

            # 校验密码
            # if user.password == password:   # 密码正确
            if check_password_hash(user.password, password):  # 密码正确
                if user.isdelete == True:   # 已删除
                    datadir['status'] = 401
                    datadir['msg'] = '登录失败'
                    datadir['err'] = '该用户已注销！'
                    return datadir

                if user.isactive == False:   # 未激活
                    datadir['status'] = 401
                    datadir['msg'] = '登录失败'
                    datadir['err'] = '用户未激活，请激活后登录！'

                    # 发送邮件
                    msg = Message('TPP激活邮件',
                                  sender='18924235915@163.com',
                                  recipients=[user.email])
                    action_url = 'http://127.0.0.1:5000/api/v1/action/?token=' + user.token
                    msg.html = render_template('useraction.html', name=user.name, url=action_url)
                    mail.send(msg)

                    # 超时处理
                    # token:userid
                    cache.set(user.token, user.id, timeout=30)

                    return datadir


                # 更新token
                user.token = str(uuid.uuid5(uuid.NAMESPACE_DNS, 'szflask'))
                db.session.add(user)
                db.session.commit()

                # 返回数据
                datadir['status'] = 200
                datadir['msg'] = '登录成功'
                datadir['data'] = user

                return datadir

            else:   # 密码错误
                datadir['status'] = 401
                datadir['msg'] = '登录失败'
                datadir['err'] = '密码错误！'
                return datadir

        else:               # 用户名不存在
            datadir['status'] = 401
            datadir['msg'] = '登录失败'
            datadir['err'] = '用户不存在！'
            return datadir
