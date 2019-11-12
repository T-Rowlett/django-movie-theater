from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.TextField()
    rating = models.TextField()
    genre = models.TextField()
    runtime = models.TimeField()

class Showing(models.Model):
    movie = models.ForeignKey(Movie, on_delete='PROTECT')
    showtime = models.TextField()

class Ticket(models.Model):
    name = models.TextField()
    purschase_at = models.TimeField()
    showing = models.ForeignKey(Showing, on_delete="PROTECT")