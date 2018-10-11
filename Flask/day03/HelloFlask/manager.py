from flask_script import Manager
from App import init_app
from flask_migrate import MigrateCommand

app = init_app()
manager = Manager(app)

# 添加了一个新的命令 db
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
