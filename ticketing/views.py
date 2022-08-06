from django.shortcuts import render


from ticketing.models import Movie, Cinema


def movie_list(request):
    movies = Movie.objects.all()
    context = {
        'design' : movies
    }
    return render(request, 'design.html', context)


def cinema_list(request):
    cinemas = Cinema.objects.all()
    response_text = '''
            <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <script> </script>
                <title>List of Cinema </title>
        </head>
        <body>
          <h1>
              List of Cinemas in the Country
          </h1> 
          <u1>
              {}
          </u1> 
        </body>
        </html>
    '''.join('<li> {} <li>'.format(cinema) for cinema in cinemas)
