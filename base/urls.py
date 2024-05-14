from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('movies/<str:pk>/',views.movies,name="movies"),
    path('chat-room/<str:pk>/',views.chatroom,name="chat-room"),
    path('login/',views.logme,name="login"),
    path('logout/',views.logmeout,name="logout"),
    path('profile/<str:pk>/',views.profile,name="profile"),
    path('register/',views.register,name="register"),
    path('editpfp/<str:pk>/',views.profileEdit,name="editpfp"),
]