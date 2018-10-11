import os


class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SECRECY_KEY = '%^&*()ghjkl1231f%^&*()FGHJKL'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/sztpp1805'
    MAIL_SERVER = 'smtp.163.com'
    MAIL_USERNAME = '18924235915@163.com'
    MAIL_PASSWORD = 'zyz123'


# 根目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR, 'static/img')


config = {
    'develop': DevelopConfig,
    'default': DevelopConfig
}