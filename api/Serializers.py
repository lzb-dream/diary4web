from rest_framework import serializers
from .models import User,Diary
class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True,required=False)
    openId = serializers.CharField(max_length=255,required=True)
    nickName = serializers.CharField(max_length=255,default='用户',required=False)
    addTime = serializers.DateTimeField()
    userImage = serializers.CharField(max_length=255,default='static/set/user.png')
    heartWallpaper = serializers.CharField(required=False)
    writeBackgroundWallpaper = serializers.CharField(max_length=255,required=False)
    readBackgroundWallpaper = serializers.CharField(max_length=255,required=False)
    diaryCount = serializers.IntegerField(default=0)

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        return user