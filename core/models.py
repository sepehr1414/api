from tkinter import Widget
from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self) -> str:
        return f'{self.name} live in {self.location} and his email is {self.email}'
