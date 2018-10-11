from App.apis import init_api
from App.ext import init_ext
from App.settings import config


def init_app(env_name=None):
    from flask import Flask

    app = Flask(__name__)

    app.config.from_object(config.get(env_name or 'default'))

    init_ext(app)

    init_api(app)

    return app