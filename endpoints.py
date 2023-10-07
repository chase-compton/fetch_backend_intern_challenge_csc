from flask import Blueprint, request, jsonify
from points_tracker import PointTracker  # Importing the PointTracker class

api = Blueprint("api", __name__)  # Creating a Blueprint named 'api'
point_tracker = PointTracker()  # Creating an instance of the PointTracker class


@api.route("/add", methods=["POST"])
def add_points():
    """
    Endpoint to add points for a specific payer.

    Expected JSON request:
    {
        "payer": "PAYER_NAME",
        "points": POINTS_TO_ADD,
        "timestamp": "TIMESTAMP"
    }

    Returns:
    - tuple: Response message and HTTP status code.
    """
    data = request.get_json()
    if not all(key in data for key in ("payer", "points", "timestamp")):
        return (
            jsonify(
                {
                    "error": "Incomplete data. Please provide payer, points, and timestamp."
                }
            ),
            400,
        )
    payer = data.get("payer")
    points = data.get("points")
    timestamp = data.get("timestamp")
    return point_tracker.add_points_transaction(payer, points, timestamp)


@api.route("/spend", methods=["POST"])
def spend_points():
    """
    Endpoint to spend points.

    Expected JSON request:
    {
        "points": POINTS_TO_SPEND
    }

    Returns:
    - tuple: Response message and HTTP status code.
    """
    data = request.get_json()
    if "points" not in data:
        return jsonify({"error": "Missing 'points' in the request."}), 400
    points = data.get("points")
    return point_tracker.spend_points(points)


@api.route("/balance", methods=["GET"])
def get_balance():
    """
    Endpoint to get the points balance by payer.

    Returns:
    - tuple: Response message and HTTP status code.
    """
    return point_tracker.get_points_balance()
