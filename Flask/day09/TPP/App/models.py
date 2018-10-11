from App.ext import db


# class City(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     parentId = db.Column(db.Integer, default=0)
#     regionName = db.Column(db.String(50))
#     cityCode = db.Column(db.Integer)
#     pinYin = db.Column(db.String)
#     letter = db.Column(db.String(10))


# 一对多
# 一个字母对应多个城市
class Letter(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(3))
    # 对应的城市
    l_citys = db.relationship('City', backref='letter', lazy=True)

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    parentId = db.Column(db.Integer, default=0)
    regionName = db.Column(db.String(50))
    cityCode = db.Column(db.Integer)
    pinYin = db.Column(db.String(50))
    # 属于哪个字母[外键]
    c_letter = db.Column(db.Integer, db.ForeignKey(Letter.id))




# 用户模型类
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(255))
    email = db.Column(db.String(50), unique=True)
    phone = db.Column(db.String(20))
    icon = db.Column(db.String(30), default='head.png')
    token = db.Column(db.String(255))
    permission = db.Column(db.Integer, default=1)
    isactive = db.Column(db.Boolean, default=False)
    isdelete = db.Column(db.Boolean, default=False)



# 影片信息
# insert into
# movies( backgroundpicture, flag, isdelete)
# values("i1/TB19_XCoLDH8KJjy1XcXXcpdXXa_.jpg",1,0);
class Movies(db.Model):
    # id
    id = db.Column(db.Integer, primary_key=True)
    # 中文名
    showname = db.Column(db.String(255))
    # 英文名
    shownameen = db.Column(db.String(255))
    # 导演
    director = db.Column(db.String(100))
    # 主演
    leadingRole = db.Column(db.String(255))
    # 分类
    type = db.Column(db.String(100))
    # 产地
    country= db.Column(db.String(100))
    # 语言
    language = db.Column(db.String(100))
    # 时长
    duration = db.Column(db.Integer)
    # 放映方式(2D/3D/4D)
    screeningmodel = db.Column(db.String(20))
    # 上映时间
    openday = db.Column(db.String(30))
    # 影片图片
    backgroundpicture = db.Column(db.String(100))
    # 0全部数据  1即将上映  2热播
    flag = db.Column(db.Integer)
    # 是否删除
    isdelete = db.Column(db.Boolean, default=False)



# 影院模型类
# insert into
# cinemas(astrict,flag,isdelete)
# values(5,1,0);
class Cinemas(db.Model):
    # id
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 影院名称
    name = db.Column(db.String(255))
    # 城市
    city = db.Column(db.String(100))
    # 区域
    district = db.Column(db.String(100))
    # 具体地址
    address = db.Column(db.String(255))
    # 联系方式
    phone = db.Column(db.String(30))
    # 评分
    score = db.Column(db.Float)
    # 放映厅个数
    hallnum = db.Column(db.Integer)
    # 服务评分
    servicecharge = db.Column(db.Float)
    # 限制
    astrict = db.Column(db.Integer)
    # 标志位
    flag = db.Column(db.Integer)
    # 逻辑删除
    isdelete = db.Column(db.Integer)

