from django.urls import path
from .views import *


urlpatterns = [
    path('read-csv/', UploadCsvCreateAPIView.as_view()),
    path('athlete-events/', AthleteEventListAPIView.as_view()),
    path('athlete-events/<int:pk>/', AthleteEventRetrieveUpdateDestroyAPIView.as_view()),
    path('athletes/', AthleteListCreateAPIView.as_view()),
    path('teams/', TeamListCreateAPIView.as_view()),
    path('nocs/', NocListCreateAPIView.as_view()),
    path('cities/', CityListCreateAPIView.as_view()),
    path('sports/', SportListCreateAPIView.as_view()),
    path('games/', GameListCreateAPIView.as_view()),
    path('events/', EventListCreateAPIView.as_view()),
]