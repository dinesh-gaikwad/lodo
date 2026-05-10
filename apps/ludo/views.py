from django.shortcuts import render

def index(request):
    return render(request, "ludo/index.html")

def game(request):
    return render(request, "ludo/game.html")

def room(request):
    return render(request, "ludo/room.html")

def leaderboard(request):
    return render(request, "ludo/leaderboard.html")

def login_view(request):
    return render(request, "ludo/login.html")

def register_view(request):
    return render(request, "ludo/register.html")
