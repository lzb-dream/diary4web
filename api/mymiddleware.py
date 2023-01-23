from django.utils.deprecation import MiddlewareMixin
import jwt
from django.conf import settings
from django.http import JsonResponse
import json
import re

class Myware(MiddlewareMixin):
    # 请求到达路由之前
    def process_request(self,request):
        judge = re.match(r'^/admin',request.path)
        if judge:
            return None
        path = request.path.replace('/api/','')
        allowPath = ['login']
        if path=='getWallPaper' and request.method == 'POST':
            return None
        if path in allowPath:
            return None
        token = request.META.get("HTTP_AUTHORIZATION")
        if not token:
            print('没有获取到token')
            return
        key = settings.SECRET_KEY
        try:
            tokenParse = jwt.decode(token,key,algorithms='HS256')
            openId = tokenParse.get('user')
            if openId:
                if request.method == 'GET':
                    data = request.GET.copy()
                    data['openId'] = openId
                    request.GET = data
                else:
                    # 对上传文件路由放行
                    if request.method == 'POST' and path == 'media':
                        return None
                    # 重新构造请求体, 进行编码后, 重新赋值给 request._body
                    # 注意是 request._body, 因为 request.body 是不可修改的, 但是 body 属性继承自 _body 属性, 所以直接修改 _body 属性
                    data = json.loads(request.body.decode())
                    data['openId'] = openId
                    request._body = json.dumps(data).encode(encoding="utf-8")
        except:
            print('token错误')
            return JsonResponse({'error':'token错误'},status=401)

    # 请求达到视图之前
    def process_view(self,request,callback,callback_args,callback_kwargs):
        # print('请求达到路由之前')
        pass
    # 返回响应
    def process_response(self,request,response):
        # print('发返回视图')
        return response