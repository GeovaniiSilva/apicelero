from rest_framework import serializers
from ogames.models import *


class UploadCsvSerializer(serializers.ModelSerializer):

    class Meta:
        model = UploadCsv
        fields = ('file',)



class EventSerializer(serializers.ModelSerializer):
    game = serializers.SlugRelatedField(queryset=Game.objects.all(), slug_field='name')
    city = serializers.SlugRelatedField(queryset=City.objects.all(), slug_field='name')

    class Meta:
        model = Event
        fields = ['name','year','season','city','game']
        


class AthleteSerializer(serializers.ModelSerializer):
    team = serializers.SlugRelatedField(queryset=Team.objects.all(), slug_field='name')
    sport = serializers.SlugRelatedField(queryset=Sport.objects.all(), slug_field='name')

    class Meta:
        model = Athlete
        fields = ['name','sex','age','height','weight','team','sport']
    


class NocSerializer(serializers.ModelSerializer):

    class Meta:
        model = Noc
        fields = ['name']
    
    

class TeamSerializer(serializers.ModelSerializer):
    athletes = serializers.StringRelatedField(many=True, read_only=True)
    noc = serializers.SlugRelatedField(queryset=Noc.objects.all(), slug_field='name')
    class Meta:
        model = Team
        fields = ['name','noc', 'athletes']



class GameSerializer(serializers.ModelSerializer):
    events = serializers.SlugRelatedField(slug_field='name', many=True, read_only=True)

    class Meta:
        model = Game
        fields = ['name', 'events']



class CitySerializer(serializers.ModelSerializer):
    events = serializers.SlugRelatedField(slug_field='name', many=True, read_only=True)
    class Meta:
        model = City
        fields = ['name', 'events']



class SportSerializer(serializers.ModelSerializer):
    athletes = serializers.SlugRelatedField(slug_field='name', many=True, read_only=True)
    class Meta:
        model = Sport
        fields = ['name','athletes']



class AthleteEventSerializer(serializers.ModelSerializer):
    athlete = serializers.SlugRelatedField(queryset=Athlete.objects.all(), slug_field='name')
    sex = serializers.SerializerMethodField()
    age = serializers.SerializerMethodField()
    team = serializers.SerializerMethodField()
    noc = serializers.SerializerMethodField()
    event = serializers.SlugRelatedField(queryset=Event.objects.all(), slug_field='name')
    game = serializers.SerializerMethodField()
    year = serializers.SerializerMethodField()
    sport = serializers.SerializerMethodField()
    city = serializers.SerializerMethodField()
    season = serializers.SerializerMethodField()
    height = serializers.SerializerMethodField()
    weight = serializers.SerializerMethodField()



    class Meta:
        model = AthleteEvent
        fields = ['athlete', 'sex', 'age', 'height', 'weight', 'team', 'noc', 'game', 'year', 'season', 'city', 'sport', 'event', 'medal']

    def get_noc(self, obj):
        return obj.athlete.team.noc.name

    def get_team(self, obj):
        return obj.athlete.team.name

    def get_age(self, obj):
        return obj.athlete.age

    def get_height(self, obj):
        return obj.athlete.height
    
    def get_weight(self, obj):
        return obj.athlete.weight

    def get_sex(self, obj):
        return obj.athlete.sex

    def get_game(self, obj):
        return obj.event.game.name

    def get_year(self, obj):
        return obj.event.year

    def get_sport(self, obj):
        return obj.athlete.sport.name

    def get_city(self, obj):
        return obj.event.city.name
        
    def get_season(self, obj):
        return obj.event.season