def get_uri(DATABASE):
    db = DATABASE.get('DB') or 'mysql'
    driver = DATABASE.get('DRIVER') or 'pymysql'
    username = DATABASE.get('USERNAME') or 'root'
    password = DATABASE.get('PASSWORD') or '123456'
    host = DATABASE.get('HOST') or '127.0.0.1'
    port = DATABASE.get('PORT') or '3306'
    dbname = DATABASE.get('DBNAME') or 'flask'

    return '{}+{}://{}:{}@{}:{}/{}'.format(db,driver,username,password,host,port,dbname)


# 基类
class BaseConfig():
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '$%^&*(FGHJKL#$%^&*(DFGHJ123'
    SESSION_TYPE = 'redis'


# 开发环境
class DevelopConfig(BaseConfig):
    DEBUG = True
    # 数据库配置
    DATABASE = {
        'DB': 'mysql',
        'DRIVER': 'pymysql',
        'USERNAME': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'DBNAME': 'szflask01'
    }

    # app.config('SQLALCHEMY_DATABASE_URI') = ''
    SQLALCHEMY_DATABASE_URI = get_uri(DATABASE)

# 测试环境
class TestingConfig(BaseConfig):
    TESTING = True

    SQLALCHEMY_DATABASE_URI = 'sqlite:///testing.db'


# 演示环境
class StagingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///staging.db'


# 线上环境
class ProductConfig(BaseConfig):
    # 数据库配置
    DATABASE = {
        'DB': 'mysql',
        'DRIVER': 'pymysql',
        'USERNAME': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'DBNAME': 'sz01',
    }

    # app.config('SQLALCHEMY_DATABASE_URI') = ''
    SQLALCHEMY_DATABASE_URI = get_uri(DATABASE)



# 配置
config = {
    'develop': DevelopConfig,   # 开发环境
    'testing': TestingConfig,   # 测试环境
    'staging': StagingConfig,   # 演示环境
    'product': ProductConfig,   # 线上环境
    'default': DevelopConfig
}
