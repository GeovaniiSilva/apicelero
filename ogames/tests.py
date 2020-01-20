from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from ogames.models import *



"""
List of tests:
1 - Noc
2 - Team
3 - Athlete
4 - Game
5 - City
6 - Sport
7 - Event
8 - AthleteEvent
9 - UploadCsv
"""

class UploadCsvTests(APITestCase):
    '''
    A test case for UploadCsv file model
    '''
    def test_create_uploadcsv(self):
        '''
        To be sure a csv file is read correctly!
        '''
        url = reverse('read-csv')
        file = open('test.csv', 'r')
        data = {
            'file': file
        }
        
        
        response = self.client.post(url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(UploadCsv.objects.count(), 1)
        self.assertEqual(AthleteEvent.objects.count(), 55)
        data['file'].close()

    def test_list_csv(self):
        '''
        To be sure a list of UploadCsv object return correctly
        '''
        url = reverse('read-csv')
        upload_csv = UploadCsv.objects.get_or_create(file='test.csv')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(UploadCsv.objects.count(), 1)

class NocTests(APITestCase):
    """
    A series of tests in NOC* model and Class based views endpoints
    """

    def test_create_noc(self):
        """
        To be sure a noc object is created
        """
        url = reverse('list-nocs')
        data = {'name': 'AAA'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, msg="Noc object not created correctly!")
        self.assertEqual(Noc.objects.count(), 1)
    
    def test_list_nocs(self):
        """
        To be sure noc list is 
        """

        url = reverse('list-nocs')
        data = [{'name': 'ABC'}, {'name': 'EDB'}, {'name': 'TRE'}]
        for obj in data:
            response = self.client.post(url, obj, format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Noc.objects.count(), 3, msg="Noc object not updated correctly!")
    
    def test_detail_noc(self):
        """
        to be sure to show noc detail
        """
        url = reverse('detail-noc', kwargs={'pk': 1})
        noc = Noc.objects.get_or_create(name="ABC")
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg="Noc object not exhibited correctly!")
        self.assertEqual(Noc.objects.get().name, 'ABC')
    
    def test_destroy_noc(self):
        """
        to be sure to show noc detail
        """
        url = reverse('detail-noc', kwargs={'pk': 1})
        noc = Noc.objects.get_or_create(name="ABC")
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT, msg="Noc object not deleted correctly!")
        self.assertEqual(Noc.objects.count(), 0)
    
    def test_update_noc(self):
        """
        to be sure to show noc detail
        """
        url = reverse('detail-noc', kwargs={'pk': 1})
        noc = Noc.objects.get_or_create(name="ABC")
        data = {'name': 'ADC'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg="Noc object not updated correctly!")
        self.assertEqual(Noc.objects.get().name, 'ADC')



class TeamTests(APITestCase):
    """
    A series of tests on Team model and Class based views endpoints
    """
    def test_create_team(self):
        """
        To be sure a team object is created
        """
        url = reverse('list-teams')
        noc, _ = Noc.objects.get_or_create(name="ABC")
        data = {'name': 'Teste', 'noc': noc.name}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, msg="Team object not created correctly!")
        self.assertEqual(Team.objects.count(), 1)
        self.assertEqual(Team.objects.get().name, 'Teste')
    

    def test_list_teams(self):
        """
        To be sure team list is exhibited
        """

        url = reverse('list-teams')
        noc, _ = Noc.objects.get_or_create(name="ABC")
        data = [{'name': 'ABC', 'noc': noc.name}, {'name': 'EDB', 'noc': noc.name}, {'name': 'TRE', 'noc': noc.name}]
        for obj in data:
            response = self.client.post(url, obj, format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Team.objects.count(), 3, msg="Team object list not exhibited correctly!")
    
    
    def test_detail_team(self):
        """
        to be sure a team detail is showed correctly
        """
        url = reverse('detail-team', kwargs={'pk': 1})
        noc, _ = Noc.objects.get_or_create(name="ABC")
        team, _ = Team.objects.get_or_create(name="Teste", noc=noc)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg="Team object not exhibited correctly!")
        self.assertEqual(Team.objects.get().name, 'Teste')
    
    
    def test_destroy_team(self):
        """
        to be sure to destroy a team object correctly
        """
        url = reverse('detail-team', kwargs={'pk': 1})
        noc, _ = Noc.objects.get_or_create(name="ABC")
        team, _ = Team.objects.get_or_create(name="Teste", noc=noc)
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT, msg="Team object not deeleted correctly")
        self.assertEqual(Team.objects.count(), 0)
    

    def test_update_team(self):
        """
        to be sure to update a team object correctly
        """
        url = reverse('detail-team', kwargs={'pk': 1})

        noc, _ = Noc.objects.get_or_create(name="ABC")
        team, _ = Team.objects.get_or_create(name="Test", noc=noc)
        data = {'name': 'Test2', 'noc': noc.name}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg="Noc object not updated correctly")
        self.assertEqual(Team.objects.get().name, 'Test2')



class AthleteTests(APITestCase):
    """
    A series of tests on Athlete model and Class based views endpoints
    """
    def test_create_athlete(self):
        """
        To be sure an athlete object is created correctly
        """
        url = reverse('list-athletes')
        noc, _ = Noc.objects.get_or_create(name="ABC")
        team, _ = Team.objects.get_or_create(name="Test", noc=noc)
        sport, _ = Sport.objects.get_or_create(name="Sport ABC")
        data = {
            "name": "Athlete 1",
            "sex": "M",
            "age": 33,
            "height": "189",
            "weight": "78",
            "team": team.name,
            "sport": sport.name
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, msg="Athlete object not created correctly")
        self.assertEqual(Athlete.objects.count(), 1)


    def test_list_athletes(self):
        """
        To be sure an anthlete list of object is returned correctly
        """
        url = reverse('list-athletes')
        noc, _ = Noc.objects.get_or_create(name="ABC")
        team, _ = Team.objects.get_or_create(name="Test", noc=noc)
        sport, _ = Sport.objects.get_or_create(name="Sport ABC")
        athlete_object_1 = Athlete.objects.get_or_create(
            name="Athlete 1",
            sex="M",
            age=33,
            height="189",
            weight="78",
            team=team,
            sport=sport
        )
        athlete_object_1 = Athlete.objects.get_or_create(
            name="Athlete 2",
            sex="M",
            age=23,
            height="180",
            weight="98",
            team=team,
            sport=sport
        )
        athlete_object_3 = Athlete.objects.get_or_create(
            name="Athlete 3",
            sex="F",
            age= 19,
            height="159",
            weight="68",
            team=team,
            sport=sport
        )
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Athlete.objects.count(), 3, msg="List of athlete objects is not correct!")
    

    def test_detail_athlete(self):
        """
        To be sure a detailed athlete object is exhibited correctly
        """
        url = reverse('detail-athlete', kwargs={"pk": 1})
        noc, _ = Noc.objects.get_or_create(name="ABC")
        team, _ = Team.objects.get_or_create(name="Test", noc=noc)
        sport, _ = Sport.objects.get_or_create(name="Sport ABC")
        athlete = Athlete.objects.get_or_create(
            name="Athlete A",
            sex="M",
            age=23,
            height="169",
            weight="72",
            team=team,
            sport=sport
        )
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg="Athlete object not exhibited correctly")
        self.assertEqual(Athlete.objects.get().name, 'Athlete A')
    
    def test_destroy_athlete(self):
        """
        To be sure an athlete object is deleted correctly!
        """
        url = reverse('detail-athlete', kwargs={"pk": 1})
        noc, _ = Noc.objects.get_or_create(name="ABC")
        team, _ = Team.objects.get_or_create(name="Test", noc=noc)
        sport, _ = Sport.objects.get_or_create(name="Sport ABC")
        athlete = Athlete.objects.get_or_create(
            name="Athlete A",
            sex="M",
            age=23,
            height="169",
            weight="72",
            team=team,
            sport=sport
        )
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT, msg="Athlete object not deleted correwctly!")
        self.assertEqual(Athlete.objects.count(), 0)
    

    def test_update_athlete(self):
        """
        To be sure an athlete object is updated correctly!
        """
        url = reverse('detail-athlete', kwargs={"pk": 1})
        noc, _ = Noc.objects.get_or_create(name="ABC")
        team, _ = Team.objects.get_or_create(name="Test", noc=noc)
        sport, _ = Sport.objects.get_or_create(name="Sport ABC")
        athlete = Athlete.objects.get_or_create(
            name="Athlete A",
            sex="M",
            age=23,
            height="169",
            weight="72",
            team=team,
            sport=sport
        )
        data = {
            "name": "Athlete B",
            "sex": "M",
            "age": 24,
            "height": "169",
            "weight": "75",
            "team": team.name,
            "sport": sport.name
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Athlete.objects.get().name, 'Athlete B', msg="Athlete object not updated correctly!")
    


class GameTests(APITestCase):
    """
    A series of tests on Game model and Class based views endpoints
    """
    def test_create_game(self):
       """
       To be sure a Game object is created correctly!
       """ 
       url = reverse('list-games')
       data = {
           "name": "Game A"
       }
       response =  self.client.post(url, data, format='json')
       self.assertEqual(response.status_code, status.HTTP_201_CREATED, msg="Game object not created correctly")
       self.assertEqual(Game.objects.get().name, "Game A")


    def test_list_games(self):
        """
        To be sure a list of Game objects is exhibited correctly!
        """
        url = reverse('list-games')
        game_obj_1 = Game.objects.get_or_create(name="Game1")
        game_obj_2 = Game.objects.get_or_create(name="Game2")
        game_obj_3 = Game.objects.get_or_create(name="Game3")
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Game.objects.count(), 3, msg="Game objects list not exhibited correctly")
    

    def test_detail_game(self):
        """
        To be sure a detailed Game object is exhibited correctly!
        """
        url = reverse('detail-game', kwargs={"pk": 1})
        game = Game.objects.get_or_create(name="Game A")
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg="Game object not exhibited correctly!")
        self.assertEqual(Game.objects.get().name, "Game A")
    

    def test_detroy_game(self):
        """
        To be sure a Game object is delete correctly!
        """
        url = reverse('detail-game', kwargs={"pk": 1})
        game = Game.objects.get_or_create(name="Game A")
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT, msg="Game object not deleted correctly!")
        self.assertEqual(Game.objects.count(), 0)
    

    def test_update_game(self):
        """
        To be sure a Game object is updated correctly!
        """
        url = reverse('detail-game', kwargs={"pk": 1})
        game = Game.objects.get_or_create(name="Game 1")
        data = {
            "name": "Game 2"
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg="Game object not updated correctly!")
        self.assertEqual(Game.objects.get().name, "Game 2")


class CityTests(APITestCase):
    """
    A series of tests on City model and class based views endoints
    """
    def test_create_city(self):
        """
        To be sure a City object is created correctly!
        """
        url = reverse('list-cities')
        data = {
            "name": "City A"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, msg="City object not created correctly!")
        self.assertEqual(City.objects.count(), 1)
        self.assertEqual(City.objects.get().name, "City A")
    
    def test_list_cities(self):
        """
        To be sure a list of cities os exhibited correctly!
        """
        url = reverse('list-cities')
        city_1 = City.objects.get_or_create(name="City 1")
        city_2 = City.objects.get_or_create(name="City 2")
        city_3 = City.objects.get_or_create(name="City 3")
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(City.objects.count(), 3, msg="City objects list not exhibited correctly!")

    def test_detail_city(self):
        """
        To be sure a City object is exhibited correctly
        """
        url = reverse('detail-city', kwargs={"pk": 1})
        city = City.objects.get_or_create(name="City A")
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg="City object not exhibited correctly!")
        self.assertEqual(City.objects.get().name, "City A")

    def test_detroy_city(self):
        """
        To be sure a City object is deleted correctly!
        """
        url = reverse('detail-city', kwargs={"pk": 1})
        city = City.objects.get_or_create(name="City A")
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT, msg="City object not deleted correctly!")
        self.assertEqual(City.objects.count(), 0)
    
    def test_update_city(self):
        """
        To be sure a City object is updated correctly!
        """
        url = reverse('detail-city', kwargs={"pk": 1})
        city = City.objects.get_or_create(name="City A")
        data = {
            "name": "City B"
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg="City object not updated correctly!")
        self.assertEqual(City.objects.get().name, "City B")

class SportTests(APITestCase):
    """
    A series of tests on model Sport and class based views endpoints
    """
    def test_create_sport(self):
        """
        To be sure a Sport object is created correctly!
        """
        url = reverse('list-sports')
        data = {
            "name": "Sport A"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, msg="Sport object was not created correctly")
        self.assertEqual(Sport.objects.get().name, "Sport A")

    def test_list_sports(self):
        """
        To be sure a list of Sport objects is exhibited correctly
        """
        url = reverse('list-sports')
        sport_1 = Sport.objects.get_or_create(name="Sport A")
        sport_2 = Sport.objects.get_or_create(name="Sport B")
        sport_3 = Sport.objects.get_or_create(name="Sport C")

        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg="Sport objects list not exhibited correctly")
        self.assertEqual(Sport.objects.count(), 3)
    
    def test_detail_sport(self):
        """
        To be sure a Sport object detail
        """
        url = reverse('detail-sport', kwargs={"pk": 1})
        sport = Sport.objects.get_or_create(name="Sport A")
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg="Sport object detail not exhibited correctly!")
        self.assertEqual(Sport.objects.get().name, "Sport A")

    def test_detroy_sport(self):
        """
        To be sure a Sport object is deleted correctly!
        """
        url = reverse('detail-sport', kwargs={"pk": 1})
        sport = Sport.objects.get_or_create(name="Sport A")
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT, msg="Sport object not deleted correctly!")
        self.assertEqual(Sport.objects.count(), 0)

    def test_update_sport(self):
        """
        To be sure a Sport object is updated correctly!
        """
        url = reverse('detail-sport', kwargs={"pk": 1})
        sport = Sport.objects.get_or_create(name="Sport A")
        data = {
            "name": "Sport B"
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg="Sport object not updated correctly!")
        self.assertEqual(Sport.objects.get().name, "Sport B")



class EventTests(APITestCase):
    """
    A serie of tests on Event model and class based views endpoints!
    """
    def test_create_event(self):
        """
        to be sure an Event model is created correctly!
        """
        url = reverse('list-events')
        city, _ = City.objects.get_or_create(name="City A")
        game, _ = Game.objects.get_or_create(name="Game B")
        data = {
            "name": "Event ABC",
            'year': 1900,
            "season": "Summer",
            "city": city.name,
            "game": game.name
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, msg="Event object not created correctly!")
        self.assertEqual(Event.objects.count(), 1)
    
    def test_list_events(self):
        """
        To be sure a list of Event objects is exhibited correctly!
        """
        url = reverse('list-events')
        city, _ = City.objects.get_or_create(name="City A")
        game, _ = Game.objects.get_or_create(name="Game B")
        event_1 = Event.objects.get_or_create(
            name="Event A",
            year=1991,
            season="Summer",
            city=city,
            game=game
            )
        event_2 = Event.objects.get_or_create(
            name="Event B",
            year=1992,
            season="Winter",
            city=city,
            game=game
            )
        event_3 = Event.objects.get_or_create(
            name="Event C",
            year=1993,
            season="Autumn",
            city=city,
            game=game
            )
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg="Event objects list not exhibited correctly!")
        self.assertEqual(Event.objects.count(), 3)

    def test_detail_event(self):
        """
        To be sure a detailed Event object is exhibited correctly
        """
        url = reverse('detail-event', kwargs={"pk": 1})
        city, _ = City.objects.get_or_create(name="City A")
        game, _ = Game.objects.get_or_create(name="Game B")
        event_1 = Event.objects.get_or_create(
            name="Event ABC",
            year=1991,
            season="Summer",
            city=city,
            game=game
            )
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg="Event object not exhibited correctly!")
        self.assertEqual(Event.objects.get().name, "Event ABC")

    def test_destroy_event(self):
        """
        To be sure a Event object is deleted correctly!
        """
        url = reverse('detail-event', kwargs={"pk": 1})
        city, _ = City.objects.get_or_create(name="City A")
        game, _ = Game.objects.get_or_create(name="Game B")
        event_1 = Event.objects.get_or_create(
            name="Event A",
            year=1991,
            season="Summer",
            city=city,
            game=game
            )
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT, msg="Event object not deleted correctly!")
        self.assertEqual(Event.objects.count(), 0)
    
    def test_update_event(self):
        """
        To be sure a Event object is deleted correctly!
        """
        url = reverse('detail-event', kwargs={"pk": 1})
        city, _ = City.objects.get_or_create(name="City A")
        game, _ = Game.objects.get_or_create(name="Game B")
        event_1 = Event.objects.get_or_create(
            name="Event A",
            year=1991,
            season="Summer",
            city=city,
            game=game
            )
        data = {
            "name": "Event AAA",
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg="Event object not deleted correctly!")
        self.assertEqual(Event.objects.get().name, "Event AAA")



class AthleteEventTests(APITestCase):
    """
    A series of tests on AthleteEvent model and class based views endpoints
    """
    def test_create_athlete_event(self):
        """
        To be sure a AthleteEvent object is created correctly!
        """
        url = reverse('list-athlete-events')
        noc, _ = Noc.objects.get_or_create(name="ABC")
        team, _ = Team.objects.get_or_create(name="Team 1", noc=noc)
        sport, _ = Sport.objects.get_or_create(name="Sport A")
        athlete, _ = Athlete.objects.get_or_create(
            name="Athlete 1", 
            sex="M", 
            age=23, 
            height="160", 
            weight="78",
            team=team,
            sport=sport
            )
        city, _ = City.objects.get_or_create(name="City A")
        game, _ = Game.objects.get_or_create(name="Game B")
        event, _ = Event.objects.get_or_create(
            name="Event A",
            year=1991,
            season="Summer",
            city=city,
            game=game
            )
        data = {
            "athlete": athlete.name,
            "event": event.name,
            "medal": "Gold"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, msg="AthleteEvent object not created correctly!")
        self.assertEqual(AthleteEvent.objects.count(), 1)
    
    def test_list_athlete_events(self):
        """
        To be sure an AthleteEvent objects list is exhibited correctly!
        """
        url = reverse('list-athlete-events')
        noc, _ = Noc.objects.get_or_create(name="ABC")
        team, _ = Team.objects.get_or_create(name="Team 1", noc=noc)
        sport, _ = Sport.objects.get_or_create(name="Sport ABC")
        athlete, _ = Athlete.objects.get_or_create(
            name="Athlete 1", 
            sex="M", 
            age=23, 
            height="160", 
            weight="78",
            team=team,
            sport=sport
            )
        game, _ = Game.objects.get_or_create(name="Game ABC")
        city, _ = City.objects.get_or_create(name="City ABC")
        event, _ = Event.objects.get_or_create(
            name="Event ABC",
            year=1991,
            season="Summer",
            city=city,
            game=game,
            )
        athlete_event_1, _ = AthleteEvent.objects.get_or_create(
            athlete=athlete,
            event=event,
            medal="Gold"
        )
        athlete_event_2, _ = AthleteEvent.objects.get_or_create(
            athlete=athlete,
            event=event,
            medal="Bronze"
        )
        athlete_event_3, _ = AthleteEvent.objects.get_or_create(
            athlete=athlete,
            event=event,
            medal="Silver"
        )
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(AthleteEvent.objects.count(), 3, msg="AthleteEvent object not exhibited correctly!")
    
    def test_detail_athlete_event(self):
        """
        To be sure an AthleteEvent object is exhibited correctly!
        """
        url = reverse('detail-athlete-event', kwargs={"pk": 1})
        noc, _ = Noc.objects.get_or_create(name="ABC")
        team, _ = Team.objects.get_or_create(name="Team 1", noc=noc)
        sport, _ = Sport.objects.get_or_create(name="Sport ABC")
        athlete, _ = Athlete.objects.get_or_create(
            name="Athlete 1", 
            sex="M", 
            age=23, 
            height="160", 
            weight="78",
            team=team,
            sport=sport,
            )
        game, _ = Game.objects.get_or_create(name="Game ABC")
        city, _ = City.objects.get_or_create(name="City ABC")
        event, _ = Event.objects.get_or_create(
            name="Event ABC",
            game=game,
            year=1991,
            season="Summer",
            city=city,
            )
        athlete_event_1, _ = AthleteEvent.objects.get_or_create(
            athlete=athlete,
            event=event,
            medal="Gold"
        )

        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(AthleteEvent.objects.count(), 1, msg="AthleteEvent object not exhibited correctly!")
    
    def test_destroy_athlete_event(self):
        """
        To be sure an AthleteEvent object is exhibited correctly!
        """
        url = reverse('detail-athlete-event', kwargs={"pk": 1})
        noc, _ = Noc.objects.get_or_create(name="ABC")
        team, _ = Team.objects.get_or_create(name="Team 1", noc=noc)
        sport, _ = Sport.objects.get_or_create(name="Sport ABC")
        athlete, _ = Athlete.objects.get_or_create(
            name="Athlete 1", 
            sex="M", 
            age=23, 
            height="160", 
            weight="78",
            team=team,
            sport=sport
            )
        game, _ = Game.objects.get_or_create(name="Game ABC")
        city, _ = City.objects.get_or_create(name="City ABC")    
        event, _ = Event.objects.get_or_create(
            name="Event ABC",
            game=game,
            year=1991,
            season="Summer",
            city=city,
            )
        athlete_event_1, _ = AthleteEvent.objects.get_or_create(
            athlete=athlete,
            event=event,
            medal="Gold"
        )

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT, msg="AthleteEvent object not deleted correctly!")
        self.assertEqual(AthleteEvent.objects.count(), 0)
    
    def test_update_athlete_event(self):
        """
        To be sure an AthleteEvent object is exhibited correctly!
        """
        url = reverse('detail-athlete-event', kwargs={"pk": 1})
        noc, _ = Noc.objects.get_or_create(name="ABC")
        team, _ = Team.objects.get_or_create(name="Team 1", noc=noc)
        sport, _ = Sport.objects.get_or_create(name="Sport A")
        athlete, _ = Athlete.objects.get_or_create(
            name="Athlete 1", 
            sex="M", 
            age=23, 
            height="160", 
            weight="78",
            team=team, 
            sport=sport
            )
        game, _ = Game.objects.get_or_create(name="Game ABC")
        city, _ = City.objects.get_or_create(name="City ABC")
        sport, _ = Sport.objects.get_or_create(name="Sport ABC")
        event, _ = Event.objects.get_or_create(
            name="Event ABC",
            game=game,
            year=1991,
            season="Summer",
            city=city,
            )
        athlete_event_1, _ = AthleteEvent.objects.get_or_create(
            athlete=athlete,
            event=event,
            medal="Gold"
        )
        data = {
            "athlete": athlete.name,
            "event": event.name,
            "medal": "Gold"
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(AthleteEvent.objects.get().event.year, 1991, msg="AthleteEvent object not updated correctly!")