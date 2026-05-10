# Ludo Multiplayer API Documentation

## Base URL

http://localhost:8000/

---

# Authentication APIs

## Register User

Endpoint:
POST /register/

Request Body:

{
    "username": "dinesh",
    "email": "dinesh@gmail.com",
    "password": "123456"
}

Response:

{
    "status": "success",
    "message": "User Registered"
}

---

## Login User

Endpoint:
POST /login/

Request Body:

{
    "email": "dinesh@gmail.com",
    "password": "123456"
}

Response:

{
    "status": "success",
    "token": "jwt-token"
}

---

# Game APIs

## Create Room

Endpoint:
POST /room/create/

Response:

{
    "room_code": "ROOM123",
    "status": "created"
}

---

## Join Room

Endpoint:
POST /room/join/

Request:

{
    "room_code": "ROOM123"
}

Response:

{
    "status": "joined"
}

---

## Start Match

Endpoint:
POST /game/start/

Response:

{
    "status": "started"
}

---

## Roll Dice

Endpoint:
POST /game/roll/

Response:

{
    "dice": 6
}

---

## Move Token

Endpoint:
POST /game/move/

Request:

{
    "token_id": 1,
    "steps": 6
}

Response:

{
    "position": 25
}

---

# WebSocket API

Endpoint:
ws://localhost:8000/ws/ludo/

Events:

1. player_join
2. player_leave
3. dice_roll
4. token_move
5. game_end
6. winner

Example Socket Message:

{
    "event": "dice_roll",
    "value": 5
}

---

# Leaderboard API

Endpoint:
GET /leaderboard/

Response:

[
    {
        "username": "Dinesh",
        "wins": 50
    }
]

---

# Error Response

{
    "status": "error",
    "message": "Invalid Request"
}

---

# Security

- CSRF Protection
- JWT Authentication
- Secure WebSocket
- Password Hashing
- Session Validation

---

# Future APIs

- Voice Chat
- Tournament Mode
- Friend System
- Match History
- Live Streaming
