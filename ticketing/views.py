from django.shortcuts import render


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