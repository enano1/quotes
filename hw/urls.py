## hw/urls.py

from django.urls import path
from django.conf import settings
from . import views

# all of the RULs that are part of this app
urlpatterns = [
    path(r'', views.home, name="home"), #standard practice is to put a comma here

]
