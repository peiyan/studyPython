from flask import request
from flask_restful import Resource


# 定义资源
class NameResource(Resource):
    def get(self,username):
        age = request.args.get('age')
        print(age)
        return {'msg': '你的名字:%s'%username}