# Points Tracker API

This repository contains a simple Flask application that implements an API for a points tracker system. The API allows users to add points, spend points, and retrieve the points balance by payer.

## How to Use

To run this application and test the API, follow these steps:

1. Ensure you have Python and pip installed on your system.

2. Install the required dependencies:
   ```bash
   pip install flask
3. Clone the repo
   ```bash
   git clone https://github.com/chase-compton/fetch_backend_intern_challenge_csc.git
4. Navigate to the repo's location
   ```bash
   cd fetch_backend_intern_challenge_csc
5. Run the application
   ```bash
   python app.py
6. At this point the application is up and running. You can test it using Postman or cURL. For example, here is the add endpoint with a cURL command:
   ```bash
   curl -X POST -H "Content-Type: application/json" -d '{"payer": "DANNON", "points": 300, "timestamp": "2022-10-31T10:00:00Z"}' http://localhost:8000/add

## Testing 

To test the application there are two built-in ways.

### Method 1
1. After running the app using
   ```bash
   python app.py
2. In a separate terminal, use the following command to run the sample solution provided in the instructions
   ```bash
   python sample.py

### Method 2
1. Run the following command to run the testing suite which is located in the tests folder
   ```bash
   python -m unittest tests/test_api.py

## API Endpoints

### Add Points

- **Endpoint:** `/add`
- **Method:** POST
- **Request:**
  ```json
  {
      "payer": "PAYER_NAME",
      "points": POINTS_TO_ADD,
      "timestamp": "TIMESTAMP"
  }
- **Response:** Response message and HTTP status code.

### Spend Points
- **Endpoint:** `/spend`
- **Method:** POST
- **Request:**
  ```json
  {
    "points": POINTS_TO_SPEND
  }
- **Response:** Response message with payers with the amount of points spent by each and an HTTP status code.

### Get Balance
- **Endpoint:** `/balance`
- **Method:** GET
- **Response:** Response message with each payer's balance and HTTP status code.
