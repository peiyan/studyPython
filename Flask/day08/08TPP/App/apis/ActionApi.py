import uuid

from flask_restful import Resource,marshal_with,reqparse,fields

from App.ext import cache, db
from App.models import User

parser = reqparse.RequestParser()
parser.add_argument('token', type=str, required=True, help='请提供token')


user_fileds = {
    'name': fields.String,
    'icon': fields.String,
    'token': fields.String,
    'permission': fields.String
}

result_fileds = {
    'status': fields.Integer,
    'msg': fields.String,
    'err': fields.String(default=''),
    'data': fields.Nested(user_fileds, default='')
}



class UserAction(Resource):
    @marshal_with(result_fileds)
    def get(self):
        parse = parser.parse_args()
        token = parse.get('token')

        # 根据token 获取userid
        userid = cache.get(token)
        if userid:  # 存在(没超时)
            # 删除cache
            cache.delete(token)

            # 对应用户
            user = User.query.get(userid)

            user.isactive = True
            user.token = str(uuid.uuid5(uuid.NAMESPACE_DNS, 'szflask'))
            db.session.add(user)
            db.session.commit()

            datadir = {
                'status': 200,
                'msg': '激活成功',
                'data': user
            }

            return datadir

        else:       # 不存在(超时)
            datadir = {
                'status':201,
                'msg':'激活失败，请联系管理员',
                'err': '该激活地址已过期!'
            }

            return datadir