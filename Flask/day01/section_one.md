####一  Flask简介

基于python实现的web开发"微"框架

百度指数的查询,gitHub上得查询

MVC   Flask和Django一样,也是一个基于MVC设计模式的web框架

```
官方文档: http://flask.pocoo.org/docs/0.12/
中文文档: http://docs.jinkan.org/docs/flask/
```

Flask依赖三个库: Jinja2模板引擎、Werkzeug WSGI工具集、Itsdangerous基于Django的签名模块

####二 MVC和MTV

```
M: 模型
    数据逻辑
    数据库中的数据存取
V: 视图
    数据显示部分
    视图依据数据模型创建的
C: 控制器
    用户交互部分
```

- MTV
```
M: 模型
    负责业务对象于数据库对象ORM (屏蔽了数据库SQL语句的不一致性,mysql oracle等)
T: 模板
    负责如何把页面显示给用户
V: 视图
    业务逻辑处理(Model和Template)
```

####三 Django和flask对比

- 返回一个数据   # flask  
- 返回一个页面   #Django

- 安装 Flask及新建一个原始项目

```
pip install flask

打开pycharm-new project-flask选项-(填写好名字及jingjia2信息)-create,创建项目

在Terminal 执行 python XX.py 启动项目
```

- 编辑文件

  ```
  # 创建hello.py文件
  from flask import Flask
  
  app = Flask(__name__)
  
  @app.route('/')
  def index():
      return 'Hello Flask'
  
  app.run()
    - 在启动时，可以在run()中添加参数
    - debug是否开启调试模式，开启后修改python代码会自动重启
    - threaded是否开启多线程
    - port启动指定服务器端口号
    - host主机，默认是127.0.0.1，指定为0.0.0.0代表本机IP
    	示例:app.run(debug=True, port=8000, host='0.0.0.0')
  ```

- 运行

  ```
  python hello.py
  ```

####四 插件(扩展库)

- flask-script插件,实现命令行参数接受

- 插件操作
```
- 安装插件
- 初始化插件(配置插件)
- 使用插件
    - 安装插件
        pip install flask-script
    - 调整代码
        app = Flask(__name__)
        manager = Manager(app)
    - 修改启动方式
        manager.run()
    - 命令启动项目(类似Django)
        python app.py runserver -r -d
        # 查看帮助文档，有哪些参数
        python app.py runserver --help
        # 端口号
        python app.py runserver -p 9000
        # 调试模式
        python app.py runserver -d 
        # 自动重新加载
        python app.py runserver -r
        # 主机
        python app.py runserver -h '0.0.0.0'
        
   Warning:生产环境是不能使用这种方式
   Pin: 后台调试密码
   示例: python manager.py runserver -r -d -h '0.0.0.0' -p 8001 # 启动项目,并自定参数
```

####五 项目拆分(flask-blueprint插件)

- 请求流程

  浏览器 ---> route ---> views --->models --->views --->template ---> 浏览器

  其中views可以不去models,两个views是一个,跟Django的请求流程是一样的

- 项目的简单拆分

  ```
  --  FlaskProject
       -- App
           -- static
           -- templates
           -- models.py
           -- views.py   注意: views.py直接写是不生效的，需要引入蓝图来解决这问题
       -- manager.py
  -- External Libraries (外部的库)
  ```

- 蓝图概念

```
项目模块划分阶段，使用Blueprint(这里暂且称之为“蓝本”)。Blueprint通过把实现不同功能的module分开,从而把一个大的application分割成各自实现不同功能的module。在一个Blueprint中可以调用另一个blueprint的view function, 但要加相应的blueprint名。 
  Blueprint还有其他好处，其本质上来说就是让程序更加松耦合，更加灵活，增加复用性，提高查错效率，降低出错概率。 
在具体项目开发过程中，不同蓝本分别对应不同的功能模块。例如auth授权模块和项目主模块。

- 蓝图
	宏观规划
- 蓝图是一种规划
	主要用来规划urls(路由)
```

- 蓝图基本使用

  ```
  - 安装插件 
      pip install flask-blueprint
  
  - 初始化蓝图
  	# views.py中创建
  	from flask import Blueprint
      blue = Blueprint('blue', __name__)  # 第一个参数'blue'反向解析会使用
      
      # 在app/__init__.py中注册
      from flask import Flask
      from App.views import blue
      def createapp():
          app = Flask(__name__)
          app.register_blueprint(blueprint=blue)
          return app
      
  - 调用蓝图进行路由注册
      @blue.route('/')
      def hello_world():
          return 'Hello World!'
          
  - 创建app
      # 在manager.py中
      from flask_script import Manager
      from App import createapp
  
      app = createapp()
      manager = Manager(app)
  
      if __name__ == '__main__':
          manager.run()
  ```

####六  视图之路由

路由对应视图函数,并且可以接收参数.

- 参数类型

  ```
  - 路径参数
  	位置参数
  	关键字参数
  - 请求参数
  	get 参数在路径中?之后
  	post 参数在请求体中
  ```

- 参数语法

  ```
  converter:var_name
  ```

- 参数类型converter

  ```javascript
  - string 字符串
      接收的时候也是string,匹配到 / 的时候是匹配结束
      例如: 
          @blue.route('/getstudent/<string:name>/')
          def getstudent(name):
              print(type(name))
              return '你的名字: %s' % name
              
  - path 路径
      接收的时候也是string,而 / 只会当作字符串中的一个字符处理
      
  - any 任意一个
      指的是any中提供的任意一个，类似于SQL查询中的 in
      例如: @blue.route('/getoption/<any(A,B,C):op>/')后面只能是A,B,C的其中一个
      
  - uuid 
      uuid格式
      例如: @blue.route('/getuser/<uuid:uu>/')
      
      # 获取uuid
      import uuid
      @blue.route('/getuuid/')
      def get_uuid():
          return str(uuid.uuid4())
      
  - int 
      int格式
    
  - float 
      float格式
  ```

  > 默认是string类型;
  >
  > 路由参数名和视图参数名必须一致 ! !

- 请求方式
```javascript
- 默认支持 GET,HEAD,OPTIONS
- 如果想支持某一请求方式,需要自己手动指定
	@blue.route('/requesttest/',methods=['POST','GET','PUT'])
```

- 反向解析
```js
- 语法
	url_for()
	url_for("蓝图名.函数名")
- 例如
# 反向解析
@blue.route('/gethello/')
def gethello():
	# 假设使用app就用app的名称,反之使用blue就用blue名称
	# 名称.函数名
	# blue = Blueprint('first',__name__)
	p = url_for('first.hello')
	return p
```

> 反向解析即是可以获取对应的路径

#### 七 视图之Request请求

服务器在接收到客户端请求后，会自动创建Request对象，由Flask自动创建，Request对象不可修改。

```javascript
- request.method
    请求方式
- request.path
    路由中的路径
- request.args
    get请求参数的包装，args是一个ImmutableMultiDict对象，类字典结构对象
    数据存储也是key-value
    外层是大列表，列表中的元素是元组，元组中左边是key，右边是value
    示例:
		- get请求参数
            request.args['height']  # 不推荐
            request.args.get('height')  # 推荐
- request.form
    存储结构个args一致
    默认是接收post参数
    还可以接收PUT，PATCH参数
- request.url
    完整请求地址
- request.base_url
    去掉GET参数的URL
- request.remote_addr
    请求的客户端地址
- request.file
    上传的文件
- request.headers
    请求头
- request.cookie
    请求中的cookie
    
ImmutableMultiDict类型
    ImmutableMultiDict类似字典的数据结构
    与字典的区别，可以存在相同的键
    args、form、files都是ImmutableMultiDict的对象
ImmutableMultiDict数据获取方式
    dict['uname']       
    dict.get('uname')  # 推荐(在没有数据为空)
    dict.getlist('uname')   # 获取指定key对应的所有值
```

> request , session是内置对象(所有路由函数中都有)  !!

####八  视图之Response响应

服务器返回给客户端的数据

- Response创建方式

```javascript
- 直接返回字符串
- render_template 渲染模板,将模板转换成字符串
- make_response 创建一个响应, 是一个真正的Response
- Response()创建
```

> Response由开发者创建

- 返回配置

  ```javascript
  - 内容
  	直接写, 将内容传递过去
  	@blue.route('/response/')
  	def get_response():
      	return "带你装逼带你飞",403
  - 状态码
      字符串形式直接将状态码添加到return 的第二个参数
      如果make形势，直接添加到make的第二个参数上
      # response响应3
      @blue.route('/makeresponse/')
      def make_resp():
          resp = make_response('<h2>我很帅!</h2>',300)
          return resp
  ```

- 返回重定向

  ``` :
  - redirect 重定向302
  - url_for 反向解析
  @blue.route('/redirect/')
  def make_redir():
  	# 固定
      # return redirect('/makeresponse/')
      # 反向解析
      return  redirect(url_for('first.make_resp'))
  ```

- 抛出异常 ,  终止程序执行

  ``` javascript
  - abort状态码
  
  @blue.route('/makeabort/')
  def make_abort():
      # 抛出异常(4xx  5xx)
      abort(404)
      return '睡着了?'
  ```

- errorhandler

  ``` java
  - 异常捕获
  - 可以根据状态或 Exception进行捕获
  - 函数中要包含一个参数，参数用来接收异常信息
  
  # 捕获404异常
  @blue.errorhandler(404)
  def handler404(exception):
      return '<h1>  我是404我怕谁！！！ </h1>'
  ```


#### 九 视图之会话技术

都是来解决HTTP请求在网络开发中短链接的问题，HTTP是无状态的。

- Cookie

  ``` java
  - 客户端会话技术，浏览器的会话技术
  - 数据全都是存储在客户端中
  - 存储使用的键值对结构进行的存储(key-value)
  - Cookie是通过服务器创建的Response来创建的
  - cookie特性
      支持过期时间
      默认会自动携带本网站的所有cookie
      根据域名进行cookie存储
      不能跨域名
      不能跨浏览器
      
  - 设置cookie
      respon = redirect(url_for('blue.index'))
      respon.set_cookie('username',username)
  - 获取cookie
      username = request.cookies.get('username','游客')
  - 删除cookie
      resp = redirect(url_for('blue.user_index'))
      resp.delete_cookie()
      
  备注:
      # 模板转为字符串
      tempstr = render_template('about.html', username=uu)
      # 模板字符串作为 响应对象 参数
      respon = make_response(tempstr)
      return respon
  ```

- Session

  ```javascript
  - 服务端的会话技术
  - 所有数据存储在服务器中
  - 默认存储在内存中
      django默认做了数据持久化(存在了数据库中)
  - 存储结构也是key-value形式，键值对(其实就是字典)
  - session 是离不开cookie的
  
  - 设置session
      session['username'] = username
  - 获取session
      username = session.get('username','游客')
  - 删除session
      # 方式一: session是存在cookie中的
      resp.delete_cookie('session')
      # 方式二: 直接删除session中对应数据
      session.pop('username')
  ```

  >要使用session还需要秘钥种子SECRET_KEY，在app初始化添加进去即可(app.config['SECRET_KEY'] = '1231231eqwedfaefdf');

- Token

  ```java
  - 手动实现的session
  - 如果在web开发中没有cookie，那么token也是不能使用的
  - 脱离web前端，Token是可以使用的
      传输给客户端，客户端保存
      在请求的时候，将token值再传输回来
  ```

####十 session之持久化存储

flask中这些插件几乎并没有干扰到之前的任何逻辑，使用起来非常的方便，就类似于中间件。

```
flask中session默认存储在内存中；
django中做了持久化，存储在数据库(可以修改到redis中)；
flask中没有对默认session进行任何处理；
flask-session 可以实现session的数据持久化；
redis(缓存在磁盘上的时候，管理磁盘文件使用lru, 最近最少使用);


- flask-session安装
    pip install flask-session

- 需要安装redis
    pip install redis
    
- flask-session的配置(初始化完成后，使用和之前session使用一致)
    # app/__init__.py文件中
    from flask_session import Session
    app.config['SECRET_KEY'] = '123qdqwe123113' # 秘钥
    app.config['SESSION_TYPE'] = 'redis'    # 配置
    sess = Session()    # 实例化session对象
    sess.init_app(app)  # session对象初始化
    
    # 简化操作： sess = Session(app)

- redis连接问题(需要启动)
    redis-server
    
- redis查看值
    # 进入到redis命令行
    redis-cli
    
    # 查看所有的
    keys *
    
    # 获取对应的值
    get xxxx(key)
    
    # 获取时间(session的生命周期,默认31天)
    ttl xxx(key)
    app.config['PERMANENT_SESSION_LIFETIME'] = 60 #可选,超过时间,单位时间是秒
    
    # 删除对应的值
    del xxx(key)
    
    # 删除当前所有的
    flushdb
    
- session其他设置(flask-session同样适用)
    PERMANENT_SESSION_LIFETIME 设置超时时间
        app.config['PERMANENT_SESSION_LIFETIME'] = 60
    SESSION_COOKIE_NAME 设置会话cookie的名称
        app.config['SESSION_COOKIE_NAME'] = 'flask'
```

> 备注: 如果没有安装redis-server是启动不了的。安装操作: sudo apt install redis