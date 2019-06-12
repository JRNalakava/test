from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('directory/', views.directory, name='directory'),
    path('account/', views.account, name='account'),
]