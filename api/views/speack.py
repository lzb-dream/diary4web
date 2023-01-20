from rest_framework.views import APIView,Response

class S(APIView):
    def get(self,request):
        with open('static/speack.txt',mode='r') as f:
            txt = f.read()
        return Response({'txt':txt})
