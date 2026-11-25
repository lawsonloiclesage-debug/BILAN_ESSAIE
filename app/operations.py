import data as dt
import metier as mt

# Classe qui permet d'effectuer les operations de recuperer les debits et credits de de la base de donnee
# et de definir les soldes
class OperationsBilan:

    def __init__(self):
        self.db = dt.Database()
    
    def total_debit_unique(self,number_account: str) -> float:
        return self.db.total_debit_unique(number_account)

    def total_credit_unique(self,number_account: str) -> float:
        return self.db.total_credit_unique(number_account)
        
    def solde_unique(self, number_account: str) -> str:
        debit = self.total_debit_unique(number_account)
        credit = self.total_credit_unique(number_account)
        if debit > credit:
            return f"Le solde du compte {number_account} est debiteur de {debit - credit}"
        elif credit > debit:
            return f"Le solde du compte {number_account} est crediteur de {credit - debit}"
        return f"Le solde du compte {number_account} est nul (0.0)"
    
    def total_debit_total(self) -> float:
        return self.db.total_debit_total()

    def total_credit_total(self) -> float:
        return self.db.total_credit_total()

    def solde_total(self) -> float:
        debit = self.total_debit_total()
        credit = self.total_credit_total()
        if debit > credit:
            return debit - credit
        return credit - debit
    

    def double_partie(self, assets: mt.Assets, liabilities: mt.Liabilities):
        if assets.debit == liabilities.credit:
            return "Good"
        return "Bad"

    def check_solde(self) -> bool:
        return self.total_debit_total() == self.total_credit_total()


class OperationResultat:
    ...

"""
def main():
    while True:
        infos_set = {}
        try:
            ask = int(input("Combien de comptes voulezz vous enregistrer: "))
            for account in range(1,ask+1):
                account_name = ask("Taper le libelle du compte: ")
                account

                
"""


cmpte = OperationsBilan()
print("Total debit:", cmpte.total_debit_unique("53"))
print("Total credit:", cmpte.total_credit_unique("53"))
print("Solde:", cmpte.solde_unique("53"))
print(cmpte.solde_unique("53"))