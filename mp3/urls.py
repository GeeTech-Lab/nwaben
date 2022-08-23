from django.urls import path
from . import views


app_name = 'mp3'

urlpatterns = [
    path('', views.AlbumList.as_view(), name='album_list'),
    path('<slug:slug>/', views.AlbumDetail.as_view(), name='album_detail'),
    path('album/add/', views.AlbumCreate.as_view(), name='add_album'),
    path('album/<slug:slug>/', views.AlbumUpdate.as_view(), name='update_album'),
    path('album/<slug:slug>/delete', views.AlbumDelete.as_view(), name='delete_album'),
    path('songs/', views.SongList.as_view(), name='song_list'),
    path('song/<slug:slug>/add/', views.SongCreate.as_view(), name='add_song'),
    path('song/<slug:slug>/delete', views.SongDelete.as_view(), name='delete_song'),
]