from . import views
from django.urls import path

urlpatterns = [
    path('<user_name>', views.brothers, name='brothers'),
]