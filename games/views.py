from django.shortcuts import render
from .models import Game

# Create your views here.
def home(request):
    games = Game.objects.all()
    ctx = {'games': games}
    return render(request, 'games/home.html', ctx)
