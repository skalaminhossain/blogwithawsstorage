from django.db import models

# Create your models here.
class Blog(models.Model):
    discription = models.TextField()
    timecase = models.DateTimeField( auto_now_add=True)
    thumbnail = models.ImageField(upload_to='album/skalaminhossain/')


class Personalblog(models.Model):
    blogtitle = models.TextField()
    description = models.TextField()
    timecase = models.DateTimeField( auto_now_add=True)
    thumbnail = models.ImageField(upload_to='album/skalaminhossain/')
