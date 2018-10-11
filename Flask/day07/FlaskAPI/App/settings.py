
class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SECRECY_KEY = '%^&*()ghjkl1231f%^&*()FGHJKL'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/szflask07'


config = {
    'develop': DevelopConfig,
    'default': DevelopConfig
}