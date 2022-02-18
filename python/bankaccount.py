class Account:
    
    balance = 0
    
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance
    
    def __str__(self):
        return f"Account owner: {self.owner}\nAccount balance: {self.balance}"
        
    def deposit(self, dep_amount):
        self.balance += dep_amount
        print("Deposit Accepted")
        
    
    def withdraw(self, with_amount):
        if self.balance > with_amount:
            self.balance -= with_amount
            print("Withdraw Acepted")
        else:
            print("Funds Unavialable")
            print(f"{self.owner}, you only have ${self.balance} in your account.")
    
    
    