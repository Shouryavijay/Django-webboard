from django.db import models

class Board(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Topic(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)

class Post(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    message = models.TextField()
