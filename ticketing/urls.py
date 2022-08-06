from django.urls import path
from ticketing import views

url_pattern = [
    path('ticketing/Movie/', views.movie_list),
    path('ticketing/Cinema/', views.cinema_list)
]