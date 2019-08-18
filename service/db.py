import sqlite3


class sqliteDb:
    def __init__(self):
        self.conn = sqlite3.connect('../sql/vineyard.db')
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

    def get_predictions(self):
        query = (
            "SELECT moment, prediction_boolean, prediction_percentage FROM output_model")
        rows = self.cursor.execute(query).fetchall()
        # sqlite3 returns row instead of list by default
        return [dict(row) for row in rows]

    def get_spray_moments(self):
        query = ("SELECT moment FROM spray")
        rows = self.cursor.execute(query).fetchall()

        # sqlite3 returns row instead of list by default
        return [''.join(list(row)) for row in rows]
