from django.contrib import admin
from .models import PlayerProfile, GameRoom, GameHistory

@admin.register(PlayerProfile)
class PlayerProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "score", "wins", "losses")

@admin.register(GameRoom)
class GameRoomAdmin(admin.ModelAdmin):
    list_display = ("room_code", "is_active", "max_players")

@admin.register(GameHistory)
class GameHistoryAdmin(admin.ModelAdmin):
    list_display = ("player", "room", "result", "played_at")
