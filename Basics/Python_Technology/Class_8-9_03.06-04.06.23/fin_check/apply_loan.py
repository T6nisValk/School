import bank_checks

client_old = int(input("How old are you? "))


def apply_loan():
    print("apply_loan")
    print(bank_checks.Age(client_old).check_age())


apply_loan()
