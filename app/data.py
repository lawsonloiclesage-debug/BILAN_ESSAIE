import sqlite3 as sq

class Database:
    def __init__(self, name="data.db"):
        self.conn = sq.connect(name)
        self.cursor = self.conn.cursor()

        # Creation de la base de donnees
        