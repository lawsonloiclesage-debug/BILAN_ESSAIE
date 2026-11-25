import sqlite3 as sq

class Database:
    def __init__(self, name="data.db"):
        self.conn = sq.connect(name)
        self.cursor = self.conn.cursor()
        self.data_rows = self.cursor.fetchall()

        # Creation de la table journal
        journal_table = ("""
        CREATE TABLE IF NOT EXISTS Journal(
        id_transact INTEGER PRIMARY KEY AUTOINCREMENT,
        number_account TEXT NOT NULL,
        class_account TEXT NOT NULL,
        name_account TEXT NOT NULL,
        debit FLOAT NOT NULL,
        credit FLOAT NOT NULL)
        """)
        self.cursor.execute(journal_table)
        self.conn.commit()


    # insertion des donnees dans la table
    def insert(self, number_account: str, class_account: str, name_account: str, debit: float, credit: float, id_transact: int = None):
        self.cursor.execute(
            """INSERT INTO Journal (number_account, class_account, name_account, debit, credit) VALUES(?,?,?,?,?)""",
            (number_account, class_account, name_account, debit, credit)
        )
        self.conn.commit()

    def fetch_data(self):
        self.cursor.execute("SELECT * FROM Journal")
        return self.cursor.fetchall() 

    # selection de la somme du debit d'un compte en fonction de son nom
    def total_debit_unique(self, number_account):       
        self.cursor.execute("SELECT TOTAL(debit) FROM Journal WHERE number_account = (?)", (number_account,))
        result = self.cursor.fetchall()
        return result[0][0]

    # selection de la somme du credit d'un compte en fonction de son nom
    def total_credit_unique(self, number_account):
        self.cursor.execute("SELECT TOTAL(credit) FROM Journal WHERE number_account = (?)", (number_account,))
        result = self.cursor.fetchall()
        return result[0][0]

    # selection de la somme du debit total
    def total_debit_total(self):
        self.cursor.execute("SELECT TOTAL(debit) FROM Journal")
        result = self.cursor.fetchall()
        return result[0][0]

    # selection de la somme du credit total
    def total_credit_total(self):
        self.cursor.execute("SELECT TOTAL(credit) FROM Journal")
        result = self.cursor.fetchall()
        return result[0][0]
    
    
    

        



