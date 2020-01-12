from django.urls import path
from .views import *


urlpatterns = [
    path('read-csv/', UploadCsvCreateAPIView.as_view(), name='read-csv'),
    path('athlete-events/', AthleteEventListAPIView.as_view(), name='list-athlete-events'),
    path('athlete-events/<int:pk>/', AthleteEventRetrieveUpdateDestroyAPIView.as_view(), name='athlete-events-details'),
    path('athletes/', AthleteListCreateAPIView.as_view(), name='list-athletes'),
    path('teams/', TeamListCreateAPIView.as_view(), name='list-teams'),
    path('nocs/', NocListCreateAPIView.as_view(), name='list-nocs'),
    path('nocs/<int:pk>/', NocRetrieveUpdateDestroyAPIView.as_view(), name='detail-noc'),
    path('cities/', CityListCreateAPIView.as_view(), name='list-cities'),
    path('sports/', SportListCreateAPIView.as_view(), name='list-sports'),
    path('games/', GameListCreateAPIView.as_view(), name='list-games'),
    path('events/', EventListCreateAPIView.as_view(), name='list-events'),
]