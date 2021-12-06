from django.shortcuts import render
from .models import Game
import os
import threading

def open_game(game_location):
    os.system(f'''cmd /c "C:\\Users\\jhemsley\\Desktop\\em_test\\ares.exe -loadbin "{game_location}""''')

# Create your views here.
def home(request):
    games = Game.objects.all()
    ctx = {'games': games}
    return render(request, 'games/home.html', ctx)

def detail(request, game_id):
    game = Game.objects.get(id=game_id)
    print('local', f"{game.location}")
    game_location = game.location
    t = threading.Thread(target=open_game, args=(game_location,))
    t.daemon = True
    t.start()
    return render(request, 'games/detail.html', {'game':game})
