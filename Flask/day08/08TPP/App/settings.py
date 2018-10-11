
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


config = {
    'develop': DevelopConfig,
    'default': DevelopConfig
}