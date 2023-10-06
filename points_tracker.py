import heapq
from flask import jsonify


class PointTracker:
    def __init__(self):
        self.total_points = 0  # Total points at any given time
        self.transactions = []  # List of transactions
        self.points_by_payer = {}  # Dictionary to store points by payer

    def add_points_transaction(self, payer, points, timestamp):
        self.total_points += points

        heapq.heappush(self.transactions, [timestamp, payer, points])

        if payer not in self.points_by_payer:
            self.points_by_payer[payer] = 0

        self.points_by_payer[payer] += points

        print(self.total_points)

        return "", 200

    def spend_points(self, points):
        if points < 0:
            return "Points to spend must be greater than 0", 400
        if points > self.total_points:
            return "Insufficient points balance", 400
        if points == 0:
            return "", 200

        self.total_points -= points
        spent_points = {}
        while points > 0:
            transaction_time, transaction_payer, transaction_points = self.transactions[0]

            if points >= transaction_points:
                heapq.heappop(self.transactions)
                points -= transaction_points
                if transaction_payer not in spent_points:
                    spent_points[transaction_payer] = 0
                spent_points[transaction_payer] -= transaction_points
                self.points_by_payer[transaction_payer] -= transaction_points

            else:
                transaction_points -= points
                self.transactions[0][2] = transaction_points
                if transaction_payer not in spent_points:
                    spent_points[transaction_payer] = 0
                spent_points[transaction_payer] -= points
                self.points_by_payer[transaction_payer] -= points
                points = 0

        return jsonify(spent_points), 200

    def get_points_balance(self):
        return jsonify(self.points_by_payer), 200
