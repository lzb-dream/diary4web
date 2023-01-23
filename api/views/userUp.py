from rest_framework.views import APIView,Response
from ..models import User

class UserUp(APIView):
    def put(self,request):
        data = request.data
        openId = data.get('openId')
        print(openId)
        nickName = data.get('nickName')
        user = User.objects.filter(openId=openId).first()
        user.nickName = nickName
        user.save()
        return Response({'message':'ok'})