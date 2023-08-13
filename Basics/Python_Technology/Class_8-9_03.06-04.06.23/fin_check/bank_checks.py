""" this package is used to check the customer fin status"""
"""
checking fin status
checking age
checking valid estonia id
"""


# check finanical status
class FinStatus:
    def __init__(self, account_balance, debt_balance, monthly_income):
        self.account_balance = account_balance
        self.debt_balance = debt_balance
        self.monthly_income = monthly_income

    def check_fin_status(self):
        if (
            self.account_balance > 0
            and self.debt_balance == 0
            and self.monthly_income > 0
        ):
            return "You are in good financial standing"
        elif self.account_balance < 0 < self.debt_balance and self.monthly_income > 0:
            return "You are in bad financial standing"
        else:
            return "You are in neutral financial standing"


# check age
class Age:
    def __init__(self, age):
        self.age = age

    def check_age(self):
        if self.age >= 20:
            return "You can open an account"
        else:
            return "You are not old enough to open an account"


# check valid estonia id
class EstoniaID:
    def __init__(self, estonia_id):
        self.estonia_id = estonia_id

    def check_estonia_id(self):
        if len(self.estonia_id) == 11:
            return "You have a valid estonia id"
        else:
            return "You do not have a valid estonia id"
