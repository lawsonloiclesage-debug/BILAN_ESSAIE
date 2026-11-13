from abc import ABC, abstractmethod
import sqlite3 as sq

class Metier:
    class Account(ABC):
        def __init__(self, designation: str, class_account: int, account_number: int, montant: float):
            self.designation = designation
            self.class_account = class_account
            self.account_number = account_number
            self.montant = montant

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





        

        

            
