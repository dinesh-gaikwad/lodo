from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('game/', views.game, name='game'),
    path('room/', views.room, name='room'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
]
