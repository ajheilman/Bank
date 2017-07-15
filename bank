class Bank(object):
    customers = 0
    
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance
        Bank.customers += 1

    def displayCustomers(self):
        return Bank.customers
    
    def getName(self):
        return self._name

    def getBalance(self):
        return "$" + str(self._balance) + '\n'

    def deposit(self, amount):
        if amount == 0:
            return "You can't deposit nothing!"
        else:
            self._balance += amount
            return self._balance

    def withdrawl(self, amount):
        if not amount.isdigit():
            return "You must enter a number!"
        elif self._balance == 0:
            return "You can't withdraw any money because you have none!"
        elif amount > self._balance:
            return "You don't have that much money to withdraw!"
        elif amount == 0:
            return "You can't withdraw nothing!"
        else:
            self._balance -= amount
            return self._balance

    def __str__(self):
        return "Name: " + self._name + "\nBalance: $" + str(self._balance) + '\n'
