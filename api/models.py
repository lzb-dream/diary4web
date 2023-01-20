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
    diaryStatus = models.BooleanField(default=False)

    class Meta:
        managed = True
        db_table = 'userNew'
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
        db_table = 'diaryNew'
        verbose_name = '用户日记'
        verbose_name_plural = verbose_name

class Userold(models.Model):
    id = models.BigAutoField(primary_key=True)

    nickname = models.CharField(db_column='nickName', max_length=20)  # Field name made lowercase.
    openid = models.CharField(db_column='openId', unique=True, max_length=255)  # Field name made lowercase.
    addtime = models.DateTimeField(db_column='addTime')  # Field name made lowercase.

    updatetime = models.DateTimeField(db_column='updateTime', blank=True, null=True)  # Field name made lowercase.
    headportrait = models.CharField(db_column='headPortrait', max_length=255)  # Field name made lowercase.
    state = models.IntegerField()
    flowers = models.IntegerField()
    money = models.DecimalField(max_digits=6, decimal_places=2)
    diarynumber = models.IntegerField(db_column='diaryNumber')  # Field name made lowercase.
    praise = models.IntegerField()
    diarypassword = models.IntegerField(db_column='diaryPassword', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'user'

class Diaryold(models.Model):
    id = models.BigAutoField(primary_key=True)

    diary = models.TextField()
    writetime = models.DateTimeField(db_column='writeTime')  # Field name made lowercase.
    mood = models.CharField(max_length=10)
    weather = models.CharField(max_length=10)
    address = models.CharField(max_length=255)

    thumbupnumber = models.IntegerField(db_column='thumbUpNumber')  # Field name made lowercase.
    flowercount = models.IntegerField(db_column='flowerCount')  # Field name made lowercase.
    squareswitch = models.IntegerField(db_column='squareSwitch')  # Field name made lowercase.
    user_id = models.BigIntegerField()
    image = models.TextField()
    video = models.TextField()
    updatetime = models.DateTimeField(db_column='updateTime', blank=True, null=True)  # Field name made lowercase.
    videophoto = models.TextField(db_column='videoPhoto')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'diary'