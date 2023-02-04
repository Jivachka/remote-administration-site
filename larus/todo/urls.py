from django.urls import path
from .views import BaseHomePage

urlpatterns = [
    path('', BaseHomePage.as_view(), name='home'),
]
