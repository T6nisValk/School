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


class PaymentProcessorSMS(PaymentProcessor):
    @abstractmethod
    def auth_sms(self, code):
        pass


class DebitPaymentProcessor(PaymentProcessorSMS):
    def __init__(self, security_code):
        self.security_code = security_code
        self.verified = False

    def pay(self, order, security_code):
        print("Processing debit card...")
        print(f"Verifying security code {security_code}")
        order.status = "paid"

    def auth_sms(self, code):
        print(f"Verifying SMS code {code}")
        self.verified = True
        print("Verified!")


class CreditPaymentProcessor(PaymentProcessorSMS):
    def __init__(self, security_code):
        self.security_code = security_code
        self.verified = False

    def pay(self, order, security_code):
        print("Processing credit card..")
        print(f"Verifying security code {security_code}")
        order.status = "paid"

    def auth_sms(self, code):
        print(f"Verifying SMS code {code}")
        self.verified = True
        print("Verified!")


class PayPalPaymentProcessor(PaymentProcessorSMS):
    def __init__(self, email):
        self.email = email
        self.verified = False

    def pay(self, order):
        print("Processing PayPal account...")
        print(f"Verifying your email {self.email}")
        order.status = "paid"

    def auth_sms(self, code):
        print(f"Verifying SMS code {code}")
        self.verified = True
        print("Verified!")


order = Order()
order.add_item("Item1", 70)
order.add_item("Item2", 170)
order.add_item("Item3", 20)
print(order.total_price())

processor = PayPalPaymentProcessor("something@something.com")
processor.auth_sms("0000")
processor.pay(order)

if order.status == "paid":
    print("Payment succeeded!")
