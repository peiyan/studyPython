from flask_migrate import Migrate
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migate = Migrate()


def init_ext(app):
    db.init_app(app)
    Session(app)
    migate.init_app(app=app, db=db)