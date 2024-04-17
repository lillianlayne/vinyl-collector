from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('vinyls/', views.vinyls_index, name="index"),
    path('vinyls/<int:vinyl_id>/', views.vinyls_detail, name="detail"),
    path('vinyls/create/', views.VinylCreate.as_view(), name='vinyls_create'),
    path('vinyls/<int:pk>/update/', views.VinylsUpdate.as_view(), name='vinyls_update'),
    path('vinyls/<int:pk>/delete/', views.VinylDelete.as_view(), name='vinyls_delete'),
    path('vinyls/<int:vinyl_id>/add_song/', views.add_song, name="add_song"),
    path('genres/create/', views.GenreCreate.as_view(), name="genre_create"), 
    path('vinyls/<int:vinyl_id>/assoc_genre/<int:genre_id>', views.assoc_genre, name='assoc_genre'), 
    path('genres/', views.GenreList.as_view(), name='genre_index'),
    path('genres/<int:pk>/', views.GenreDelete.as_view(), name='genre_delete'),
    path('vinyls/<int:vinyl_id>/add_photo/', views.add_photo, name='add_photo')
]