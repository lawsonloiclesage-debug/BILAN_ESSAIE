import sqlite3 as sq

class Database:
    def __init__(self, name="data.db"):
        self.conn = sq.connect(name)
        self.cursor = self.conn.cursor()
        self.data_rows = self.cursor.fetchall()

        # Creation de la table journal

        journal_table = ("""
        CREATE TABLE IF NOT EXISTS Journal(
        id_account INTEGER PRIMARY KEY AUTOINCREMENT,
        number_account TEXT NOT NULL,
        class_account TEXT NOT NULL,
        name_account TEXT NOT NULL,
        debit FLOAT NOT NULL,
        credit FLOAT NOT NULL)
        """)
        self.cursor.execute(journal_table)
        self.conn.commit()


    def insert(self, id_account: int = None, number_account: str = None, class_account: str = None, name_account: str = None, debit: float = 0.0, credit: float = 0.0 ):
        if id_account is not None:
            self.cursor.execute("""INSERT INTO Journal (id_account, number_account, class_account, name_account, debit, credit) VALUES(?,?,?,?,?,?)""",
                                 (id_account, number_account, class_account, name_account, debit, credit))
        else:
            self.cursor.execute("""INSERT INTO Journal (number_account, class_account, name_account, debit, credit) VALUES(?,?,?,?,?)""",
                                 (number_account, class_account, name_account, debit, credit))
        self.conn.commit()

    
    def fetch_data(self):
        return self.data_rows 


    def total_debit_unique(self, number_account):
       return self.cursor.execute("SELECT SUM(debit) FROM Journal WHERE number_account = (?)", (number_account,))

    def total_credit_unique(self, number_account):
        return self.cursor.execute("SELECT SUM(credit) FROM Journal WHERE number_account = (?)", (number_account,))

    def total_debit_total(self):
        return self.cursor.execute("SELECT SUM(debit) FROM Journal")

    def total_credit_total(self):
        return self.cursor.execute("SELECT SUM(credit) FROM Journal")
    
    
    

        



