from django.urls import path
from .views import AlbumList, AlbumDetail, AlbumCreate, AlbumUpdate, AlbumDelete, CoverCreate, SongCreate, CoverCreate, SongCreate

urlpatterns = [
    path('', AlbumList.as_view(), name='albums-home'),
    path('<int:pk>', AlbumDetail.as_view(), name='album-detail'),
    path('add', AlbumCreate.as_view(), name='add-album'),
    path('edit/<int:pk>', AlbumUpdate.as_view(), name='edit-album'),
    path('delete/<int:pk>', AlbumDelete.as_view(), name='delete-album'),
    path('cover/add/<int:pk>', CoverCreate.as_view(), name='add-cover'),
    path('song/add/<int:pk>', SongCreate.as_view(), name='add-song'),
]