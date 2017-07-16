class savingsAccount(object):
    #customers = 0
    
    def __init__(self, name, balance, pin):
        self._name = name
        self._balance = balance
        self._pin = pin
        #Bank.customers += 1

    def displayCustomers(self):
        return Bank.customers
    
    def getName(self):
        return "The customer's name is: " + self._name

    def getBalance(self):
        return "$" + str(self._balance) + '\n'

    def getPin(self):
        return self._name + "'s pin number is: " + str(self._pin)

    def setPin(self, newPin):
        self._pin = newPin
        return "Your new pin number is: " + str(self._pin)

    def deposit(self, amount):
        '''if not amount.isdigit():
            return "You must enter a number!"'''
        if amount < 0:
            return "You must enter a postive number!"
        elif amount == 0:
            return "You can't deposit nothing!"
        else:
            self._balance += amount
            return "You new balance is: $" + str(self._balance)

    def withdrawl(self, amount):
        '''if not amount.isdigit():
            return "You must enter a number!"'''
        if amount < 0:
            return "You must enter a postive number!"
        elif self._balance == 0:
            return "You can't withdraw any money because you have none!"
        elif amount > self._balance:
            return "You don't have that much money to withdraw!"
        elif amount == 0:
            return "You can't withdraw nothing!"
        else:
            self._balance -= amount
            return "You new balance is: $" + str(self._balance)

    def __str__(self):
        return "Name: " + self._name + \
               "\nBalance: $" + str(self._balance) + \
               "\nPin: " + str(self._pin) + '\n'
