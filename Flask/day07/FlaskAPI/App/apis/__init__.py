from flask_restful import Api

from App.apis.DogApi import DogResource
from App.apis.GoodsApi import GoodsResource
from App.apis.HelloApi import HelloResource
from App.apis.WheelApi import WheelResource

api = Api()

def init_api(app):
    api.init_app(app)


# 添加资源
api.add_resource(HelloResource, '/api/v1/hello/', endpoint='hello')
api.add_resource(DogResource, '/api/v1/dog/', endpoint='dog')
api.add_resource(GoodsResource, '/api/v1/goods/',endpoint='goods')
api.add_resource(WheelResource,'/api/v1/wheel/', endpoint='wheel')