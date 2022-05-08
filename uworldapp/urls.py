from django.urls import path
from . import views

urlpatterns =[
    path('',views.home,name='home'),
    path('about/', views.ClubMan, name="about"),
    path('create/', views.createPlayer.as_view(), name="create"),
    path('allplayers/', views.ShowPlayers.as_view(), name="players"),
    path('detail/<int:idx>', views.OnePlayer, name="detail"),
    path('delete/<int:pk>/', views.DeletePlayer.as_view(), name="delete"),
    path('update/<int:pk>/', views.UpdatePlayer.as_view(), name="update"),
    path('players/<int:player_id>/add_photo/', views.add_photo, name='add_photo'),
]