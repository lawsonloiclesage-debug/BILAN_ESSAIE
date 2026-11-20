import data as dt
import metier as mt

# Classe qui permet d'effectuer les operations de recuperer les debits et credits de de la base de donnee
# et de definir les soldes
class Operations:

    def __init__(self,metier: mt):
        self.checking = metier.Accounts
        self.db = dt.Database()
    
    def total_debit_unique(self,name_account: str) -> float:
        return self.db.total_debit_unique(name_account)

    def total_credit_unique(self,name_account: str) -> float:
        return self.db.total_credit_unique(name_account)
        
    def solde_unique(self, name_account) -> float:
        is_solde = self.total_debit_unique(name_account) > self.total_credit_unique(name_account)
        if is_solde:
            return self.total_debit_unique(name_account) - self.total_credit_unique(name_account)
        return self.total_credit_unique(name_account) - self.total_debit_unique(name_account)
    
    def total_debit_total(self) -> float:
        return self.db.total_debit_total()

    def total_credit_total(self) -> float:
        return self.db.total_credit_total()

    def solde_total(self) -> float:
        is_solde = self.total_debit_total() > self.total_credit_total()
        if is_solde:
            return self.total_debit_total() - self.total_credit_total()
        return self.total_credit_total() - self.total_debit_unique()
    

    def double_partie(self):
        if self.checking.Assets.debit == self.checking.Liabilities.credit:
            return "Good"
        return "Bad"







cmpte = Operations()
print(cmpte.total_credit_unique(""))
