
## 一 环境
    Ubuntu 16.04


## 二 课程安排
```
    - flask基本流程
    - 视图
    - 会话
    - session
    - 模板
    - 模型
    - bootstrap
    - 分页
    - cache   # 在一些版本有进行修改Api,慢慢caching
    - REST
    - RESTful
    - 前后端分离
    - 淘票票
    - flask考试
```

## 三 笔记

flask笔记: EndEvent

## 四 flask简介

[flask官网](http://flask.pocoo.org/)

[flask中文文档](http://docs.jinkan.org/docs/flask/)  # 百度指数的查询,GitHub上得查询


## 五 flask的流行
- 文档齐全
- 扩展机制
- 社区活跃
- 微框架


## 六 MVC和MTV
- MVC
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
    负责业务对象于数据库对象ORM
T: 模板
    负责如何把页面显示给用户
V: 视图
    业务逻辑处理(Model和Template)
```

## 七 Django和flask对比
- 返回一个数据
- 返回一个页面


## 八 flask-script插件 [能不能类似于Django启动操作]

flask-script 接受命令行参数

- 插件操作
```
- 安装插件
- 初始化插件(配置插件)
- 使用插件
```

- flask-scirpt插件
```
- 安装插件
    pip install flask-script

- 初始化
    manager = Manager(app)
    manager.run()

- 使用插件
    命令行启动: python manager.py runserver



python manager.py runserver --help  # 查看参数帮助文档
python manager.py runserver -r -d -h '0.0.0.0' -p 8001  # 启动项目,并自定参数
```

## 九 项目拆分(flask-blueprint插件)
```
- 安装插件
    pip install flask-blueprint

- 初始化
    blue = Blueprint('blue', __name__)
    app.register_blueprint(blueprint=blue)

- 使用
    @blue.rout('/')
    def index():
        return 'hello'
```

## 十 请求参数
- 请求类型
```
- 路径参数
- get
- post
```

- 路径参数
```
- string(默认)
- int
- float
- path
- uuid
- any
```


## 十一 请求方式
```
默认支持: GET/HEAD/OPTIONS.
```


## 十二 反向解析
```
反向解析语法: 蓝图名称.函数名

temp = url_for('helloblue.req')
```


## 十三 request请求

request是内置对象,所有路由函数中都有!
服务器在接受到客户端请求后,会自动创建request对象,由flask自动创建,request不能修改!
```
- get请求参数
    request.args['height']  # 不推荐
    request.args.get('height')  # 推荐
```

## 十四 response响应
- response创建
```
- 直接返回
- render_template
- make_response
- Response()
```

## 十五 作业
```
- 消化当天内容
- 预习(简书)
- 会话技术(cookie/session/token)
```