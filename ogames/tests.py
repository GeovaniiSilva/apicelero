from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from ogames.models import Noc
from ogames.serializers import NocSerializer



class NocTests(APITestCase):

    def test_create_nocs(self):
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
        noc = Noc.objects.get_or_create(name="ABC")
        response = self.client.delete('/api/nocs/1/', format='json')
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