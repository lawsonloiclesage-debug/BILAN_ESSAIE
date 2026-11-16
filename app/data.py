import sqlite3 as sq

class Database:
    def __init__(self, name="data.db"):
        self.conn = sq.connect(name)
        self.cursor = self.conn.cursor()

        # Creation de la table journal

        journal_table = ("""
        CREATE TABLE IF NOT EXISTS Journal(
        id_account TEXT PRIMARY KEY,
        class_account TEXT NOT NULL check,
        name_account TEXT NOT NULL,
        debit DECIMAL,
        credit DECIMAL)
        """)
        self.cursor.execute(journal_table)
        self.conn.commit()


    def insert(self, id_account: str, class_account: str, name_acount: str, debit: float, credit: float ):
        self.cursor.execute("""INSERT INTO journal_table (id_account, class_account, name_account, debit, credit) VALUES(?,?,?,?,?)""",
                             (id_account, class_account, name_acount, debit, credit))

    



