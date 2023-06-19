# Create a class called "BankAccount" with attributes for account number and balance.
# Add methods to the BankAccount class for depositing and withdrawing money.
# Create a subclass of BankAccount called "SavingsAccount" with an additional attribute for interest rate.
# Override the BankAccount class's withdraw method in the SavingsAccount subclass to include a fee for each withdrawal.
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def withdraw(self, amount):
        fee = amount * self.interest_rate
        self.balance -= amount + fee
        return self.balance


account_1 = BankAccount(123456789, 10)
account_2 = SavingsAccount(987654321, 20, 0.1)
print(f"Account balance: {account_1.balance} carrots\n"
      f"Savings account balance: {account_2.balance} carrots\n")
account_1.withdraw(5)
account_2.withdraw(5)
print(f"After withdrawing 5 carrots:\n\n"
      f"Account balance: {account_1.balance} carrots\n"
      f"Savings account balance: {account_2.balance} carrots\n")
