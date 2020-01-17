from django.shortcuts import render, HttpResponse, get_object_or_404
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, ListCreateAPIView
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.reverse import reverse_lazy
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
import csv

from ogames.models import *
from ogames.serializers import *



class ApiRootView(APIView):
    def get(self, request):
        data = {
            'read-csv-url': reverse_lazy('read-csv', request=request),
            'list-create-nocs': reverse_lazy('list-nocs', request=request),
            'list-create-cities': reverse_lazy('list-cities', request=request),
            'list-create-games': reverse_lazy('list-games', request=request),
            'list-create-events': reverse_lazy('list-events', request=request),
            'list-create-sports': reverse_lazy('list-sports', request=request),
            'list-create-teams': reverse_lazy('list-teams', request=request),
            'list-create-athletes': reverse_lazy('list-athletes', request=request),
            'list-create-athlete-events': reverse_lazy('list-athlete-events', request=request)

        }
        return Response(data)



class UploadCsvCreateAPIView(ListCreateAPIView):
    """
    Class based view to upload a CSV file and store all data in the database. 
    """
    model = UploadCsv
    serializer_class = UploadCsvSerializer
    queryset = UploadCsv.objects.all().order_by('id')

    @receiver(pre_save, sender=UploadCsv)
    def fileupload_post_save(sender, instance, *args, **kwargs):
        """
        post save signal to read the csv file and separate the data according to the models, 
        storing them in the database
        """
        with open(instance.file.url, 'r') as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                noc_data={"name": row["NOC"]}
                noc_object, noc_created = Noc.objects.get_or_create(**noc_data)

                team_data={"name": row["Team"], "noc": noc_object}
                team_object, team_created = Team.objects.get_or_create(**team_data)


                game_data={"name": row["Games"]}
                game_object, game_created = Game.objects.get_or_create(**game_data)


                city_data={"name": row["City"]}
                city_object, city_created = City.objects.get_or_create(**city_data)


                sport_data={"name": row["Sport"]}
                sport_object, sport_created = Sport.objects.get_or_create(**sport_data)


                event_data={
                    "name": row["Event"],
                    "year": row["Year"],
                    "season": row["Season"],
                    "city": city_object,
                    "game": game_object,
                    }
                event_object, event_created = Event.objects.get_or_create(**event_data, defaults={'name': row["Event"]})


                athlete_data={
                    "name": row["Name"], 
                    "sex": row["Sex"], 
                    "age": row["Age"], 
                    "height": row["Height"], 
                    "weight": row["Weight"], 
                    "team": team_object,
                    "sport": sport_object,
                    }
                athlete_object, athlete_created = Athlete.objects.get_or_create(**athlete_data)

                athlete_event_data={
                    "athlete": athlete_object, 
                    "event": event_object, 
                    "medal": row["Medal"]
                    }
                athlete_event_object, athlete_event_created = AthleteEvent.objects.get_or_create(**athlete_event_data)




class NocListCreateAPIView(ListCreateAPIView):
    """
    Class based view based on rest_framework.ListCreateAPIView,
    used to create a new NOC data and list all NOCs*.

    NOC = National Olympique Commitee
    """
    model = Noc
    serializer_class = NocSerializer
    queryset = Noc.objects.all()



class NocRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    Class based view based on rest_framework.RetrieveUpdateDestroyAPIView,
    used to show detail, update and destroy a NOC* object.

    NOC = National Olympique Commitee
    """
    model = Noc
    serializer_class = NocSerializer
    queryset = Noc.objects.all()


class TeamListCreateAPIView(ListCreateAPIView):
    """
    Class based view based on rest_framework.ListCreateAPIView,
    used to create a new Team object and list all Team objects.
    """
    model = Team
    serializer_class = TeamSerializer
    queryset = Team.objects.all().order_by('id')


class TeamRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    Class based view based on rest_framework.RetrieveUpdateDestroyAPIView,
    used to show detail, update and destroy a Team object.
    """
    model = Team
    serializer_class = TeamSerializer
    queryset = Team.objects.all()


class AthleteListCreateAPIView(ListCreateAPIView):
    """
    Class based view based on rest_framework.ListCreateAPIView,
    used to create a new Athlete object and list all Athlete objects.
    """
    model = Athlete
    serializer_class = AthleteSerializer
    queryset = Athlete.objects.all().order_by('id')
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['age', 'sex', 'sport', 'team','height','weight']
    search_fields = ['name']


class AthleteRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    Class based view based on rest_framework.RetrieveUpdateDestroyAPIView,
    used to show detail, update and destroy an Athlete object.
    """
    model = Athlete
    serializer_class = AthleteSerializer
    queryset = Athlete.objects.all()


class GameListCreateAPIView(ListCreateAPIView):
    """
    Class based view based on rest_framework.ListCreateAPIView,
    used to create a new Game object and list all Game objects.
    """
    model = Game
    serializer_class = GameSerializer
    queryset = Game.objects.all().order_by('id')



class GameRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    Class based view based on rest_framework.RetrieveUpdateDestroyAPIView,
    used to show detail, update and destroy a Game object.
    """
    model = Game
    serializer_class = GameSerializer
    queryset = Game.objects.all()


class CityListCreateAPIView(ListCreateAPIView):
    """
    Class based view based on rest_framework.ListCreateAPIView,
    used to create a new City object and list all City objects.
    """
    model = City
    serializer_class = CitySerializer
    queryset = City.objects.all().order_by('id')



class CityRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    Class based view based on rest_framework.RetrieveUpdateDestroyAPIView,
    used to show detail, update and destroy a City object.
    """
    model = City
    serializer_class = CitySerializer
    queryset = City.objects.all()



class EventListCreateAPIView(ListCreateAPIView):
    """
    Class based view based on rest_framework.ListCreateAPIView,
    used to create a new Event object and list all Event objects.
    """
    model = Event
    serializer_class = EventSerializer
    queryset = Event.objects.all().order_by('id')


class EventRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    Class based view based on rest_framework.RetrieveUpdateDestroyAPIView,
    used to show detail, update and destroy a Event object.
    """
    model = Event
    serializer_class = EventSerializer
    queryset = Event.objects.all()


class SportListCreateAPIView(ListCreateAPIView):
    """
    Class based view based on rest_framework.ListCreateAPIView,
    used to create a new Sport object and list all Sport objects.
    """
    model = Sport
    serializer_class = SportSerializer
    queryset = Sport.objects.all().order_by('id')


class SportRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    Class based view based on rest_framework.RetrieveUpdateDestroyAPIView,
    used to show detail, update and destroy a Sport object.
    """
    model = Sport
    serializer_class = SportSerializer
    queryset = Sport.objects.all()


class AthleteEventListAPIView(ListCreateAPIView):
    """
    Class based view based on rest_framework.ListCreateAPIView,
    used to create a new AthleteEvent object and list all AthleteEvent objects.
    """
    model = AthleteEvent
    serializer_class = AthleteEventSerializer
    queryset = AthleteEvent.objects.all()

    def get_queryset(self):
        if self.request.GET.get('athlete'):
            queryset = AthleteEvent.objects.filter(athlete__name__icontains=self.request.GET.get('athlete'))
        elif self.request.GET.get('event'):
            queryset = AthleteEvent.objects.filter(event__name__icontains=self.request.GET.get('event'))
        elif self.request.GET.get('medal'):
            queryset = AthleteEvent.objects.filter(medal__icontains=self.request.GET.get('medal'))
        else:
            queryset = AthleteEvent.objects.all().order_by('id')
               
        return queryset


class AthleteEventRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    Class based view based on rest_framework.RetrieveUpdateDestroyAPIView,
    used to show detail, update and destroy an AthleteEvent object.
    """
    model = AthleteEvent
    serializer_class = AthleteEventSerializer
    queryset = AthleteEvent.objects.all()