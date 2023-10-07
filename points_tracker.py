import heapq
from flask import jsonify


class PointTracker:
    def __init__(self):
        """
        Constructor to initialize the PointTracker class.
        """
        self.total_points = 0  # Total points at any given time
        self.transactions = []  # List of transactions
        self.points_by_payer = {}  # Dictionary to store points by payer

    def add_points_transaction(self, payer, points, timestamp):
        """
        Add points transaction to the system.

        Parameters:
        - payer (str): Payer's name.
        - points (int): Points to be added.
        - timestamp (str): Timestamp of the transaction.

        Returns:
        - tuple: Response message and HTTP status code.
        """

        if payer not in self.points_by_payer:
            self.points_by_payer[payer] = 0

        if self.points_by_payer[payer] + points < 0:
            return f"Error: This transaction would result in a negative balance for {payer}." ,400
        
        self.points_by_payer[payer] += points

        self.total_points += points

        heapq.heappush(self.transactions, [timestamp, payer, points])

        return "", 200

    def spend_points(self, points):
        """
        Spend points from the system.

        Parameters:
        - points (int): Points to be spent.

        Returns:
        - tuple: Response message and HTTP status code.
        """
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

        output = []
        for payer in spent_points.keys():
            output.append({"payer": payer, "points": spent_points[payer]})

        return jsonify(output), 200

    def get_points_balance(self):
        """
        Get the points balance by payer.

        Returns:
        - tuple: Response message and HTTP status code.
        """
        return jsonify(self.points_by_payer), 200
