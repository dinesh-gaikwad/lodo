import json
from channels.testing import WebsocketCommunicator
from django.test import TransactionTestCase
from config.asgi import application

class WebSocketTest(TransactionTestCase):

    async def test_websocket_connection(self):

        communicator = WebsocketCommunicator(
            application,
            "/ws/ludo/"
        )

        connected, subprotocol = await communicator.connect()

        self.assertTrue(connected)

        await communicator.disconnect()

    async def test_socket_send_receive(self):

        communicator = WebsocketCommunicator(
            application,
            "/ws/ludo/"
        )

        connected, subprotocol = await communicator.connect()

        self.assertTrue(connected)

        await communicator.send_json_to({
            "event": "dice_roll",
            "value": 6
        })

        response = await communicator.receive_json_from()

        self.assertIn("message", response)

        await communicator.disconnect()

    async def test_multiple_messages(self):

        communicator = WebsocketCommunicator(
            application,
            "/ws/ludo/"
        )

        connected, subprotocol = await communicator.connect()

        self.assertTrue(connected)

        messages = [
            {"event": "join"},
            {"event": "roll"},
            {"event": "move"}
        ]

        for msg in messages:
            await communicator.send_json_to(msg)

            response = await communicator.receive_json_from()

            self.assertIn("message", response)

        await communicator.disconnect()

    async def test_disconnect(self):

        communicator = WebsocketCommunicator(
            application,
            "/ws/ludo/"
        )

        connected, subprotocol = await communicator.connect()

        self.assertTrue(connected)

        await communicator.disconnect()

        self.assertTrue(True)
