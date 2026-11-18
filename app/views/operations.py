import data as dt
import metier as mt

class Operations:
    def __init__(self):
        ...        

    def total_debit_unique(self, id_account: str) -> float:
        return dt.Database.total_debit(id_account)

    def total_credit_unique(self, id_account: str) -> float:
        return dt.Database.total_credit(id_account)
        
    def solde_unique(self) -> float:
        is_solde = self.total_debit_unique > self.total_credit_unique
        if is_solde:
            return self.total_debit_unique - self.total_credit_unique
        return self.total_credit_unique - self.total_debit_unique
    
    def total_debit_total(self) -> float:
        return dt.Database.total_debit_total()

    def total_credit_total(self) -> float:
        return dt.Database.total_credit_total()

    def solde_total(self) -> float:
        is_solde = self.total_debit_total > self.total_credit_total
        if is_solde:
            return self.total_debit_total - self.total_credit_total
        return self.total_credit_total - self.total_debit_unique


        
        


        
    

    
