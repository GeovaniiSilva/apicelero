from rest_framework import serializers
from ogames.models import *


class UploadCsvSerializer(serializers.ModelSerializer):

    class Meta:
        model = UploadCsv
        fields = ('file',)



class AthleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Athlete
        fields = '__all__'
    



class NocSerializer(serializers.ModelSerializer):

    class Meta:
        model = Noc
        fields = ['name']
    
    


class TeamSerializer(serializers.ModelSerializer):
    #noc = serializers.PrimaryKeyRelatedField(read_only=True, many=True)

    class Meta:
        model = Team
        fields = ['name','noc']



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

    class Meta:
        model = Event
        fields = '__all__'



class AthleteEventSerializer(serializers.ModelSerializer):

    class Meta:
        model = AthleteEvent
        fields = '__all__'
