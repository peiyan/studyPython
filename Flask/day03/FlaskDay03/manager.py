from flask_script import Manager
from Meituan import init_app

app = init_app()
manager = Manager(app)

if __name__ == '__main__':
    manager.run()
