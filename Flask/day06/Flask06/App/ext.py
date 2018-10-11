from flask_bootstrap import Bootstrap
# from flask_cache import Cache
from flask_caching import Cache
# from flask.ext.cache import Cache
from flask_debugtoolbar import DebugToolbarExtension
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
migrate = Migrate()
toolbar = DebugToolbarExtension()
cache = Cache(config={
    'CACHE_TYPE':'redis',
    'CACHE_KEY_PREFIX':'flaskcache',
    'CACHE_DEFAULT_TIMEOUT':60
})
api = Api()

def init_ext(app):
    db.init_app(app)
    migrate.init_app(app,db)
    Bootstrap(app)
    toolbar.init_app(app)
    cache.init_app(app)
    api.init_app(app)