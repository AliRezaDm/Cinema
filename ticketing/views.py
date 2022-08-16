from django.shortcuts import get_object_or_404, render
from .models import Movie, Cinema


def movie_list(request):
    movies = Movie.objects.all()
    context = {
        'movies' : movies
    }
    return render(request, 'ticketing/movie_list_view.html', context)


def cinema_list(request):
    cinemas = Cinema.objects.all()
    context = {
        'cinemas' : cinemas
    }
    return render(request, 'ticketing/cinema_list_view.html', context)

def movie_details(request, movie_id):
    movie = get_object_or_404(Movie, id = movie_id)
    context = {
        'movie' : movie
    }    
    return render(request, 'ticketing/movie_details_view.html', context)

