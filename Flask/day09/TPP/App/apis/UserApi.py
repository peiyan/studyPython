import uuid
from flask import render_template
from flask_mail import Message
from flask_restful import Resource,fields,marshal_with,reqparse
from werkzeug.security import generate_password_hash
from App.ext import db, mail, cache
from App.models import User

# 请求格式定制
parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True,help='请提供用户名name')
parser.add_argument('password', type=str, required=True,help='请提供密码password')
parser.add_argument('email', type=str, required=True,help='请提供邮箱email')
parser.add_argument('phone', type=str, required=True,
                    help='请提供手机号phone')


# 自定义字段
class UserIcon(fields.Raw):
    def format(self, value):
        return '/staitc/img/' + value

# 响应格式定制
user_fileds = {
    'name': fields.String,
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


class UserResource(Resource):
    @marshal_with(result_fileds)
    def post(self):
        # 获取数据
        parse = parser.parse_args()
        user = User()
        user.name = parse.get('name')
        user.password = generate_password_hash(parse.get('password'))
        user.email = parse.get('email')
        user.phone = parse.get('phone')
        # 生成token
        # uuid.uuid1() 基于时间戳(MAC地址+当前时间戳+随机数) 【不建议使用】

        # uuid.uuid2() 【Python中没有】

        # uuid.uuid3()  基于名字MD5散列值      【推荐使用】
        # user.token = str(uuid.uuid3(uuid.NAMESPACE_DNS, 'zsflask'))
        # user.token = str(uuid.uuid3(uuid.uuid4(), 'zsflask'))

        # uuid.uuid4()  基于随机数   【不推荐使用】
        # user.token = str(uuid.uuid4())

        # uuid.uuid5() 基于名字SHA-1散列值     【推荐使用】
        user.token = str(uuid.uuid5(uuid.NAMESPACE_DNS, 'zsflask'))


        # 返回数据
        datadir = {}

        # 异常(邮箱、用户名)
        users = User.query.filter(User.name == user.name).filter(User.password == user.password).filter(User.email == user.email)
        if users.count():   # 用户已注册
            datadir['status'] = 406
            datadir['msg'] = '注册失败'
            datadir['err'] = '用户已注册过，直接登录！'
            return datadir
        else:               # 用户未注册
            users = User.query.filter(User.email == user.email)
            if users.count():   # 邮箱已存在
                datadir['status'] = 406
                datadir['msg'] = '注册失败'
                datadir['err'] = '该邮箱已被注册过！'
                return datadir
            else:               # 邮箱不存在
                users = User.query.filter(User.name == user.name)
                if users.count():   # 用户名存在
                    datadir['status'] = 406
                    datadir['msg'] = '注册失败'
                    datadir['err'] = '用户名已存在！'
                    return datadir


        # 写入数据库
        db.session.add(user)
        db.session.commit()

        datadir['status'] = 200
        datadir['msg'] = '注册成功'
        datadir['data'] = user

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

        # 返回数据
        return datadir