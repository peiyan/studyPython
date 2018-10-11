from flask import request
from flask_restful import Resource, reqparse


# 请求格式化定制
parser = reqparse.RequestParser()
parser.add_argument('page', type=int, required=True, help='请提供page参数')
parser.add_argument('per_page', type=int, required=True, help='请提供per_page参数')

class GoodsResource(Resource):
    def get(self):
        # request.args
        parse = parser.parse_args()
        page = parse.get('page')
        print(page)

        return {'msg':'商品列表'}

    def post(self):
        # request.form
        parse = parser.parse_args()
        per_page = parse.get('page')
        print(per_page)

        return {'msg':'ok'}
