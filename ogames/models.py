from django.db import models


class UploadCsv(models.Model):
    file = models.FileField(upload_to='csv')


class Noc(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=50, unique=True)
    noc = models.ForeignKey(Noc, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Game(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Sport(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=50, unique=True)
    year = models.IntegerField()
    season = models.CharField(max_length=50)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='events')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='events')

    def __str__(self):
        return self.name


class Athlete(models.Model):
    name = models.CharField(max_length=50)
    sex = models.CharField(max_length=20)
    age = models.IntegerField()
    height = models.CharField(max_length=20)
    weight = models.CharField(max_length=20)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="athletes")
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE, related_name='athletes')

    def __str__(self):
        return self.name


class AthleteEvent(models.Model):
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, related_name='athlete_event') 
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    medal = models.CharField(max_length=50, null=True)







