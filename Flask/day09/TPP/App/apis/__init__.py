from flask_restful import Api

from App.apis.ActionApi import UserAction
from App.apis.CinemasApi import CinemasResource
from App.apis.CityApi import CityResource
from App.apis.FileApi import FileResource
from App.apis.HelloApi import HelloWorld
from App.apis.LoginApi import Login
from App.apis.MoviesApi import MoviesResource
from App.apis.PasswordApi import PasswordResource
from App.apis.SmsApi import SMSResource
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

# 登录
api.add_resource(Login, '/api/v1/login/', endpoint='login')

# 修改密码
api.add_resource(PasswordResource, '/api/v1/password/', endpoint='password')

# 电影列表
api.add_resource(MoviesResource, '/api/v1/movies/', endpoint='movies')

# 影院列表
api.add_resource(CinemasResource, '/api/v1/cinemas/', endpoint='cinemas')

# 文件上传(用户头像)
api.add_resource(FileResource, '/api/v1/file/', endpoint='file')

# 短信验证
api.add_resource(SMSResource, '/api/v1/sms/', endpoint='sms')