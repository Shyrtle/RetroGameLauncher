from django.urls import path
from django.views.generic.base import RedirectView
from . import views


urlpatterns = [
    path('', views.home, name='home'),
]
