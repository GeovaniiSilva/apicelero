from django.shortcuts import render, HttpResponse, get_object_or_404
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, ListCreateAPIView
from django.dispatch import receiver
from django.db.models.signals import post_save
import csv

from ogames.models import *
from ogames.serializers import *



class UploadCsvCreateAPIView(CreateAPIView):

    model = UploadCsv
    serializer_class = UploadCsvSerializer

    @receiver(post_save, sender=UploadCsv)
    def fileupload_post_save(sender, instance, *args, **kwargs):
        with open(instance.file.path, 'r') as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                noc_serializer = NocSerializer(data={"name": row["noc"]})
                if noc_serializer.is_valid():
                    noc_serializer.save()
                    noc_object = Noc.objects.get(name=row["noc"])
                team_serializer = TeamSerializer(data={"name": row["team"], "noc": noc_object.id})
                if team_serializer.is_valid():
                    team_serializer.save()
                    team_object = Team.objects.get(name=row["team"])
                game_serializer = GameSerializer(data={"name": row["games"]})
                if game_serializer.is_valid():
                    game_serializer.save()
                    game_object = Game.objects.get(name=row["games"])
                city_serializer = CitySerializer(data={"name": row["city"]})
                if city_serializer.is_valid():
                    city_serializer.save()
                    city_object = City.objects.get(name=row["city"])
                sport_serializer = SportSerializer(data={"name": row["sport"]})
                if sport_serializer.is_valid():
                    sport_serializer.save()
                    sport_object = Sport.objects.get(name=row["sport"])
                event_serializer = EventSerializer(data={"name": row["event"]})
                if event_serializer.is_valid():
                    event_serializer.save()
                    event_object = Event.objects.get(name=row["event"])
                athlete_serializer = AthleteSerializer(data={"name": row["name"], "sex": row["sex"], "age": row["age"], "height": row["height"], "weight": row["weight"], "team": team_object.id})
                if athlete_serializer.is_valid():
                    athlete_serializer.save()
                    athlete_object = Athlete.objects.get(name=row["name"])
                athlete_event_serializer = AthleteEventSerializer(data={"athlete": athlete_object.id, "game": game_object.id, "year": row["year"], "season": row["season"], "city": city_object.id, "sport": sport_object.id, "event": event_object.id, "medal": row["medal"]})
                if athlete_event_serializer.is_valid():
                    athlete_event_serializer.save()



class NocListCreateAPIView(ListCreateAPIView):
    model = Noc
    serializer_class = NocSerializer
    queryset = Noc.objects.all()



class TeamListCreateAPIView(ListCreateAPIView):
    model = Team
    serializer_class = TeamSerializer
    queryset = Team.objects.all()


class AthleteListCreateAPIView(ListCreateAPIView):
    model = Athlete
    serializer_class = AthleteSerializer
    #queryset = Athlete.objects.all()

    def get_queryset(self):
        if self.request.GET.get('sex'):
            queryset = Athlete.objects.filter(sex__icontains=self.request.GET.get('sex'))
        elif self.request.GET.get('team'):
            queryset = Athlete.objects.filter(team__name__icontains=self.request.GET.get('team'))
        elif self.request.GET.get('age'):
            queryset = Athlete.objects.filter(age__iexact=self.request.GET.get('age'))
        elif self.request.GET.get('aboveage'):
            queryset = Athlete.objects.filter(age__gte=self.request.GET.get('aboveage'))
        elif self.request.GET.get('belowage'):
            queryset = Athlete.objects.filter(age__lte=self.request.GET.get('belowage'))
        elif self.request.GET.get('height'):
            queryset = Athlete.objects.filter(height__iexact=self.request.GET.get('height'))
        elif self.request.GET.get('aboveheight'):
            queryset = Athlete.objects.filter(height__gte=self.request.GET.get('aboveheight'))
        elif self.request.GET.get('belowheight'):
            queryset = Athlete.objects.filter(height__lte=self.request.GET.get('belowheight'))
        elif self.request.GET.get('weight'):
            queryset = Athlete.objects.filter(weight__iexact=self.request.GET.get('weight'))
        elif self.request.GET.get('aboveweight'):
            queryset = Athlete.objects.filter(weight__gte=self.request.GET.get('aboveweight')).exclude(weight='NA')
        elif self.request.GET.get('belowweight'):
            queryset = Athlete.objects.filter(weight__lte=self.request.GET.get('belowweight')).exclude(weight='NA')
        
        else:
            queryset = Athlete.objects.all()
        
        return queryset


class GameListCreateAPIView(ListCreateAPIView):
    model = Game
    serializer_class = GameSerializer
    queryset = Game.objects.all()


class CityListCreateAPIView(ListCreateAPIView):
    model = City
    serializer_class = CitySerializer
    queryset = City.objects.all()


class EventListCreateAPIView(ListCreateAPIView):
    model = Event
    serializer_class = EventSerializer
    queryset = Event.objects.all()


class SportListCreateAPIView(ListCreateAPIView):
    model = Sport
    serializer_class = SportSerializer
    queryset = Sport.objects.all()


class AthleteEventListAPIView(ListCreateAPIView):

    model = AthleteEvent
    serializer_class = AthleteEventSerializer
    queryset = AthleteEvent.objects.all()

    def get_queryset(self):
        if self.request.GET.get('athlete'):
            queryset = AthleteEvent.objects.filter(athlete__name__icontains=self.request.GET.get('athlete'))
        elif self.request.GET.get('game'):
            queryset = AthleteEvent.objects.filter(game__name__icontains=self.request.GET.get('game'))
        elif self.request.GET.get('year'):
            queryset = AthleteEvent.objects.filter(year=self.request.GET.get('year'))
        elif self.request.GET.get('season'):
            queryset = AthleteEvent.objects.filter(season__icontains=self.request.GET.get('season'))
        elif self.request.GET.get('city'):
            queryset = AthleteEvent.objects.filter(city__name__icontains=self.request.GET.get('city'))
        elif self.request.GET.get('sport'):
            queryset = AthleteEvent.objects.filter(sport__name__icontains=self.request.GET.get('sport'))
        elif self.request.GET.get('event'):
            queryset = AthleteEvent.objects.filter(event__name__icontains=self.request.GET.get('event'))
        elif self.request.GET.get('medal'):
            queryset = AthleteEvent.objects.filter(medal__icontains=self.request.GET.get('medal'))
        else:
            queryset = AthleteEvent.objects.all()
               
        return queryset


class AthleteEventRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):

    model = AthleteEvent
    serializer_class = AthleteEventSerializer
    queryset = AthleteEvent.objects.all()