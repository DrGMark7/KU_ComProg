class BankAccount:
    def __init__(self,accountID=0 ,balance=0) -> None:
        self.accountID = accountID
        self.balance = balance
    def __str__(self) -> str:
        return f"ID: {self.accountID}, Balance: {self.balance:.2f}"
    
    def set_account_ID(self, newID):
        self.account_ID = newID

    def set_balance(self, new_balance):
        self.balance = new_balance

    def get_account_ID(self):
        return self.account_ID
    
    def get_balance(self):
        return self.balance
    
    def deposit(self,amount):
        self.balance += amount

    def withdrawal(self,amount):
        self.balance -= amount