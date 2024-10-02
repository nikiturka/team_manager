from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    teams = models.ManyToManyField(Team, related_name='members')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
