from django.urls import path
from . import views


urlpatterns = [
    path('artists/', views.artist_list),
    path('artists/<int:artist_pk>/', views.artist_detail),
    path('musics/', views.music_list),
    path('musics/<int:music_pk>', views.music_detail),
]
