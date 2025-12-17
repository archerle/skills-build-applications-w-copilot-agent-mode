from djongo import models

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        db_table = 'teams'
    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team_id = models.CharField(max_length=24)
    class Meta:
        db_table = 'users'
    def __str__(self):
        return self.name


class Activity(models.Model):
    user_id = models.CharField(max_length=24)
    type = models.CharField(max_length=50)
    duration = models.IntegerField()  # minutos
    date = models.DateField()
    class Meta:
        db_table = 'activities'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    difficulty = models.CharField(max_length=50)
    class Meta:
        db_table = 'workouts'


class Leaderboard(models.Model):
    user_id = models.CharField(max_length=24)
    score = models.IntegerField()
    class Meta:
        db_table = 'leaderboard'
