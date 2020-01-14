from rest_framework import serializers
from ogames.models import *


class UploadCsvSerializer(serializers.ModelSerializer):

    class Meta:
        model = UploadCsv
        fields = ('file',)



class AthleteSerializer(serializers.ModelSerializer):
    team = serializers.SlugRelatedField(queryset=Team.objects.all(), slug_field='name')
    sport = serializers.SlugRelatedField(queryset=Sport.objects.all(), slug_field='name')
    class Meta:
        model = Athlete
        fields = '__all__'
    



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

    class Meta:
        model = Game
        fields = '__all__'
    


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = '__all__'



class SportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sport
        fields = '__all__'



class EventSerializer(serializers.ModelSerializer):
    game = serializers.SlugRelatedField(queryset=Game.objects.all(), slug_field='name')
    city = serializers.SlugRelatedField(queryset=City.objects.all(), slug_field='name')
    class Meta:
        model = Event
        fields = '__all__'
        depth = 1



class AthleteEventSerializer(serializers.ModelSerializer):
    athlete = serializers.SlugRelatedField(queryset=Athlete.objects.all(), slug_field='name')
    event = serializers.SlugRelatedField(queryset=Event.objects.all(), slug_field='name')
    class Meta:
        model = AthleteEvent
        fields = '__all__'
