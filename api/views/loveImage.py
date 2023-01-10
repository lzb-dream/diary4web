from ..Serializers import UserSerializer,User
from rest_framework.views import APIView,Response
import json
from ..models import Family,GourmetFood,Child,Appointment


class LoveImage(APIView):
    def post(self,request):
        data = request.data
        image = data.get('image')
        if not image:
            return Response({'error':'image不存在'},status=500)
        user = User.objects.filter(openId=data.get('openId')).first()
        heartWallpaper = json.loads(user.heartWallpaper)
        heartWallpaper.insert(0,image)
        user.heartWallpaper = json.dumps(heartWallpaper)
        user.save()
        return Response({'message':'ok'})


    def get(self,request):
        pass

    def delete(self,request):
        data = request.data
        image = data.get('image')
        user = User.objects.filter(openId=data.get('openId')).first()
        heartWallpaper = json.loads(user.heartWallpaper)
        heartWallpaper.remove(image)
        user.heartWallpaper = json.dumps(heartWallpaper)
        user.save()
        return Response({'message':'ok'})
