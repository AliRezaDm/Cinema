from django.urls import path
from ticketing import views

urlpatterns =  [
    path('Movie/', views.movie_list, name = 'movie_list'),
    path('Cinema/', views.cinema_list, name = 'cinema_list'),
    path('movie_details/<int:movie_id>/', views.movie_details, name = 'movie_details')
]