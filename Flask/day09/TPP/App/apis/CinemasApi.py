from flask_restful import Resource,fields,marshal_with,reqparse

# 请求格式定制
from App.models import Cinemas

parser = reqparse.RequestParser()
parser.add_argument('city', type=str, default='全部')
parser.add_argument('district', type=str)
parser.add_argument('sort', type=int, default=1)   # 1降序，0升序
parser.add_argument('limit', type=int)

# 响应格式定制
cinemas_fields = {
    'name': fields.String,
    # '':fields.String,
    'city':fields.String,
    'district':fields.String,
    'address':fields.String,
    'phone':fields.String,
    'score':fields.Float,
    'hallnum':fields.Integer,
    'servicecharge':fields.Float,
    'astrict':fields.String,
}

result_fileds = {
    'status': fields.String,
    'msg': fields.String,
    'err': fields.String(default=''),
    'data': fields.List(fields.Nested(cinemas_fields))
}

class CinemasResource(Resource):
    @marshal_with(result_fileds)
    def get(self):
        parse = parser.parse_args()
        city = parse.get('city')
        district = parse.get('district')
        sort = parse.get('sort')
        limit_n = parse.get('limit')



        if sort == 1:
            cinemas = Cinemas.query.order_by(-Cinemas.score)
        elif sort == 0:
            cinemas = Cinemas.query.order_by(Cinemas.score)


        if city == '全部':
            cinemas = cinemas
        else:
            cinemas = cinemas.filter(Cinemas.city == city)

        if district:    # 有选择区域(没有选择即所有)
            cinemas = cinemas.filter(Cinemas.district == district)

        if limit_n:
            cinemas = cinemas.limit(limit_n)


        datadir = {
            'status': 200,
            'msg': '获取影院信息成功',
            'data': cinemas
        }

        return datadir
