from django.db import models

class Player(models.Model):
    full_name = models.CharField(max_length=35)
    age = models.IntegerField(default=0)
    region = models.CharField(max_length=20)
    date_of_joining = models.PositiveIntegerField(default=0)
    this_year_credit = models.PositiveIntegerField(default=0)
    total_credit = models.PositiveIntegerField(default=0)
    total_awards = models.PositiveIntegerField(default=0)
    total_titles = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    no_of_games = models.IntegerField(default=0)
    
    
    def __str__(self):
        return self.full_name
    
class league(models.Model):
    name = models.CharField(max_length=50)
    teams = models.ManyToManyField(Player, related_name='leagues')
    
    
    def __str__(self):
        return self.name
    
class state(models.Model):
    name = models.CharField(max_length=40)
    teams = teams = models.ManyToManyField(Player, related_name='state')