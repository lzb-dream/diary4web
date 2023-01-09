import random
from api.models import GourmetFood,Appointment,Child,Family
from rest_framework.views import APIView,Response
import jwt
from django.conf import settings

class GetWallPaper(APIView):
    def get(self,request):
        try:
            identification = request.GET.get('tableName') # 标识
        except:
            return Response({'error':'非法请求'},status=400)
        TableName = None
        if identification == 'GourmetFood':
            TableName = GourmetFood
        elif identification == 'Appointment':
            TableName = Appointment
        elif identification == 'Child':
            TableName = Child
        elif identification == 'Family':
            TableName = Family
        count = TableName.objects.all().count()
        indexList = []
        def getIndex():
            index = random.randint(0,count-1)
            if index in indexList:
                getIndex()
            else:
                indexList.append(index)
        for i in range(20):
            getIndex()
        imageList = []
        for w in indexList:
            data = TableName.objects.all()[w]
            image = {'maxImage': data.maximage,
                     'minImage':data.minimage,
                     'id':data.id}
            imageList.append(image)

        return Response({'data':imageList})

    def post(self, request):
        import datetime, time
        data = request.data
        if data.get('user') == 'stranger':
            times = (datetime.datetime.now() + datetime.timedelta(minutes=1)).strftime("%Y-%m-%d %H:%M:%S")
            tokenTime = time.mktime(time.strptime(times, '%Y-%m-%d %H:%M:%S'))
            token = jwt.encode({'user': 'stranger','exp':tokenTime}, key=settings.SECRET_KEY, algorithm='HS256')
            print(tokenTime)
            print(token)
            return Response({'token': token})
        else:
            return Response({'error': '非法请求'},status=401)

    def delete(self,request):
        identification = request.data['tableName']
        id = request.data['id']

        table = None
        if identification == 'GourmetFood':
            table = GourmetFood
        elif identification == 'Appointment':
            table = Appointment
        elif identification == 'Child':
            table = Child
        elif identification == 'Family':
            table = Family
        table.objects.get(id=id).delete()
        return Response({'message':f'{id}删除成功'})
