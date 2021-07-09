from django.urls import path
from . import views
app_name = 'chat'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('register/', views.register, name='register'),
    path('updateuser/<int:user_id>/', views.updateuser, name='updateuser'),
    path('searchuser/', views.searchuser, name='searchuser'),
    path('chatroom/', views.chatroom, name='chatroom'),


]