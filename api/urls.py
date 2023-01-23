from django.urls import path
from .views.login import Login
from .views.randomWallpaper import GetWallPaper
from .views.wallpaper import Add
from .views.loveImage import LoveImage
from .views.diary import DiaryManagement,Media
from .views.speack import S
from .views.userUp import UserUp
# from .views.db import Zhuan
urlpatterns = [
    path('login',Login.as_view()),
    path('loveimage',LoveImage.as_view()),
    path('diary',DiaryManagement.as_view()),
    path('media', Media.as_view()),
    path('speack', S.as_view()),
    path('userup', UserUp.as_view()),
    # path('db', Zhuan.as_view()),






    path('getWallPaper',GetWallPaper.as_view()),
    path('add',Add.as_view())
]