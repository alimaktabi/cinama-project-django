from django.db import models


class Cinema(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    capacity = models.IntegerField()
    address = models.TextField()
    about = models.TextField()


class Movie(models.Model):
    Name = models.CharField(max_length=50)
    length = models.IntegerField()
    year = models.IntegerField()
    director = models.CharField(max_length=50)
    genre = models.CharField(max_length=30)
    about = models.TextField()


class Sans(models.Model):
    movie_name = models.Foreignkey(Movie, on_delete=models.CASCADE)
    start_time = models.Datetime
    price = models.IntegerField


class Ticket(models.Model):
    name = models.Foreignkey(Movie , on_delete=models.PROTECT)
    movie = models.Foreignkey(Sans , on_delete=models.CASCADE)
    count = models.IntegerField
    seat = models.IntegerField

