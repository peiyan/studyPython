## 一 response响应
- 创建方式
```
- 直接返回字符串
- render_template
- make_response
- Response()
```

- 状态码
```
状态码位置: 第二个参数
    return 'Hello World!',201
    return render_template('temptest.html'),301
    resp = make_response('<h1>创建响应</h1>', 204)
    resp = Response('<h1>通过Response创建</h1>', 205)

2xx: 成功
3xx: 重定向
4xx: 客户端错误
5xx: 服务器错误
```

- 重定向
```
return redirect('/')
return redirect(url_for('blue.hello_world'))
```

- 异常处理
```
- abort(状态码) 抛出异常
- @blue.errorhandler(状态码) 处理异常
```


## 二 会话技术
- 概述
```
HTTP短链接,是无状态的!

- cookie
- session
- token
```

- cookie
```
- 客户端会话技术
- 支持过期时间
- 默认会自动携带本网站的所有cookie [自动/所有]
- 根据域名进行存储
- key-value
- 不能跨域名
- 不能跨浏览器


- 设置cookie
    resp.set_cookie('username', username)

- 获取cookie
    username = request.cookies.get('username', '游客(未登录)')

- 删除cookie
    resp.delete_cookie('username')
```

- session
```
- 服务端的会话技术
- 所有数据都存储在服务器中
- flask默认存储是在内存中 [django默认是做了持久化存储,是在数据库中]
- session 是离不开cookie
- key-value

- 设置session
    session['username'] = username

- 获取session
    username = session.get('username','游客(未登录)')

- 删除session
    # 方式一: cookie
    resp.delete_cookie('username')

    # 方式二: session
    session.pop('username')
```
> 要使用session,得配置secret_key


- token
```
- 手动实现的session
- Android/ios 没有cookie, 是不能使用使用cookie
- 服务器只负责给客户端传输,客户端保存(你怎么保存我不管)
- 每次请求时,请将token传过来
```


## 三 flask-session插件 [session可持久化存储]
```
- 安装插件
    pip install flask-session

- 初始化
	from flask_session import Session
    app.config['SESSION_TYPE'] = 'redis'  # session类型
    Session(app)            # 和应用关联

    app.config['SESSION_COOKIE_NAME'] = 'flask(session)'    # 可选,cookie中存储的名字key
    app.config['PERMANENT_SESSION_LIFETIME'] = 60           # 可选,超时时间,单位是秒,默认31天

- 使用
    原生一模一样(不需要做任何的修改)
```
> redis安装: sudo apt install redis


## 四 模板
- 模板概念
```
{{ 变量 }}
{% 标签 %}
```

- 结构标签 block
```
- 第一次是挖坑
    {% block 名称 %}   {% endblock %}

- 第二次是填坑
    {% block 名称 %}   {% endblock %}

- 保留父模块
    {% block 名称 %}
        {{ super() }}
        # 其他内容
    {% endblock %}
```

- 结构标签 extends
```
    {% extends 'base.html' %}
```

- 结构标签 include
```
将页面进行拆分,拆分成一个个的小模块.
通过include包含,即进行拼接.

{% include 'home-goods.html' %}
```

- 宏定义 macro
```
# 不带参数
{% macro study() %}
    <h3> 我爱学习! </h3>
{% endmacro %}

# 带参数
{% macro study(name) %}
    <h3> {{ name }}: 我爱学习! </h3>
{% endmacro %}

# 导入
{% from 'appmacro.html' import create_student %}
```

- if语句
```
    {% if username and username == 'root' %}
        <h1>超级用户^_^!</h1>
    {% elif username %}
        <h1>欢迎用户: {{ username }}</h1>
    {% else %}
        <h1> 游客(未登录) </h1>
    {% endif %}
```

- for语句
```
{% for student in students %}
{% endfor %}
```

## 五 模型
- ORM
```
对象关系映射
```

manager.py 文件 代码

```\javascript
from flask_script import Manager
from App import init_app

app = init_app()
manager = Manager(app)

if __name__ == '__main__':
    manager.run()
```

```javascript
__init__.py文件代码:

from flask_session import Session
from App.views import blue

def init_app():
    from flask import Flask
    app = Flask(__name__)

    # 配置
    # app.secret_key = '$%^&*(FGHJKVBNJE$%^&*#$%^&*DFGHJ'
    app.config['SECRET_KEY'] = '$%^&*(FGHJKVBNJE$%^&*#$%^&*DFGHJ'
    app.config['SESSION_TYPE'] = 'redis'
    app.config['SESSION_COOKIE_NAME'] = 'flask(session)'
    app.config['PERMANENT_SESSION_LIFETIME'] = 60
    # 方式一
    # Session(app)

    # 方式二
    ses = Session()
    ses.init_app(app)

    # 注册蓝图
    app.register_blueprint(blueprint=blue)

    return app

```

view.py 代码

```javascript
from flask import Blueprint, render_template, make_response, Response, redirect, url_for, abort, request, session

blue = Blueprint('blue', __name__)


######################### response创建方式 #########################
@blue.route('/123123123sffdsf/')
def hello_world():
    return 'Hello World!',201


@blue.route('/templaptetest/')
def temptest():
    return render_template('temptest.html'),301

@blue.route('/makeresponse/')
def makeresponse():

    resp = make_response('<h1>创建响应</h1>', 204)

    return resp

@blue.route('/responsetest/')
def responsetest():
    resp = Response('<h1>通过Response创建</h1>', 205)
    return resp



######################### 重定向 #########################
@blue.route('/redirecttest/')
def redirecttest():
    # 固定写法
    # return redirect('/')

    # 反向解析
    return redirect(url_for('blue.hello_world'))



######################### abort 抛出异常 #########################
@blue.route('/aborttest/<int:num>/')
def aborttest(num):
    if num:
        return '正常.....'
    else:
        abort(404)  # 抛出异常

# 捕获异常
@blue.errorhandler(404)
def error404(exception):
    return render_template('error404.html')

@blue.errorhandler(400)
def error400(exception):
    return '恭喜你中奖了,中奖号码400!'



#########################  会话技术cookie #########################
# # 首页
# @blue.route('/index/')
# def index():
#     # 获取cookie
#     username = request.cookies.get('username', '游客(未登录)')
#
#     # 渲染模板
#     return render_template('index.html', username=username)
#
# # 登录
# @blue.route('/login/', methods=['GET','POST'])
# def login():
#     if request.method == 'GET': # 登录页面
#         return render_template('login.html')
#     elif request.method == 'POST':  # 登录请求
#         # 获取用户名
#         username = request.form.get('username')
#
#         # 设置cookie
#         resp = redirect(url_for('blue.index'))
#         resp.set_cookie('username', username)
#
#         # 登录成功,重定向到首页
#         # return redirect(url_for('blue.index'))
#         return resp
#
# # 退出
# @blue.route('/quit/')
# def quit():
#     print('退出')
#     # 退出成功,重定向到首页
#     # return redirect(url_for('blue.index'))
#
#     resp = redirect(url_for('blue.index'))
#     resp.delete_cookie('username')
#
#     return resp
#
# # 关于我们
# @blue.route('/about/')
# def about():
#     username = request.cookies.get('username', '游客(未登录)')
#
#     return render_template('about.html', username=username)






#########################  会话技术session #########################
# 首页
@blue.route('/index/')
def index():
    # 获取session
    username = session.get('username', '游客(未登录)')

    # 渲染模板
    return render_template('index.html', username=username)

# 登录
@blue.route('/login/', methods=['GET','POST'])
def login():
    if request.method == 'GET': # 登录页面
        return render_template('login.html')
    elif request.method == 'POST':  # 登录请求
        # 获取用户名
        username = request.form.get('username')

        # 设置session
        session['username'] = username

        # 登录成功,重定向到首页
        return redirect(url_for('blue.index'))

# 退出
@blue.route('/quit/')
def quit():
    print('退出')
    # 退出成功,重定向到首页
    # return redirect(url_for('blue.index'))

    resp = redirect(url_for('blue.index'))

    # 方式一: 删除cookie  [key-value]
    # resp.delete_cookie('session')

    # 方式二: 删除session  [key-value]
    session.pop('username')

    return resp

# 关于我们
@blue.route('/about/')
def about():
    # 获取session
    username = session.get('username', '游客(未登录)')

    return render_template('about.html', username=username)


######################### 模板 #########################
@blue.route('/base/')
def base():
    return render_template('base.html')


@blue.route('/home/')
def home():

    username = session.get('username')

    students = [
        {'name': '张三', 'score': 91},
        {'name': '李四', 'score': 23},
        {'name': '王五', 'score': 43},
        {'name': '赵柳', 'score': 97},
        {'name': '田七', 'score': 45},
        {'name': '王八', 'score': 96},
        {'name': '小九', 'score': 87},
    ]

    return render_template('home.html', username=username, students=students)
```

