from django.test import TestCase
from django.urls import reverse

class APITest(TestCase):

    def test_home_page(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)

    def test_game_page(self):
        response = self.client.get("/game/")

        self.assertEqual(response.status_code, 200)

    def test_room_page(self):
        response = self.client.get("/room/")

        self.assertEqual(response.status_code, 200)

    def test_leaderboard_page(self):
        response = self.client.get("/leaderboard/")

        self.assertEqual(response.status_code, 200)

    def test_login_page(self):
        response = self.client.get("/login/")

        self.assertEqual(response.status_code, 200)

    def test_register_page(self):
        response = self.client.get("/register/")

        self.assertEqual(response.status_code, 200)

    def test_api_status(self):
        response = self.client.get("/api/status/")

        self.assertEqual(response.status_code, 200)

        data = response.json()

        self.assertEqual(data["status"], "running")

    def test_invalid_route(self):
        response = self.client.get("/invalid/")

        self.assertEqual(response.status_code, 404)
