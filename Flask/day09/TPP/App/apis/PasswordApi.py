import uuid

from flask_restful import Resource,marshal_with,reqparse,fields
from werkzeug.security import check_password_hash, generate_password_hash

from App.ext import db
from App.models import User

parser = reqparse.RequestParser()
parser.add_argument('token', type=str, required=True, help='请提供token')
parser.add_argument('oldPW', type=str, required=True, help='请提供oldPW')
parser.add_argument('newPW', type=str, required=True, help='请提供newPW')


result_fileds = {
    'status': fields.Integer,
    'msg': fields.String,
    'err': fields.String(default=''),
    'data': fields.String(default='')
}

class PasswordResource(Resource):
    @marshal_with(result_fileds)
    def post(self):
        parse = parser.parse_args()
        token = parse.get('token')
        oldPW = parse.get('oldPW')
        newPW = parse.get('newPW')
        datadir = {}

        user = User.query.filter(User.token == token).first()

        if check_password_hash(user.password, oldPW):
            user.password = generate_password_hash(newPW)
            db.session.add(user)
            db.session.commit()

            datadir['status'] = 200
            datadir['msg'] = '修改密码成功'
            datadir['err'] = ''
            return datadir
        else:
            datadir['status'] = 400
            datadir['msg'] = '修改失败'
            datadir['err'] = '旧密码不正确'
            return datadir