from flask_restful import Resource, fields, marshal_with
from App.models import Dog

##############################  原生写法  ##############################
# 参考格式(一只)
# {
#     'status': 200,
#     'msg': '获取数据成功',
#     'data': {
#         'name': '大黄',
#         'color': '黄色'
#     }
# }

# 定义资源
# class DogResource(Resource):
#     def get(self):
#         dog = Dog.query.first()
#         datadir = {
#             'status': 200,
#             'msg': '获取数据成功',
#             'data': {
#                 'name': dog.name,
#                 'color': dog.color
#             }
#         }
#
#         return datadir



# 参考格式(多只)
# {
#     'status': 200,
#     'msg': '获取数据成功',
#     'data': [
#         {
#             'name':'大黄',
#             'color':'黄色'
#         },
#         {
#             'name': '大黄',
#             'color': '黄色'
#         },
#         {
#             'name':'大黄',
#             'color':'黄色'
#         },
#         {
#             'name':'大黄',
#             'color':'黄色'
#         }
#     ]
# }
# 定义资源
# class DogResource(Resource):
#     def get(self):
#         dog = Dog.query.all()
#
#         datadir = {
#             'status': 200,
#             'msg': '获取数据成功',
#             'data': [
#                 {
#                     'name': dog[0].name,
#                     'color': dog[0].color
#                 },
#                 {
#                     'name': dog[1].name,
#                     'color': dog[1].color
#                 },
#                 {
#                     'name': dog[2].name,
#                     'color': dog[2].color
#                 },
#                 {
#                     'name': dog[3].name,
#                     'color': dog[3].color
#                 },
#             ]
#         }
#
#         return datadir


##############################  flask-restful方式  ##############################


# 参考格式(一只)
# {
#     'status': 200,
#     'msg': '获取数据成功',
#     'data': {
#         'name': '大黄',
#         'color': '黄色'
#     }
# }
# 响应数据格式化 [格式定制]
# dog_fields = {
#     'name': fields.String,
#     'color': fields.String
# }
#
# result_fields = {
#     'status': fields.Integer,
#     'msg': fields.String,
#     'data': fields.Nested(dog_fields)
# }
#
#
# class DogResource(Resource):
#     @marshal_with(result_fields)
#     def get(self):
#         dog = Dog.query.first()
#         datadir = {
#             'status': 200,
#             'msg': '获取数据成功',
#             'data': dog
#         }
#
#         return datadir



# 参考格式(多只)
# {
#     'status': 200,
#     'msg': '获取数据成功',
#     'data': [
#         {
#             'name':'大黄',
#             'color':'黄色'
#         },
#         {
#             'name': '大黄',
#             'color': '黄色'
#         },
#         {
#             'name':'大黄',
#             'color':'黄色'
#         },
#         {
#             'name':'大黄',
#             'color':'黄色'
#         }
#     ]
# }

# String 字符串   ""
# Integer 整形    数字
# Nested 级联类型  {}
# List 列表类型    []
dog_fields = {
    'name': fields.String,
    'color': fields.String,
    'runing': fields.String(default='跑...')
}

result_fields = {
    'stauts': fields.Integer,
    'msg': fields.String,
    'data': fields.List(fields.Nested(dog_fields))
}

class DogResource(Resource):
    # 定制中字段不存在，数据是不会被显示（自动过滤掉）
    # 定制中字段存在，数据会正常显示
    # 返回数据比定制的字段要少，显示默认值(前提有默认值)
    @marshal_with(result_fields)
    def get(self):
        dogs = Dog.query.all()
        datadir = {
            'status': 200,
            'msg': '获取数据成功',
            'data': dogs
        }

        return datadir