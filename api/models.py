# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Child(models.Model):
    addtime = models.DateTimeField()
    maximage = models.CharField(max_length=255,unique=True)
    minimage = models.CharField(max_length=255,unique=True)
    class Meta:
        db_table = 'child'
        verbose_name = '孩童'
        verbose_name_plural = verbose_name

class Family(models.Model):
    addtime = models.DateTimeField()
    maximage = models.CharField(max_length=255,unique=True)
    minimage = models.CharField(max_length=255,unique=True)
    class Meta:
        db_table = 'family'
        verbose_name = '家庭'
        verbose_name_plural = verbose_name

class Appointment(models.Model):
    addtime = models.DateTimeField()
    maximage = models.CharField(max_length=255,unique=True)
    minimage = models.CharField(max_length=255,unique=True)
    class Meta:
        db_table = 'appointment'
        verbose_name = '相约'
        verbose_name_plural = verbose_name


class GourmetFood(models.Model):
    addtime = models.DateTimeField()
    maximage = models.CharField(max_length=255,unique=True)
    minimage = models.CharField(max_length=255,unique=True)
    class Meta:
        db_table = 'gourmetFood'
        verbose_name = '美食'
        verbose_name_plural = verbose_name


class User(models.Model):
    openId = models.CharField(max_length=255,unique=True)
    nickName = models.CharField(max_length=255,default='用户')
    addTime = models.DateTimeField()
    userImage = models.CharField(max_length=255,default='static/set/user.png')
    heartWallpaper = models.TextField(default='[]')
    writeBackgroundWallpaper = models.CharField(max_length=255,blank=True)
    readBackgroundWallpaper = models.CharField(max_length=255,blank=True)
    diaryCount = models.IntegerField(default=0)
    diaryPassword = models.CharField(max_length=255,blank=True)

    class Meta:
        managed = True
        db_table = 'user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

class Diary(models.Model):
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    diary = models.TextField()
    video = models.TextField(default='[]')
    videoPhoto = models.TextField(default='[]')
    image = models.TextField(default='[]')
    writeTime = models.DateTimeField()
    mood = models.CharField(max_length=20)
    weather = models.CharField(max_length=20)
    address = models.CharField(max_length=255,blank=True)

    def __str__(self):
        return self.user.nickName

    class Meta:
        managed = True
        db_table = 'diary'
        verbose_name = '用户日记'
        verbose_name_plural = verbose_name
