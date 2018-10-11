from flask_restful import Api

from App.apis.ActionApi import UserAction
from App.apis.CityApi import CityResource
from App.apis.HelloApi import HelloWorld
from App.apis.UserApi import UserResource

api = Api()

def init_api(app):
    api.init_app(app)


# 测试
api.add_resource(HelloWorld, '/api/v1/hello/', endpoint='hello')

# 区域选择
api.add_resource(CityResource, '/api/v1/city/', endpoint='city')

# 注册
api.add_resource(UserResource, '/api/v1/register/', endpoint='register')

# 激活
api.add_resource(UserAction, '/api/v1/action/', endpoint='action')