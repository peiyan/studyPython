
class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = "$%^&*(FGHJKL#$%^&*fghjuikfghj"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopConfig(BaseConfig):
    # DEBUG = True
    # 如果远程服务器mysql [mysql需要有远程链接用户]
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/szflask06'


config = {
    'develop': DevelopConfig,
    'default': DevelopConfig
}