from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from ogames.models import *
from ogames.serializers import NocSerializer



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
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Noc.objects.count(), 1)
        self.assertEqual(Noc.objects.get().name, 'AAA')
    
    def test_list_nocs(self):
        """
        To be sure noc list is 
        """

        url = reverse('list-nocs')
        data = [{'name': 'ABC'}, {'name': 'EDB'}, {'name': 'TRE'}]
        for obj in data:
            response = self.client.post(url, obj, format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertGreater(Noc.objects.count(), 0)
    
    def test_detail_noc(self):
        """
        to be sure to show noc detail
        """
        url = reverse('detail-noc', kwargs={'pk': 1})
        noc = Noc.objects.get_or_create(name="ABC")
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Noc.objects.count(), 1)
        self.assertEqual(Noc.objects.get().name, 'ABC')
    
    def test_destroy_noc(self):
        """
        to be sure to show noc detail
        """
        url = reverse('detail-noc', kwargs={'pk': 1})
        noc = Noc.objects.get_or_create(name="ABC")
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Noc.objects.count(), 0)
    
    def test_update_noc(self):
        """
        to be sure to show noc detail
        """
        url = reverse('detail-noc', kwargs={'pk': 1})
        noc = Noc.objects.get_or_create(name="ABC")
        data = {'name': 'ADC'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Noc.objects.count(), 1)
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
        data = {'name': 'Teste', 'noc': noc.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Team.objects.count(), 1)
        self.assertEqual(Team.objects.get().name, 'Teste')
    

    def test_list_teams(self):
        """
        To be sure team list is exhibited
        """

        url = reverse('list-teams')
        noc, _ = Noc.objects.get_or_create(name="ABC")
        data = [{'name': 'ABC', 'noc': noc.id}, {'name': 'EDB', 'noc': noc.id}, {'name': 'TRE', 'noc': noc.id}]
        for obj in data:
            response = self.client.post(url, obj, format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertGreater(Team.objects.count(), 0)
    
    
    def test_detail_team(self):
        """
        to be sure a team detail is showed correctly
        """
        url = reverse('detail-team', kwargs={'pk': 1})
        noc, _ = Noc.objects.get_or_create(name="ABC")
        team, _ = Team.objects.get_or_create(name="Teste", noc=noc)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Team.objects.count(), 1)
        self.assertEqual(Team.objects.get().name, 'Teste')
    
    
    def test_destroy_team(self):
        """
        to be sure to destroy a team object correctly
        """
        url = reverse('detail-team', kwargs={'pk': 1})
        noc, _ = Noc.objects.get_or_create(name="ABC")
        team, _ = Team.objects.get_or_create(name="Teste", noc=noc)
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Team.objects.count(), 0)
    

    def test_update_noc(self):
        """
        to be sure to update a team object correctly
        """
        url = reverse('detail-team', kwargs={'pk': 1})

        noc, _ = Noc.objects.get_or_create(name="ABC")
        team, _ = Team.objects.get_or_create(name="Test", noc=noc)
        data = {'name': 'Test2', 'noc': noc.id}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Team.objects.count(), 1)
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
        data = {
            "name": "Athlete 1",
            "sex": "M",
            "age": 33,
            "height": "189",
            "weight": "78",
            "team": team.id
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Athlete.objects.count(), 1)
        self.assertEqual(Athlete.objects.get().name, "Athlete 1")

