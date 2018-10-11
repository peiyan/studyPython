from App.apis import init_api
from App.ext import init_ext
from App.settings import config


def init_app(env_name=None):
    from flask import Flask
    app = Flask(__name__)

    # 配置
    app.config.from_object(config.get(env_name or 'default'))

    # 插件
    init_ext(app)

    # api
    init_api(app)

    return app