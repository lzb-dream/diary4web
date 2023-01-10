from django.urls import path
from .views.login import Login
from .views.randomWallpaper import GetWallPaper
from .views.wallpaper import Add
from .views.loveImage import LoveImage
from .views.diary import DiaryManagement,Media


urlpatterns = [
    path('login',Login.as_view()),
    path('loveimage',LoveImage.as_view()),
    path('diary',DiaryManagement.as_view()),
    path('media', Media.as_view()),







    path('getWallPaper',GetWallPaper.as_view()),
    path('add',Add.as_view())
]