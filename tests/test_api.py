import unittest
from flask import Flask
from app import api
import json


class TestAPI(unittest.TestCase):
    def setUp(self) -> None:
        self.app = Flask(__name__)
        self.app.register_blueprint(api)
        self.client = self.app.test_client()
        return super().setUp()

    def test_a_get_balance_empty(self):
        print("Testing getting points balance with an empty balance...")
        response = self.client.get("/balance")
        expected_response = {}
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), expected_response)
        print("Test completed for getting points balance with an empty balance.")

    def test_b_get_balance_after_adding(self):
        print("Testing getting points balance after adding points...")
        # Add points to the balance
        add_payload = {
            "payer": "DANNON",
            "points": 500,
            "timestamp": "2022-10-31T10:00:00Z",
        }
        self.client.post(
            "/add", data=json.dumps(add_payload), content_type="application/json"
        )

        response = self.client.get("/balance")
        expected_response = {"DANNON": 500}
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), expected_response)
        print("Test completed for getting points balance after adding points.")

    def test_c_add_points(self):
        print("Testing the '/add' endpoint...")
        data = [
            {"payer": "DANNON", "points": 300, "timestamp": "2022-10-31T10:00:00Z"},
            {"payer": "UNILEVER", "points": 200, "timestamp": "2022-10-31T11:00:00Z"},
            {"payer": "DANNON", "points": -200, "timestamp": "2022-10-31T15:00:00Z"},
            {
                "payer": "MILLER COORS",
                "points": 10000,
                "timestamp": "2022-11-01T14:00:00Z",
            },
            {"payer": "DANNON", "points": 1000, "timestamp": "2022-11-02T14:00:00Z"},
        ]

        for i, payload in enumerate(data):
            with self.subTest(f"Test case {i+1}"):
                response = self.client.post(
                    "/add", data=json.dumps(payload), content_type="application/json"
                )
                try:
                    self.assertEqual(response.status_code, 200)
                except AssertionError:
                    print("Response content:", response.get_data(as_text=True))
                    raise

        print("Test completed for adding points.")

    def test_d_spend_negative_points(self):
        print("Testing spending negative points...")
        payload = {"points": -500}
        response = self.client.post(
            "/spend", data=json.dumps(payload), content_type="application/json"
        )
        self.assertEqual(response.status_code, 400)
        print("Test completed for spending negative points.")

    def test_e_spend_zero_points(self):
        print("Testing spending zero points...")
        payload = {"points": 0}
        response = self.client.post(
            "/spend", data=json.dumps(payload), content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        print("Test completed for spending zero points.")

    def test_f_spend_too_many_points(self):
        print("Testing spending more points than available...")
        payload = {"points": 999999}
        response = self.client.post(
            "/spend", data=json.dumps(payload), content_type="application/json"
        )
        self.assertEqual(response.status_code, 400)
        print("Test completed for spending more points than available.")

    def test_g_spend_valid_points(self):
        print("Testing a valid spend request...")
        add_payload = {
            "payer": "DANNON",
            "points": 300,
            "timestamp": "2022-10-31T10:00:00Z",
        }
        self.client.post(
            "/add", data=json.dumps(add_payload), content_type="application/json"
        )
        payload = {"points": 100}
        response = self.client.post(
            "/spend", data=json.dumps(payload), content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        print("Test completed for a valid spend request.")


if __name__ == "__main__":
    unittest.main()
