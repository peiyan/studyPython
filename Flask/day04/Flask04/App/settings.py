import os


class BaseConfig():
    DEBUG = False
    TESTING = False
    SECREY_KEY = '%^&*()FGHJK5678912313'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopConfig(BaseConfig):
    # 特别注意!!!
    # 操作的Flaks04/APP/sql3.db
    # flask-migrate对应生成 Flask04/sql3.db
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///sql3.db'

    # 方式一(使用flask-migrate)  [建议使用绝对路径]
    # 相对路径会有问题,flask-migrate和settings配置的时,路径不匹配 [相对路径导致]
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///../sql4.db'

    # 绝对路径
    # BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    # print(BASE_DIR)
    # SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(BASE_DIR,'./sql4.db')


    # 方式二: db.create_all()
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///sql5.db'


    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/szflask04'


config = {
    'develop': DevelopConfig,
    'default': DevelopConfig
}
