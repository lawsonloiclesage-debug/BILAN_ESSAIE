import data as dt


class Assets:
    def __init__(self, id_account: int = None, number_account: str = None, class_account: str = None, name_account: str = None, debit: float = 0.0, credit: float = 0.0 ):
        self.id_account = id_account
        self.number_account = number_account
        self.class_account = class_account
        self.name_account = name_account
        self._debit = debit
        self._credit = credit
        self.connect = dt.Database()

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
            return self._debit - self._credit
        return self._credit - self._debit
    
    def insert(self):
        self.connect.insert(self.id_account, self.number_account, self.class_account, self.name_account, self.debit, self.credit)

    
class Liabilities:
    def __init__(self, id_account: int = None, number_account: str = None, class_account: str = None, name_account: str = None, debit: float = 0.0, credit: float = 0.0):
        self.id_account = id_account
        self.number_account = number_account
        self.class_account = class_account
        self.name_account = name_account
        self._debit = debit
        self._credit = credit
        self.connect = dt.Database()

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
    
class Charge:
    def __init__(self, id_account: int = None, number_account: str = None, class_account: str = None, name_account: str = None, debit: float = 0.0, credit: float = 0.0):
        self.id_account = id_account
        self.number_account = number_account
        self.class_account = class_account
        self.name_account = name_account
        self._debit = debit
        self._credit = credit
        self.connect = dt.Database()
    
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
    

class Product:
    def __init__(self, id_account: int = None, number_account: str = None, class_account: str = None, name_account: str = None, debit: float = 0.0, credit: float = 0.0):
        self.id_account = id_account
        self.number_account = number_account
        self.class_account = class_account
        self.name_account = name_account
        self._debit = debit
        self._credit = credit
        self.connect = dt.Database()
    
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

"""
cmpte = Accounts.Assets(None,"53", "5","Caisse",0,0)
cmpte.debit = 1300
cmpte.credit = 400
cmpte.insert()
  
"""

class FinancialStatements:
    ...
    class Journal:
         ...








        

        

            
