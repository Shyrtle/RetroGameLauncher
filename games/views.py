from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger
from .models import Game
import os
import threading

def open_game(game_location):
    os.system(f'''cmd /c "C:\\Users\\jhemsley\\Desktop\\em_test\\ares.exe -loadbin "{game_location}""''')

# Create your views here.
def home(request):
    if 'q' in request.GET:
        q=request.GET['q']
        games_list = Game.objects.filter(title__icontains=q)
    else:
        games_list = Game.objects.all()
    paginator = Paginator(games_list, 5) # Show 10 per page.

    page = request.GET.get('page')
    try:
        games = paginator.page(page)
    except PageNotAnInteger:
        games = paginator.page(1)
    except EmptyPage:
        games = paginator.page(paginator.num_pages)

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
