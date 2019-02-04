"""
Object Oriented Programming Challenge
For this challenge, create a bank account class that has two attributes:
    owner
    balance
and two methods:
    deposit
    withdraw

As an added requirement, withdrawals may not exceed the available balance.
Instantiate your class, make several deposits and withdrawals, and test to
make sure the account can't be overdrawn.
"""
class Account:

    def __init__(self,name,capital):
        self.name = name
        self.capital = capital

    def account_details(self):
        print("Account name: {}\nAccount capital: {}".format(self.name, self.capital))

    def account_deposit(self):
        print("Deposit accepted.")
        return self.capital + deposit

    def account_withdrawal(self):
        if withdrawal > self.capital:
            print("Funds unavailable.")
        else:
            print("Withdrawal accepted.")
            return self.capital - withdrawal


account1 = Account('John', 100)
deposit = 150
withdrawal = 300
#print(type(account1))
#print(account1.name)
print(account1.capital)
#account1.account_details()
print(account1.account_deposit())
print(account1.account_withdrawal())
