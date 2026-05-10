import json
import datetime

class SocketEvents:

    PLAYER_JOIN = "player_join"
    PLAYER_LEAVE = "player_leave"
    DICE_ROLL = "dice_roll"
    TOKEN_MOVE = "token_move"
    GAME_START = "game_start"
    GAME_END = "game_end"
    CHAT_MESSAGE = "chat_message"
    WINNER = "winner"

def build_event(event_type, data):

    return {
        "event": event_type,
        "data": data,
        "timestamp": str(datetime.datetime.now())
    }

def join_event(username):

    return build_event(
        SocketEvents.PLAYER_JOIN,
        {
            "username": username
        }
    )

def leave_event(username):

    return build_event(
        SocketEvents.PLAYER_LEAVE,
        {
            "username": username
        }
    )

def dice_roll_event(player, value):

    return build_event(
        SocketEvents.DICE_ROLL,
        {
            "player": player,
            "value": value
        }
    )

def move_event(player, position):

    return build_event(
        SocketEvents.TOKEN_MOVE,
        {
            "player": player,
            "position": position
        }
    )

def winner_event(player):

    return build_event(
        SocketEvents.WINNER,
        {
            "winner": player
        }
    )

def chat_event(player, message):

    return build_event(
        SocketEvents.CHAT_MESSAGE,
        {
            "player": player,
            "message": message
        }
    )

def serialize_event(event):

    return json.dumps(event)

def deserialize_event(event):

    return json.loads(event)

print("Socket Events Loaded")
