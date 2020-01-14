from django.shortcuts import render, HttpResponse, get_object_or_404
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, ListCreateAPIView
from django.dispatch import receiver
from django.db.models.signals import post_save
import csv

from ogames.models import *
from ogames.serializers import *



class UploadCsvCreateAPIView(CreateAPIView):
    """
    Class based view to upload a CSV file and store all data in the database. 
    """
    model = UploadCsv
    serializer_class = UploadCsvSerializer

    @receiver(post_save, sender=UploadCsv)
    def fileupload_post_save(sender, instance, *args, **kwargs):
        """
        post save signal to read the csv file and separate the data according to the models, 
        storing them in the database
        """
        with open(instance.file.path, 'r') as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                noc_data={"name": row["noc"]}
                noc_object, _ = Noc.objects.get_or_create(**noc_data)

                team_data={"name": row["team"], "noc": noc_object}
                team_object, _ = Team.objects.get_or_create(**team_data)

                game_data={"name": row["games"]}
                game_object, _ = Game.objects.get_or_create(**game_data)

                city_data={"name": row["city"]}
                city_object, _ = City.objects.get_or_create(**city_data)

                sport_data={"name": row["sport"]}
                sport_object, _ = Sport.objects.get_or_create(**sport_data)

                event_data={
                    "name": row["event"],
                    "year": row["year"],
                    "season": row["season"],
                    "city": city_object,
                    "game": game_object,
                    }
                event_object, _ = Event.objects.get_or_create(**event_data)

                athlete_data={
                    "name": row["name"], 
                    "sex": row["sex"], 
                    "age": row["age"], 
                    "height": row["height"], 
                    "weight": row["weight"], 
                    "team": team_object,
                    "sport": sport_object,
                    }
                athlete_object, _ = Athlete.objects.get_or_create(**athlete_data)

                athlete_event_data={
                    "athlete": athlete_object, 
                    "event": event_object, 
                    "medal": row["medal"]
                    }
                athlete_event_object, _ = AthleteEvent.objects.get_or_create(**athlete_event_data)




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
    queryset = Athlete.objects.all()

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
        elif self.request.GET.get('sport'):
            queryset = Athlete.objects.filter(sport__name__icontains=self.request.GET.get('sport'))
        else:
            queryset = Athlete.objects.all().order_by('id')
        
        return queryset



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