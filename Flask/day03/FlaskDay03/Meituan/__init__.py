from Meituan.models import init_db
from Meituan.views import blue

def init_app():
    from flask import Flask

    app = Flask(__name__)  # 点击Flask 看一下源文件的配置

    # 数据库配置
    # 当前路径下创建sql3.db
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sql3.db'

    # 当前路径下db/sqlite.db
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/sqlite.db'

    # 在根目录创建 sqlite4.db
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../sqlite4.db'

    # 换mysql
    # dialect+driver://username:password@host:port/database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/flaskday03'


    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # 注册蓝图
    app.register_blueprint(blueprint=blue)

    # SQLAlchemy
    init_db(app)  

    return app
