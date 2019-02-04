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

    def __init__(self,account1):
        self.account1 = account1
