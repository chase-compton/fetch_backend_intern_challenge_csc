import requests
import json

BASE_URL = "http://127.0.0.1:8000"  # Update with your API URL


# Function to test the /add endpoint
def test_add_endpoint():
    endpoint = "/add"
    data = [
        {"payer": "DANNON", "points": 300, "timestamp": "2022-10-31T10:00:00Z"},
        {"payer": "UNILEVER", "points": 200, "timestamp": "2022-10-31T11:00:00Z"},
        {"payer": "DANNON", "points": -200, "timestamp": "2022-10-31T15:00:00Z"},
        {"payer": "MILLER COORS", "points": 10000, "timestamp": "2022-11-01T14:00:00Z"},
        {"payer": "DANNON", "points": 1000, "timestamp": "2022-11-02T14:00:00Z"},
    ]
    for content in data:
        response = requests.post(BASE_URL + endpoint, json=content)
        print("Response from /add endpoint:")
        print(response.status_code)
        print(response.text)


# Function to test the /spend endpoint
def test_spend_endpoint():
    endpoint = "/spend"
    data = {"points": 500}
    response = requests.post(BASE_URL + endpoint, json=data)
    print("Response from /spend endpoint:")
    print(response.status_code)
    print(response.text)


# Function to test the /balance endpoint
def test_balance_endpoint():
    endpoint = "/balance"
    response = requests.get(BASE_URL + endpoint)
    print("Response from /balance endpoint:")
    print(response.status_code)
    print(response.text)


if __name__ == "__main__":
    # Test the endpoints
    test_add_endpoint()
    test_spend_endpoint()
    test_balance_endpoint()
