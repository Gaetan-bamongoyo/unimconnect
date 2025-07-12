from django.urls import path
from .views import *

app_name = "postapp" 

urlpatterns = [
    path('', loginPage, name='login'),
    path('createuser', createUser, name='createuser'),
    path('homepage', dashboardPage, name='homepage'),
    path('loginuser', loginUser, name='loginuser'),
    path('createpost', createPost, name='createpost'),
    path('createlike/<int:pk>', createLike, name='createlike'),
    path('createcommentaire', createCommentaire, name='createcommentaire'),
    path('commentairepage/<int:pk>', commentairePage, name='commentairepage')
] 