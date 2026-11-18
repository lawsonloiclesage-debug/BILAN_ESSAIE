import sqlite3 as sq

class Database:
    def __init__(self, name="data.db"):
        self.conn = sq.connect(name)
        self.cursor = self.conn.cursor()
        self.data_rows = self.cursor.fetchall()

        # Creation de la table journal

        journal_table = ("""
        CREATE TABLE IF NOT EXISTS Journal(
        id_account TEXT PRIMARY KEY,
        class_account TEXT NOT NULL,
        name_account TEXT NOT NULL,
        debit FLOAT NOT NULL,
        credit FLOAT NOT NULL)
        """)
        self.cursor.execute(journal_table)
        self.conn.commit()


    def insert(self, id_account: str, class_account: str, name_account: str, debit: float, credit: float ):
        self.cursor.execute("""INSERT INTO Journal (id_account, class_account, name_account, debit, credit) VALUES(?,?,?,?,?)""",
                             (id_account, class_account, name_account, debit, credit))
        self.conn.commit()

    
    def fetch_data(self):
        return self.data_rows 


    def total_credit(self, id_account):
        self.cursor.execute("SELECT SUM(debit) WHERE id_account = (?)", (id_account,))

    def total_credit(self, id_account):
        self.cursor.execute("SELECT SUM(credit) WHERE id_account = (?)", (id_account,))
        



