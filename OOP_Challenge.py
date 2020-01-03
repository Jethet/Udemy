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

    def account_deposit(self, deposit):
        self.capital = self.capital + deposit
        print("Deposit of {} added to the balance.".format(deposit))
        print("The current balance in your account is: {}".format(self.capital))


    def account_withdrawal(self, withdrawal):
        if self.capital >= withdrawal:
            self.capital = self.capital - withdrawal
            print("Withdrawal accepted.")
        else:
            print("Funds unavailable")

    def __str__(self):
        return f"Owner: {self.name}\nBalance: {self.capital}"


account1 = Account('John', 100)
print(account1)
print(account1.name)
print(account1.capital)
account1.account_details()
account1.account_deposit(100)
account1.account_details()
account1.account_withdrawal(600)
