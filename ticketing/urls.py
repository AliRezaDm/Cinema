from django.urls import path
from ticketing import views

urlpatterns =  [
    path('Movie/', views.movie_list, name = 'movie_list'),
    path('Cinema/', views.cinema_list, name = 'cinema_list')
]