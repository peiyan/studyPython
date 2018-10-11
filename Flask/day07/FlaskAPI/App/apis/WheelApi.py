from flask_restful import Resource, fields, marshal_with
from App.models import Wheel


# {
#     'stauts': 200,
#     'msg': '获取轮播图数据成功',
#     'data': [
#         {
#             'img':'',
#             'name':'',
#             'trackid':''
#         },
#         {
#             'img':'',
#             'name':'',
#             'trackid':''
#         },
#         ...
#     ]
# }

# 响应格式定制
wheel_fields = {
    'img': fields.String,
    'name': fields.String,
    'trackid': fields.String
}

result_fiedls = {
    'status': fields.Integer,
    'msg': fields.String,
    'data': fields.List(fields.Nested(wheel_fields))
}

class WheelResource(Resource):
    @marshal_with(result_fiedls)
    def get(self):
        wheels = Wheel.query.all()

        datadir = {
            'status':200,
            'msg':'获取数据成功',
            'data': wheels
        }

        return datadir