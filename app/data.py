import sqlite3 as sq

class Database:
    def __init__(self, name="data.db"):
        self.conn = sq.connect(name)
        self.cursor = self.conn.cursor()

        # Creation de la table journal

        journal_table = ("""
        CREATE TABLE IF NOT EXISTS Journal(
        id_account INTEGER PRIMARY KEY AUTOINCREMENT,
        class_accont INTEGER NOT NULL check(class_account > 9),
        name_account TEXT NOT NULL,
        debit DECIMAL,
        credit DECIMAL)
        """)
        self.cursor.execute(journal_table)
        self.conn.commit()
        

        
