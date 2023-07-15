class SimpleClass:
    def __init__(self):
        self.num1 = 10  # Public
        self.__num2 = 20  # Private, accessible only within the class

    def sum(self):
        return self.num1 + self.__num2

    def get_num2(self):
        return self.__num2

    def set_num2(self, new_value):
        self.__num2 = new_value


obj = SimpleClass()
obj.num1 = 40
obj.set_num2(50)
print(f"sum: {obj.sum()}")
print(f"num 1: {obj.num1}")
print(f"num 2: {obj.get_num2()}")
print("-" * 120)


class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return self.__balance
        else:
            print(f"Amount must be greater than 0.")

    def withdrawl(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return self.__balance
        else:
            print(f"Invalid transaction.")

    def get_balance(self):
        return self.__balance

    def __interest(self, amount):
        self.__balance += amount


account_1 = BankAccount(200)
print(account_1.get_balance())
print("Deposit 50")
account_1.deposit(50)
print("Withdraw 75")
account_1.withdrawl(75)
print(account_1.get_balance())
