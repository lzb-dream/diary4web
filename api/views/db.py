from rest_framework.views import APIView,Response
from ..models import Diary,User,Userold,Diaryold
from ..Serializers import DiarySerializer,UserSerializer
class Zhuan(APIView):
    def get(self,request):
        # nickname = models.CharField(db_column='nickName', max_length=20)  # Field name made lowercase.
        # openid = models.CharField(db_column='openId', unique=True, max_length=255)  # Field name made lowercase.
        # addtime = models.DateTimeField(db_column='addTime')  # Field name made lowercase.
        olddiary = Diaryold.objects.all()
        for i in olddiary:
            olduserId = i.user_id
            openid = Userold.objects.filter(id=olduserId).first().openid
            newuserid = User.objects.filter(openId=openid).first().id
            Diary(user_id=newuserid,diary=i.diary,address=i.address,
                  mood=i.mood,writeTime=i.writetime,weather=i.weather).save()
            print('添加')
        return Response({'message':'ok'})

