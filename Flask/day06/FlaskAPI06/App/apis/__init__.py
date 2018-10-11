from flask_restful import Api

from App.apis.HelloApi import HelloResource
from App.apis.NameApi import NameResource

api = Api()

def init_api(app):
    api.init_app(app)


# 添加资源
# api.add_resource(HelloResource, '/api/v1/hello/', endpoint='hello')

api.add_resource(HelloResource, '/api/v1/hello/', '/api/v1/haha/', '/api/v1/hei/', '/api/v1/heheda/', endpoint='hello')
api.add_resource(NameResource, '/api/v1/name/<username>/', endpoint='name')