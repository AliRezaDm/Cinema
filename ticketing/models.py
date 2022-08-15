from django.db import models


class Movie(models.Model):
    """ movie presentation """
    name = models.CharField('Title', max_length=100)
    director = models.CharField('Director', max_length=50)
    year = models.IntegerField('Release Date')
    description = models.TextField('Story')
    length = models.IntegerField('Duration')
    image = models.ImageField('Poster', upload_to = 'media', blank = True, null = True)
    MOVIES_RATES = [
        ('G', 'General Audience'),
	    ('PG', 'Parental Guidance'),
	    ('PG-13', 'Parental Guidance Strongly Cautioned'),
	    ('R', 'Restricted'),
	    ('NC-17', 'Clearly Adult')
    ]
    
    rates = models.CharField('Rate', max_length=5, choices=MOVIES_RATES, blank = True, null = True, default= 'PG')

    def __str__(self):
        return self.name


class Cinema(models.Model):
    
    cinema_code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    city = models.CharField('Location', max_length=30, default='Tehran')
    capacity = models.IntegerField('Seats')
    phone = models.CharField('Contact', max_length=20, null=True)
    address = models.TextField()

    def __str__(self):
        return self.name


class ShowTime(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.PROTECT, verbose_name= 'Title')
    cinema = models.ForeignKey('Cinema', on_delete=models.PROTECT)
    start_time = models.DateTimeField()
    price = models.IntegerField()
    salable_sits = models.IntegerField('Availabe Seats')
    free_sits = models.IntegerField('Number of Seats')

    SALE_NOT_STARTED = 1
    SALE_OPEN = 2
    TICKET_SOLED = 3
    SALE_CLOSED = 4
    MOVIE_PLAYED = 5
    SHOW_CANCELED = 6

    status_choices = (
        (SALE_NOT_STARTED, 'sales not started yet'),
        (SALE_OPEN, 'sale is open'),
        (TICKET_SOLED, 'tickets are soled'),
        (SALE_CLOSED, 'sale is over'),
        (MOVIE_PLAYED, 'the show is over'),
        (SHOW_CANCELED, 'the show is not current available')
    )


status = models.IntegerField(choices='status_choices')


def __str__(self):
    return f'{self.movie} - {self.cinema} - {self.start_time} '
