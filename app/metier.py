from abc import ABC, abstractmethod
import data as dt

# Classe abstraite qui servira de support aux autres classes des autres differnets types de compte
class Account(ABC):
    def __init__(self, id_account: str, class_account: str, name_account: str, debit: float, credit: float ):
    #definition des attributs de la classe
        self.id_account = id_account
        self.class_account = class_account
        self.name_account = name_account
        self.debit = debit
        self.credit = credit

        #definition des composants externes de la base de donnees
        self.connect = dt.Database()
            

    @abstractmethod
    @property
    def debit(self) -> float:
            ...

    @abstractmethod
    @debit.setter
    def debit(self, montant: float):
            ...

    @abstractmethod
    @property
    def credit(self) -> float:
            ...     

    @abstractmethod
    @credit.setter
    def credit(self, montant: float):
            ...

    @abstractmethod
    def solde(self) -> float:
            ...

class Accounts:
    class Assets(Account):
        def __init__(self,id_account: str, class_account: str, name_account: str, debit: float, credit: float ):
            super().__init__(id_account, class_account,name_account, debit, credit )

        @property
        def debit(self) -> float :
            return self.debit
        
        @debit.setter
        def debit(self, debit: float):
            self.debit += debit        

        @property
        def credit(self) -> float:
            return self.credit
        

        @credit.setter
        def credit(self, credit: float):
            self.credit += credit

        def get_solde(self):
            checking = self.get_debit > self.get_credit
            if checking:
                return self.get_debit - self.get_credit
            return self.get_credit - self.get_debit

        
    class Liabilities(Account):
        def __init__(self, designation, account_number, montant):
            super().__init__(designation, account_number, montant)

        @property
        def debit(self) -> float:
            return self.debit
                
        @debit.setter
        def debit(self, debit: float):
            self.debit += debit
                
        
        @property
        def credit(self) -> float:
            return self.credit
        
        @credit.setter
        def credit(self, credit: float):
            self.montant_credit += credit

        def get_solde(self):
            checking = self.get_debit > self.get_credit
            if checking:
                return self.get_debit - self.get_credit
            return self.get_credit - self.get_debit


    class Charge(Account):
        def __init__(self, designation, account_number, montant):
                super().__init__(designation, account_number, montant)
        
        @property
        def debit(self) -> float:
            return self.debit
        
        @debit.setter
        def debit(self, debit: float):
            self.debit += debit
        

        @property
        def credit(self) -> float:
            return self.credit

        @credit.setter
        def credit(self, credit: float):
            self.credit += credit      
        
        def get_solde(self):
            checking = self.get_debit > self.get_credit
            if checking:
                return self.get_debit - self.get_credit
            return self.get_credit - self.get_debit

    class Product(Account):
        def __init__(self, designation, account_number, montant):
                super().__init__(designation, account_number, montant)
        
        @property
        def debit(self) -> float:
            return self.debit
        
        @debit.setter
        def debit(self, debit: float):
            self.debit += debit        

        @property
        def credit(self) -> float:
            return self.credit

        @credit.setter
        def set_credit(self, credit: float):
            self.credit += credit

        def get_solde(self):
            checking = self.get_debit > self.get_credit
            if checking:
                return self.get_debit - self.get_credit
            return self.get_credit - self.get_debit


compte1 = Accounts.Assets("512","5","Banque",0,0)
compte1.set_credit(3000)
print(compte1.name_account)

class FinancielStatements:
    ...



        

        

            
