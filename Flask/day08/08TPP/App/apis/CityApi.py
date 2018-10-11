from flask_restful import Resource, fields, marshal_with, marshal
from App.models import City, Letter

# 模拟返回数据格式
# {
#     'status':200,
#     'msg': '获取城市列表成功',
#     'err': '',
#     'data': {
#         'A':[
#             {
#                 'id':1,
#                 'parentId': 0,
#                 'regionName': '深圳',
#                 'cityCode': 100,
#                 'pinYin': 'shenzhen'
#             }
#         ]
#     }
# }

# 响应格式定制
city_fields = {
    'id':fields.Integer,
    'parentId':fields.Integer,
    'regionName':fields.String,
    'cityCode':fields.Integer,
    'pinYin':fields.String
}

letter_fields = {
    'A': fields.List(fields.Nested(city_fields)),
    'B': fields.List(fields.Nested(city_fields)),
    'C': fields.List(fields.Nested(city_fields)),
    'D': fields.List(fields.Nested(city_fields)),
    'E': fields.List(fields.Nested(city_fields)),
    'F': fields.List(fields.Nested(city_fields)),
    'G': fields.List(fields.Nested(city_fields)),
    'H': fields.List(fields.Nested(city_fields)),
    'J': fields.List(fields.Nested(city_fields)),
    'K': fields.List(fields.Nested(city_fields)),
    'L': fields.List(fields.Nested(city_fields)),
    'M': fields.List(fields.Nested(city_fields)),
    'N': fields.List(fields.Nested(city_fields)),
    'P': fields.List(fields.Nested(city_fields)),
    'Q': fields.List(fields.Nested(city_fields)),
    'R': fields.List(fields.Nested(city_fields)),
    'S': fields.List(fields.Nested(city_fields)),
    'T': fields.List(fields.Nested(city_fields)),
    'W': fields.List(fields.Nested(city_fields)),
    'X': fields.List(fields.Nested(city_fields)),
    'Y': fields.List(fields.Nested(city_fields)),
    'Z': fields.List(fields.Nested(city_fields)),
}

result_fields = {
    'status':fields.Integer,
    'msg':fields.String,
    'err':fields.String(default=''),
    'data':fields.Nested(letter_fields)
}

class CityResource(Resource):
    # 装饰器方式
    # @marshal_with(result_fields)
    # def get(self):
    #     # 获取所有字母 [字母中就有对应的城市]
    #     letters = Letter.query.all()
    #
    #     data = {}
    #
    #     # 遍历每个字母对应的城市
    #     for letter in letters:
    #         # print(letter.l_citys)
    #         # 'A':[]
    #         data[letter.name] = letter.l_citys
    #
    #         # 检查能否获取对应的城市信息
    #         # for city in letter.l_citys:
    #         #         print(city.regionName)
    #
    #
    #     datadir = {
    #         'status': 200,
    #         'msg':'获取区域数据成功',
    #         'data': data
    #     }
    #
    #     return datadir



    def get(self):
        letters = Letter.query.all()

        # 数据
        data = {}
        # 动态格式列表 'A':fields.List(...)
        letter_fields_dynamic = {}

        for letter in letters:
            # 添加数据  'A':[]
            data[letter.name] = letter.l_citys
            # 添加格式  'A':fields.List(...)
            letter_fields_dynamic[letter.name] = fields.List(fields.Nested(city_fields))

        # 最终的数据
        datadir = {
            'status': 200,
            'msg':'获取区域数据成功',
            'data': data
        }

        # 最终的格式
        result_fields_dynamic = {
            'status': fields.Integer,
            'msg': fields.String,
            'err': fields.String(default=''),
            'data': fields.Nested(letter_fields_dynamic)
        }

        # 格式化数据
        result = marshal(datadir, result_fields_dynamic)

        return result
