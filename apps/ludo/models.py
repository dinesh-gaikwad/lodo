from django.db import models
from django.contrib.auth.models import User

class PlayerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class GameRoom(models.Model):
    room_code = models.CharField(max_length=20, unique=True)
    is_active = models.BooleanField(default=True)
    max_players = models.IntegerField(default=4)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.room_code


class GameHistory(models.Model):
    player = models.ForeignKey(PlayerProfile, on_delete=models.CASCADE)
    room = models.ForeignKey(GameRoom, on_delete=models.CASCADE)
    result = models.CharField(max_length=20)
    played_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.player} - {self.result}"
