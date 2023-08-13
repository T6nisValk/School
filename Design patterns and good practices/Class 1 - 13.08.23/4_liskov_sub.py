from abc import ABC, abstractmethod


class Order:
    def __init__(self):
        self.items = []
        self.prices = []
        self.status = "open"

    def add_item(self, name, price):
        self.items.append(name)
        self.prices.append(price)

    def total_price(self):
        return sum(self.prices)


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order):
        pass


class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order, security_code):
        print("Processing debit card...")
        print(f"Verifying security code {security_code}")
        order.status = "paid"


class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order, security_code):
        print("Processing credit card..")
        print(f"Verifying security code {security_code}")
        order.status = "paid"


class PayPalPaymentProcessor(PaymentProcessor):
    def __init__(self, email):
        self.email = email

    def pay(self, order):
        print("Processing PayPal account...")
        print(f"Verifying your email {self.email}")
        order.status = "paid"


order = Order()
order.add_item("Item1", 70)
order.add_item("Item2", 170)
order.add_item("Item3", 20)
print(order.total_price())

processor = PayPalPaymentProcessor("something@something.com")
processor.pay(order)
