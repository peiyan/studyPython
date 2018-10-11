import os

import werkzeug
from flask_restful import Resource,reqparse,marshal_with,fields

# 请求格式定制
from werkzeug.utils import secure_filename

from App.ext import db
from App.models import User
from App.settings import UPLOAD_DIR

parser = reqparse.RequestParser()
parser.add_argument('token', type=str, required=True, help='请提供token')
parser.add_argument('headimg', type=werkzeug.datastructures.FileStorage, location='files',required=True, help='请提供headimg')


# 自定义字段
class UserIcon(fields.Raw):
    def format(self, value):
        return '/staitc/img/' + value

# 响应格式定制
user_fileds = {
    'icon': UserIcon(attribute='icon'),
}

result_fileds = {
    'status': fields.Integer,
    'msg': fields.String,
    'err': fields.String(default=''),
    'data': fields.Nested(user_fileds, default='')
}


class FileResource(Resource):
    @marshal_with(result_fileds)
    def post(self):
        parse = parser.parse_args()
        token = parse.get('token')

        users = User.query.filter(User.token == token)

        datadir = {}

        if users.count():

            user = users.first()

            # 获取图片
            imgfile = parse.get('headimg')
            # 图片名
            filename = '%d-%s' % (user.id, secure_filename(imgfile.filename))
            # 图片路径
            filepath = os.path.join(UPLOAD_DIR, filename)
            # 保存
            imgfile.save(filepath)

            # 更新用户信息
            user.icon = filename
            db.session.add(user)
            db.session.commit()

            datadir['status'] = 200
            datadir['msg'] = '上传文件成功'
            datadir['data'] = user

            return datadir

        else:   # 用户不存在
            datadir['status'] = 401
            datadir['msg'] ='上传文件失败'
            datadir['err'] = 'token有问题'
            return datadir