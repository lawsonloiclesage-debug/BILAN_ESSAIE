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


    # insertion des donnees dans la table
    def insert(self, id_account: int = None, number_account: str = None, class_account: str = None, name_account: str = None, debit: float = 0.0, credit: float = 0.0 ):
        if id_account is not None:
            self.cursor.execute("""INSERT INTO Journal (id_account, number_account, class_account, name_account, debit, credit) VALUES(?,?,?,?,?,?)""",
                                 (id_account, number_account, class_account, name_account, debit, credit))
        else:
            self.cursor.execute("""INSERT INTO Journal (number_account, class_account, name_account, debit, credit) VALUES(?,?,?,?,?)""",
                                 (number_account, class_account, name_account, debit, credit))
        self.conn.commit()

    # fonction sur lesquelles je dois reflechir 
    def fetch_data(self):
        return self.data_rows 

    # selection de la somme du debit d'un compte en fonction de son nom
    def total_debit_unique(self, number_account):       
        self.cursor.execute("SELECT SUM(debit) FROM Journal WHERE number_account = (?)", (number_account,))
        result = self.cursor.fetchall()
        return result

    # selection de la somme du credit d'un compte en fonction de son nom
    def total_credit_unique(self, number_account):
        self.cursor.execute("SELECT SUM(credit) FROM Journal WHERE number_account = (?)", (number_account,))
        result = self.cursor.fetchall()
        return result

    # selection de la somme du debit total
    def total_debit_total(self):
        self.cursor.execute("SELECT SUM(debit) FROM Journal")
        result = self.cursor.fetchall()
        return result

    # selection de la somme du credit total
    def total_credit_total(self):
        self.cursor.execute("SELECT SUM(credit) FROM Journal")
        result = self.cursor.fetchall()
        return result
    
    
    

        



