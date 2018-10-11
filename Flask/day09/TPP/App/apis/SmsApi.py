import random

from flask_restful import Resource

from App.ext import cache


class SMSResource(Resource):
    def get(self):
        ###  准备必要参数
        # 短信应用SDK AppID
        appid = 1400112809  # SDK AppID是1400开头

        # 短信应用SDK AppKey
        appkey = "8d8b808cb9073023631d241951f49fb4"

        # 需要发送短信的手机号码
        # phone_numbers = ["15770848880", "15770878316", "18666579112"]

        # 短信模板ID，需要在短信应用中申请
        # 短信验证码: {1}，请于{2}分钟内填写。如非本人操作，请忽略本短信。
        template_id = 166915  # NOTE: 这里的模板ID`7839`只是一个示例，真实的模板ID需要在短信控制台中申请

        # 签名
        sms_sign = "钟远智工作经验分享"  # NOTE: 这里的签名"腾讯云"只是一个示例，真实的签名需要在短信控制台中申请，另外签名参数使用的是`签名内容`，而不是`签名ID`


        ### 指定模板ID单发短信
        from qcloudsms_py import SmsSingleSender
        from qcloudsms_py.httpclient import HTTPError

        ssender = SmsSingleSender(appid, appkey)
        # 模板参数
        # 短信验证码: {1}，请于{2}分钟内填写。如非本人操作，请忽略本短信。
        rand= random.randrange(1000,10000)
        params = [random, 3]

        # 超时处理

        try:
            result = ssender.send_with_param(86, 15770848880,
                                             template_id, params, sign=sms_sign, extend="",
                                             ext="")  # 签名参数未提供或者为空时，会使用默认签名发送短信
        except HTTPError as e:
            print(e)
        except Exception as e:
            print(e)

        print(result)
