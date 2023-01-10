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

class DiarySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True, required=False)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    diary = serializers.CharField()
    video = serializers.CharField(required=False,allow_blank=True)
    videoPhoto = serializers.CharField(required=False,allow_blank=True)
    image = serializers.CharField(required=False,allow_blank=True)
    writeTime = serializers.DateTimeField()
    mood = serializers.CharField(max_length=20,required=False,allow_blank=True)
    weather = serializers.CharField(max_length=20,required=False,allow_blank=True)
    address = serializers.CharField(max_length=255,required=False,allow_blank=True)

    def validate(self, attrs):
        return attrs

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance,key,value)
        instance.save()
        return instance

    def create(self, validated_data):
        diary = Diary.objects.create(**validated_data)
        return diary