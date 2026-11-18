from abc import ABC, abstractmethod
import data as dt


# Classe abstraite qui servira de support aux autres classes des autres differnets types de compte
class Account(ABC):
    def __init__(self, id_account: int = None, number_account: str = None, class_account: str = None, name_account: str = None, debit: float = 0.0, credit: float = 0.0 ):
    #definition des attributs de la classe
        self.id_account = id_account
        self.number_account = number_account
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
        def __init__(self, id_account: int = None, number_account: str = None, class_account: str = None, name_account: str = None, debit: float = 0.0, credit: float = 0.0 ):
            super().__init__(id_account, number_account, class_account, name_account, debit, credit )

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
        
        def insert(self):
            self.connect.insert(self.id_account, self.number_account, self.class_account, self.name_account, self.debit, self.credit)

        
    class Liabilities(Account):
        def __init__(self, id_account: int = None, number_account: str = None, class_account: str = None, name_account: str = None, debit: float = 0.0, credit: float = 0.0):
            super().__init__(id_account, number_account, class_account, name_account, debit, credit)

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

        def insert(self):
            self.connect.insert(self.id_account, self.number_account, self.class_account, self.name_account, self.debit, self.credit)
        
    class Charge(Account):
        def __init__(self, id_account: int = None, number_account: str = None, class_account: str = None, name_account: str = None, debit: float = 0.0, credit: float = 0.0):
                super().__init__(id_account, number_account, class_account, name_account, debit, credit)
        
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
        
        def insert(self):
            self.connect.insert(self.id_account, self.number_account, self.class_account, self.name_account, self.debit, self.credit)
        

    class Product(Account):
        def __init__(self, id_account: int = None, number_account: str = None, class_account: str = None, name_account: str = None, debit: float = 0.0, credit: float = 0.0):
                super().__init__(id_account, number_account, class_account, name_account, debit, credit)
        
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

        def insert(self):
            self.connect.insert(self.id_account, self.number_account, self.class_account, self.name_account, self.debit, self.credit)


cmpte = Accounts.Assets(None, "512", "5","Banque",0,0)
cmpte.debit = 400
cmpte.credit = 300
cmpte.insert()  


class FinancialStatements:
    ...
    class Journal:
         ...








        

        

            
