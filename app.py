# 1 Understand difference between objects and classes
car = {
    "make": "Rolls Royce",
    "model": "Ghost",
    "color": "white"
}


class CoffeeCup():
    def __init__(self, capacity):  # ? this is similar to a consturctor in JS
        self.capacity = capacity
        self.amount = 0

    def fill(self):  # ? method on CoffeeCup
        self.amount = self.capacity

    def empty(self):  # ? method on CoffeeCup
        self.amount = 0

    def drink(self, amount):  # ? method
        self.amount -= amount
        if (self.amount == 0):
            self.amount = 0

    # Understand how classes are defined
    # Understand how objects are initia112liZA zed
    # Understand instance variables and instance methods
steves_cup = CoffeeCup(12)  # a fancy latte
seans_cup = CoffeeCup(16)  # gas station drip
brandis_cup = CoffeeCup(2)  # a quick expresso

steves_cup.fill()  # ? dot ntation when using methods
steves_cup.drink(12)  # ? method chaining
print(steves_cup.amount)
print(help(steves_cup))
# Understand class variables and class methods
# Utilize the self keyword
# Understand method chaining in a class


# 1 - Bank accounts should be created with the kind of account (like "savings" or "checking").
# 2 - Each account should keep track of it's current balance.
# 3 - Each account should have access to a deposit and a withdraw method.
# 4 - Each account should start with a balance set to zero.
# 5 - return the amount withdrawn, for convenience.
