from savingsAccount import savingsAccount

class Bank(object):
    customers = 0

    def __init__(self):
        self._accounts = {}

    def __str__(self):
        return "\n".join(map(str, self._accounts.values()))

    def add(self, account):
        self._accounts[account.getPin()] = account
        Bank.customers += 1

    def getNumOfCustomers(self):
        if Bank.customers == 1:
            return "There is " + str(Bank.customers) + " customer at the bank."
        else:
            return "There are " + str(Bank.customers) + " customers at the bank."
