from abc import ABC, abstractmethod
import data as dt

# Classe abstraite qui servira de support aux autres classes des autres differnets types de compte
class Account(ABC):
    def __init__(self, id_account: str, class_account: str, name_account: str, debit: float, credit: float ):
    #definition des attributs de la classe
        self.id_account = id_account
        self.class_account = class_account
        self.name_account = name_account
        self._debit = debit
        self._credit = credit

        #definition des composants externes de la base de donnees
        self.connect = dt.Database()
            
    @property
    @abstractmethod
    def debit(self) -> float:
            ...
    @debit.setter
    @abstractmethod
    def debit(self, montant: float):
            ...
    @property
    @abstractmethod
    def credit(self) -> float:
            ...     
    @credit.setter
    @abstractmethod
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
            return self._debit
        
        @debit.setter
        def debit(self, debit: float):
            self._debit += debit        

        @property
        def credit(self) -> float:
            return self._credit
        

        @credit.setter
        def credit(self, credit: float):
            self._credit += credit

        def solde(self):
            checking = self._debit > self._credit
            if checking:
                return self.get_debit - self._credit
            return self._credit - self._debit

        
    class Liabilities(Account):
        def __init__(self, designation, account_number, montant):
            super().__init__(designation, account_number, montant)

        @property
        def debit(self) -> float:
            return self._debit
                
        @debit.setter
        def debit(self, debit: float):
            self._debit += debit
                
        
        @property
        def credit(self) -> float:
            return self._credit
        
        @credit.setter
        def credit(self, credit: float):
            self._credit += credit

        def solde(self):
            checking = self._debit > self._credit
            if checking:
                return self._debit - self._credit
            return self._credit - self._debit


    class Charge(Account):
        def __init__(self, designation, account_number, montant):
                super().__init__(designation, account_number, montant)
        
        @property
        def debit(self) -> float:
            return self._debit
        
        @debit.setter
        def debit(self, debit: float):
            self._debit += debit
        

        @property
        def credit(self) -> float:
            return self._credit

        @credit.setter
        def credit(self, credit: float):
            self._credit += credit      
        
        def solde(self):
            checking = self._debit > self._credit
            if checking:
                return self._debit - self._credit
            return self._credit - self._debit

    class Product(Account):
        def __init__(self, designation, account_number, montant):
                super().__init__(designation, account_number, montant)
        
        @property
        def debit(self) -> float:
            return self._debit
        
        @debit.setter
        def debit(self, debit: float):
            self._debit += debit        

        @property
        def credit(self) -> float:
            return self._credit

        @credit.setter
        def credit(self, credit: float):
            self._credit += credit

        def solde(self):
            checking = self._debit > self._credit
            if checking:
                return self._debit - self._credit
            return self._credit - self._debit


compte1 = Accounts.Assets("512","5","Banque",0,0)
compte1._credit(300.0)
print(compte1.name_account)

class FinancielStatements:
    ...



        

        

            
