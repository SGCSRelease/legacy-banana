from django.db import models

class Post(models.Model):
    author = models.ForeignKey('User')
    title = models.CharField(max_length=100)
    content = models.TextField()
    written_date = models.DateField()


class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

