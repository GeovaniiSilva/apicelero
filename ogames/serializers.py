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
    
    def create(self, validated_data):
        athlete = Athlete.objects.get_or_create(
            name = validated_data["name"],
            sex = validated_data["sex"],
            age = validated_data["age"],
            height = validated_data["height"],
            weight = validated_data["weight"],
            team = validated_data["team"]
        )
        return athlete



class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = '__all__'
    
    def create(self, validated_data):
        team = Team.objects.get_or_create(
            name = validated_data["name"],
            noc = validated_data["noc"]
        )
        return team



class NocSerializer(serializers.ModelSerializer):

    class Meta:
        model = Noc
        fields = '__all__'
    
    def create(self, validated_data):
        noc = Noc.objects.get_or_create(
            name = validated_data["name"]
        )
        return noc



class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = '__all__'
    
    def create(self, validated_data):
        game = Game.objects.get_or_create(
            name = validated_data["name"]
        )
        return game


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = '__all__'

    def create(self, validated_data):
        city = City.objects.get_or_create(
            name = validated_data["name"]
        )
        return city


class SportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sport
        fields = '__all__'

    def create(self, validated_data):
        sport = Sport.objects.get_or_create(
            name = validated_data["name"]
        )
        return sport


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'

    def create(self, validated_data):
        event = Event.objects.get_or_create(
            name = validated_data["name"]
        )
        return event


class AthleteEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = AthleteEvent
        fields = '__all__'
    
    def create(self, validated_data):
        athlete_event = AthleteEvent.objects.get_or_create(
            athlete = validated_data["athlete"],
            game = validated_data["game"],
            year = validated_data["year"],
            season = validated_data["season"],
            city = validated_data["city"],
            sport = validated_data["sport"],
            event = validated_data["event"],
            medal = validated_data["medal"]
        )
        return athlete_event