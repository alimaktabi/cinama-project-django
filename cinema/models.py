import random

from django.db import models


class Cinema(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    capacity = models.IntegerField()
    address = models.TextField()
    about = models.TextField()

    def __str__(self):
        return self.name


class Movie(models.Model):
    Name = models.CharField(max_length=50)
    length = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    director = models.CharField(max_length=50)
    genre = models.CharField(max_length=30)
    about = models.TextField()

    def __str__(self):
        return self.Name


class Sans(models.Model):
    movie_name = models.ForeignKey('Movie', on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    price = models.IntegerField(default=10000)


class Ticket(models.Model):
    name = models.ForeignKey('Movie', on_delete=models.PROTECT)
    movie = models.ForeignKey('Sans', on_delete=models.CASCADE)
    count = models.IntegerField(default=1)
    seat = models.IntegerField(default=0)
