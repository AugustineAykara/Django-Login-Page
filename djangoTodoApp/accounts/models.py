from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class userTodo(models.Model):
    userName = models.ForeignKey(User, on_delete = models.CASCADE)
    todoTitle = models.CharField(max_length = 100)
    todoDescription = models.TextField()