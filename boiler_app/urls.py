
from django.urls import path
from django.urls import re_path
from . import views

app_name = 'boiler_app'
urlpatterns = [
    # views paths
    path("", views.index, name='index'),
]