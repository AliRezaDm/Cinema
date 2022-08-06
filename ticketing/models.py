from django.db import models


class Movie(models.Model):
    """ movie presentation """
    name = models.CharField(max_length=100)
    director = models.CharField(max_length=50)
    year = models.IntegerField()
    description = models.TextField()
    length = models.IntegerField()

    def __str__(self):
        return self.name


class Cinema(models.Model):
    """ Cinema's names """
    cinema_code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=30, default='Tehran')
    capacity = models.IntegerField()
    phone = models.CharField(max_length=20, null=True)
    address = models.TextField()

    def __str__(self):
        return self.name


class ShowTime(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.PROTECT)
    cinema = models.ForeignKey('Cinema', on_delete=models.PROTECT)
    start_time = models.DateTimeField()
    price = models.IntegerField()
    salable_sits = models.IntegerField()
    free_sits = models.IntegerField()

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
    return '{} - {} - {} '.format(self.movie, self.cinema, self.start_time)
