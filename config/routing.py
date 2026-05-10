from django.urls import re_path
from apps.ludo.consumers import LudoConsumer

websocket_urlpatterns = [

    re_path(
        r'ws/ludo/$',
        LudoConsumer.as_asgi()
    ),

]

GAME_SOCKET_EVENTS = [
    "player_join",
    "player_leave",
    "dice_roll",
    "token_move",
    "game_start",
    "game_end",
    "winner_announce"
]

def socket_info():
    return {
        "endpoint": "/ws/ludo/",
        "events": GAME_SOCKET_EVENTS
    }

print("WebSocket Routing Loaded")
