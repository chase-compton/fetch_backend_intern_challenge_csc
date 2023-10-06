from flask import Blueprint, request, jsonify
from points_tracker import PointTracker

api = Blueprint('api', __name__)
point_tracker = PointTracker()

@api.route('/add', methods=['POST'])
def add_points():
    data = request.get_json()
    payer = data.get('payer')
    points = data.get('points')
    timestamp = data.get('timestamp')
    return point_tracker.add_points_transaction(payer, points, timestamp)

@api.route('/spend', methods=['POST'])
def spend_points():
    data = request.get_json()
    points = data.get('points')
    return point_tracker.spend_points(points)

@api.route('/balance', methods=['GET'])
def get_balance():
    return point_tracker.get_points_balance()