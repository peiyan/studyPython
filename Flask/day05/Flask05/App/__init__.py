from App.ext import init_ext
from App.settings import config
from App.views import init_blue


def init_app(env_name=None):
    from flask import Flask

    app = Flask(__name__)


    # 配置(settings.py)
    app.config.from_object(config.get(env_name or 'default'))

    # 插件(ext.py)
    init_ext(app)

    # 蓝图(views.py)
    init_blue(app)


    return app