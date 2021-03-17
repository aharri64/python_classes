class BankAccount():
    def __init__(self, checkings, savings):
        self.savings = savings
        self.balance = checkings

    def __str__(self):
        return f"you have ${self.balance} in your checking account, and {self.savings} in savings account"

    def withdraw(self, transaction):
        if(transaction > 0):
            self.balance -= transaction
            if(self.balance < transaction):
                return f"{self.balance} overdrawn"
            else:
                return f"you withdrew {transaction}"
        else:
            return f"not enough to withdraw"

    def deposit(self, amount):
        self.balance += amount
        return f"new balance is {self.balance}"

    def accumulate_interest(self):
        self.balance = self.balance + (self.balance * 0.02)
        return f"interest balance ${self.balance}"


class ChildrensAccount():
    def __init__(self, checkings, savings):
        self.savings = savings
        self. balance = checkings

    def __str__(self):
        return f"you have ${self.balance} in your checking account, and {self.savings} in savings account"

    def withdraw(self, transaction):
        if(transaction > 0):
            self.balance -= transaction
            if(self.balance < transaction):
                return f"{self.balance} overdrawn"
            else:
                return f"you withdrew {transaction}"
        else:
            return f"not enough to withdraw"

    def deposit(self, amount):
        self.balance += amount
        return f"new balance is {self.balance}"

    def accumulate_interest(self):
        self.balance = self.balance + 10
        return f"interest balance ${self.balance}"


class OverdraftAccount():
    def __init__(self, checkings, savings):
        self.savings = savings
        self.balance = checkings

    def __str__(self):
        return f"you have ${self.balance} in your checking account, and {self.savings} in savings account"

    def withdraw(self, transaction)
