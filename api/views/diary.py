from ..Serializers import UserSerializer,User,Diary,DiarySerializer
from rest_framework.views import APIView,Response
import json
from ..models import Family,GourmetFood,Child,Appointment


class DiaryManagement(APIView):
    def post(self,request):
        data = request.data
        writeTime = data.get('writeTime')
        print(data)
        openId = data.get('openId')
        user_id = User.objects.filter(openId=openId).first().id
        del data['openId']
        data['user'] = user_id
        Ds = DiarySerializer(data=data)
        if Ds.is_valid(raise_exception=True):
            Ds.save()
        diaryId = Diary.objects.filter(user_id=user_id,writeTime=writeTime).first().id
        return Response({'diaryId':diaryId})

import jwt
from django.conf import settings
class Media(APIView):
    def post(self,request):
        data = request.data
        print(data)
        token = request.META.get("HTTP_AUTHORIZATION")
        key = settings.SECRET_KEY
        try:
            tokenParse = jwt.decode(token,key,algorithms='HS256')
        except:
            return Response({'error':'token错误'})
        openId = tokenParse.get('user')

        mediaFile = data.get('media')
        diaryId = data.get('diaryId')
        type = data.get('type')
        writeTime = data.get('writeTime')
        fileName = str(data.get('index'))+openId+writeTime.replace(' ','T').replace(':','-')+'.'+str(mediaFile).split('.')[-1]
        src = f'static/{type}/{fileName}'
        with open(src,mode='wb') as f:
            for i in mediaFile:
                f.write(i)
        print(fileName)
        return Response({'message':'ok'})
