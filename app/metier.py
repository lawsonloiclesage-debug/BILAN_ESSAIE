from abc import ABC, abstractmethod
import data as dt

class Accounts:
    # Classe abstraite qui servira de support aux autres classes des autres differnets types de compte
    class Account(ABC):
        def __init__(self, id_account: str, class_account: str, name_account: str, debit: float, credit: float ):
            self.id_account = id_account
            self.class_account = class_account
            self.name_account = name_account
            self.debit = debit
            self.credit = credit
            self.connect = dt.Database()
            self.Assets_data = self.connect.insert(id_account, class_account, name_account, debit, credit)
                    
        @abstractmethod
        def set_debit(self, montant: float) -> float:
            ...

        @abstractmethod
        def set_credit(self, montant: float) -> float:
            ...

        @abstractmethod
        def get_montant(self):
            ...        


    class Assets(Account):
        def __init__(self,id_account: str, class_account: str, name_account: str, debit: float, credit: float ):
            super().__init__(id_account, class_account,name_account, debit, credit )
            self.Assets_data = self.connect.insert(id_account, class_account, name_account, debit, credit)
        
        def set_debit(self, montant):            
            self.montant += montant

        def set_credit(self, montant):
            if self.montant - montant < 0:
                raise ("value error")
            else:
                self.montant -=montant

        def get_montant(self):
            return self.montant    

        
    class Liabilities(Account):
        def __init__(self, designation, account_number, montant):
            super().__init__(designation, account_number, montant)

        def set_debit(self, montant):
            if self.montant - montant < 0:
                raise ("Value error")
            else:
                self.montant -=montant

        def set_credit(self, montant):
            self.montant += montant

        def get_montant(self):
            return self.montant



    class Charge(Account):
        def __init__(self, designation, account_number, montant):
                super().__init__(designation, account_number, montant)
        
        def set_debit(self, montant):
            self.montant += montant
        
        def set_credit(self, montant):
            if self.montant - montant < 0:
                raise ("value error")
            else:
                self.montant -=montant
        
        def get_montant(self):
            return self.montant
        
        

    class Product(Account):
        def __init__(self, designation, account_number, montant):
                super().__init__(designation, account_number, montant)
        
        def set_debit(self, montant):
            if self.montant - montant < 0:
                raise ("Value error")
            else:
                self.montant -=montant
        
        def set_credit(self, montant):
            self.montant += montant

        def get_montant(self):
            return self.montant

class FinancielState:
    ...



        

        

            
