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


account1 = Account('John', '$100')

#print(type(account1))
#print(account1.name)
#print(account1.capital)
#account1.account_details()