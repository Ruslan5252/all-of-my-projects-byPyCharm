class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance


    def __add__(self, other):
        print("add_call")
        if isinstance(other,BankAccount):
            return self.balance+other.balance
        if isinstance(other,(int,float)):
            return self.balance+other
        raise NotImplemented