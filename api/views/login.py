from rest_framework.views import APIView, Response
from ..Serializers import User,UserSerializer
import httpx
import time
import jwt
import json
from ..models import Family,GourmetFood,Appointment,Child
from django.conf import settings

class Login(APIView):
    def post(self,request):
        data = request.data
        js_code = data.get('code')
        add_time = time.localtime(int(data.get('addTime')) / 1000)
        addTime = time.strftime('%Y-%m-%d %H:%M:%S', add_time)
        print('请求时间',addTime)
        url = f'https://api.weixin.qq.com/sns/jscode2session?appid=wx08afdb587195d891&secret=f618055699c8fc45c3a6d32a10dfa7e8&js_code={js_code}&grant_type=authorization_code'
        openId = httpx.get(url).json()['openid']
        user = User.objects.filter(openId=openId)
        # times = (datetime.datetime.now() + datetime.timedelta(seconds=10)).strftime("%Y-%m-%d %H:%M:%S")
        # tokenTime = time.mktime(time.strptime(times, '%Y-%m-%d %H:%M:%S'))
        if user :
            print('用户已经存在')
            user = User.objects.filter(openId=openId).first()
            nickName = user.nickName
            id = user.id
            userImage = user.userImage
            heartWallpapwer = json.loads(user.heartWallpaper)
            token = jwt.encode({'user': openId}, key=settings.SECRET_KEY, algorithm='HS256')
        else:
            us = UserSerializer(data={'addTime':addTime,'openId':openId})
            if us.is_valid(raise_exception=True):
                us.save()
            user = User.objects.filter(openId=openId).first()
            nickName = user.nickName
            id = user.id
            userImage = user.userImage
            heartWallpapwer = json.loads(user.heartWallpaper)
            token = jwt.encode({'user':openId}, key=settings.SECRET_KEY, algorithm='HS256')
        loveImageList = []
        for i in heartWallpapwer:
            tableS = list(i.keys())[0]
            imageId = list(i.values())[0]
            table = None
            if tableS=="G":
                table = GourmetFood
            elif tableS=="A":
                table = Appointment
            elif tableS == "C":
                table = Child
            elif tableS == "F":
                table = Family
            loveImage = table.objects.filter(id=imageId).first().maximage
            item = {'loveImage':loveImage,'id':i}
            loveImageList.append(item)
        return Response({'userJwt':token,'nickName':nickName,'userId':id,'userImage':userImage,'heartWallpapwer':loveImageList})