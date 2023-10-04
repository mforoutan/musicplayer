from django.db import models
from django.contrib.auth.models import User


class Song(models.Model):
    STATUS_CHOICES = [
        ('r', 'released'),
        ('u', 'unreleased'),
    ]
    GENRES = [
        ('hip', 'Hip-Hop/Rap'),
        ('rab', 'R&B'),
        ('pop', 'Pop'),
        ('metal', 'Metal'),
        ('rock', 'Rock'),
        ('alt', 'Alternative'),
        ('dance', 'Dance'),
    ]
    name = models.CharField(max_length=200)
    length = models.IntegerField()
    released = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS_CHOICES, default='u', max_length=200)
    explicit = models.BooleanField(default=False)
    genre = models.CharField(choices=GENRES, default='Pop', max_length=200)
    artist = models.CharField(max_length=200, default='unknown')
    album = models.CharField(max_length=200, default='unknown')
