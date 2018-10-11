from flask_restful import Resource, marshal_with, reqparse, fields, abort

from App.ext import db
from App.models import Movies, User

# get请求格式定制
parser_get = reqparse.RequestParser()
parser_get.add_argument('flag', type=int)

# post请求格式定制
parser_post = reqparse.RequestParser()
parser_post.add_argument('token', type=str, required=True, help='请提供token')
parser_post.add_argument('id', type=str, required=True, help='请提供id')
parser_post.add_argument('showname', type=str, required=True, help='请提供showname')
parser_post.add_argument('shownameen', type=str, required=True, help='请提供shownameen')
parser_post.add_argument('director', type=str, required=True, help='请提供director')
parser_post.add_argument('leadingRole', type=str, required=True, help='请提供leadingRole')
parser_post.add_argument('type', type=str, required=True, help='请提供type')
parser_post.add_argument('country', type=str, required=True, help='请提供country')
parser_post.add_argument('language', type=str, required=True, help='请提供language')
parser_post.add_argument('duration', type=str, required=True, help='请提供duration')
parser_post.add_argument('screeningmodel', type=str, required=True, help='请提供screeningmodel')
parser_post.add_argument('openday', type=str, required=True, help='请提供openday')
parser_post.add_argument('backgroundpicture', type=str, required=True, help='请提供backgroundpicture')
parser_post.add_argument('flag', type=str, required=True, help='请提供flag')

# 响应格式定制
movies_fileds = {
    'showname':fields.String,
    'shownameen':fields.String,
    'director':fields.String,
    'leadingRole':fields.String,
    'type':fields.String,
    'country':fields.String,
    'language':fields.String,
    'duration':fields.Integer,
    'screeningmodel':fields.String,
    'openday':fields.String,
    'backgroundpicture':fields.String,
}

result_fileds = {
    'status': fields.String,
    'msg': fields.String,
    'err': fields.String(default=''),
    'data': fields.List(fields.Nested(movies_fileds))
}


# 权限管理装饰器(只管权限，不管数据)
# 1 可读权限
# 4 可写权限
WRITE_PERMISSION = 4

def check_permission_control(permission):
    def check_permission(func):
        def check(*args, **kwargs):
            parse = parser_post.parse_args()
            token = parse.get('token')

            users = User.query.filter(User.token == token)
            if users.count():   # 有登录
                user = users.first()

                if user.permission & permission == permission:  # 有权限
                    return func(*args, **kwargs)
                else:   # 没有权限
                    abort(403, message='你没有写权限，如需更高权限，请联系管理员')

            else:   # 没有登录
                abort(401, message='你还没登录，请登录后操作')

        return check
    return check_permission


class MoviesResource(Resource):
    @marshal_with(result_fileds)
    def get(self):
        parse = parser_get.parse_args()
        flag = parse.get('flag') or 0

        if flag:
            movies = Movies.query.filter(Movies.flag == flag).filter(Movies.isdelete == False)
        else:
            movies = Movies.query.filter(Movies.isdelete == False)

        datadir = {
            'status':200,
            'msg':'获取电影列表成功',
            'data': movies
        }

        return datadir


    @check_permission_control(WRITE_PERMISSION)
    @marshal_with(result_fileds)
    def post(self):     # 只要能进去，说明权限是有的。只管数据，不管权限
        parse = parser_post.parse_args()
        movies = Movies()
        movies.id = parse.get('id')
        movies.showname = parse.get('showname')
        movies.shownameen = parse.get('shownameen')
        movies.director = parse.get('director')
        movies.leadingRole = parse.get('leadingRole')
        movies.type = parse.get('type')
        movies.country = parse.get('country')
        movies.language = parse.get('language')
        movies.duration = parse.get('duration')
        movies.screeningmodel = parse.get('screeningmodel')
        movies.openday = parse.get('openday')
        movies.backgroundpicture = parse.get('backgroundpicture')
        movies.flag = parse.get('flag')

        db.session.add(movies)
        db.session.commit()

        datadir = {
            'status':200,
            'msg':'添加电影成功',
            'data': Movies.query.filter(Movies.id == movies.id)
        }

        return datadir

