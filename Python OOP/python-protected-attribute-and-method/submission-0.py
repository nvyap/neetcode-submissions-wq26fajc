class Account:
    def __init__(self,name:str,balance:int):
        self.name = name
        self.balance = balance
    
    def _balance(self,balance:int):
        print(f"Balance: ${self.balance}")
    
    def title(self):
        pass
    
    def display_balance(self)-> None:
        self._balance(self.balance)


# Do not modify the code below this line
account = Account("John", 1000)
account.display_balance()
