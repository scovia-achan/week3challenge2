class BankAccount:
    def __init__(self):
        self.account_balance = 0
        self.flag = 0
              

    def get_balance(self):
        if self.flag ==1:
            return self.account_balance
        raise ValueError("account closed. you cannot carry out transactions")

    def open(self):
        self.account_balance = 0
        self.flag =1
        

    def deposit(self, amount):
        self.amount = amount
        if self.flag !=1:
            raise ValueError("account closed")
        if amount < 0:
            raise ValueError("Invalid; amount cannot be negative")

        self.account_balance += amount
        return self.account_balance
        

    def withdraw(self, amount):
        if self.flag !=1:
            raise ValueError("account closed; you cannot deposit")
        if amount < 0:
            raise ValueError("Invalid; amount cannot be negative")
        if amount > self.get_balance():
            raise ValueError("You cannot withdraw a negative amount")

        self.account_balance -= amount
        return self.account_balance

    def close(self):
        self.flag == 0
