from App.ext import init_ext
from App.settings import config
from App.views import init_blue


def init_app(env_name=None):
    from flask import Flask

    # 创建flask对象
    app = Flask(__name__)

    # 配置
    app.config.from_object(config.get(env_name or 'default'))

    # 插件
    init_ext(app)

    # 蓝图
    init_blue(app)

    return app