from . import views
from django.urls import path

urlpatterns = [
    path('', views.brothers, name='brothers'),
]