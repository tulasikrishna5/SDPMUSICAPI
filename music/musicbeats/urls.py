from django.urls import path
from . import views

urlpatterns = [
    path('songs/', views.songs, name='songs'),
    path('songs/<int:id>', views.songpost, name='songpost'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('Anirudh/', views.Anirudh, name='Anirudh'),
    path('Hesham/', views.Hesham, name='Hesham'),
    path('Revanth/', views.Revanth, name='Revanth'),
    path('Beat/', views.Beat, name='Beat'),
    path('Melody/', views.Melody, name='Melody'),
    path('bgm/', views.bgm, name='bgm'),
    ]
