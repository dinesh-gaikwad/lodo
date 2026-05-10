"""
WebSocket Package For Ludo Multiplayer
"""

SOCKET_VERSION = "1.0.0"

SUPPORTED_EVENTS = [
    "player_join",
    "player_leave",
    "dice_roll",
    "token_move",
    "chat_message",
    "game_start",
    "game_end",
    "winner"
]

def websocket_info():
    return {
        "version": SOCKET_VERSION,
        "events": SUPPORTED_EVENTS
    }

print("WebSocket Package Initialized")
