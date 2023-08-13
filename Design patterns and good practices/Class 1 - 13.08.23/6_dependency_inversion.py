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


class Authorizer(ABC):
    @abstractmethod
    def is_authorized(self):
        pass


class AuthorizerSMS(Authorizer):
    def __init__(self):
        self.is_authorized = False

    def verify_code(self, code):
        print(f"Eyy congratzz on doing auth so well with code {code}")
        self.is_authorized = True

    def is_authorized(self):
        return self.is_authorized


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order):
        pass


class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code, authorizer):
        self.security_code = security_code
        self.authorizer = authorizer

    def pay(self, order):
        if self.authorizer.is_authorized() is not True:
            print("Not authorized")
            return
        print("Processing debit card...")
        print(f"Verifying security code {self.security_code}")
        order.status = "paid"


class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code
        self.verified = False

    def pay(self, order):
        print("Processing credit card..")
        print(f"Verifying security code {self.security_code}")
        order.status = "paid"

    def auth_sms(self, code):
        print(f"Verifying SMS code {code}")
        self.verified = True
        print("Verified!")


class PayPalPaymentProcessor(PaymentProcessor):
    def __init__(self, email, authorizer):
        self.email = email
        self.authorizer = authorizer
        self.verified = False

    def pay(self, order):
        if self.authorizer.is_authorized is not True:
            print("Not authorized")
            return
        print("Processing PayPal account...")
        print(f"Verifying your email {self.email}")
        order.status = "paid"


order = Order()
order.add_item("Item1", 70)
order.add_item("Item2", 170)
order.add_item("Item3", 20)
print(order.total_price())

authorizer = AuthorizerSMS()
authorizer.verify_code(121212)

processor = PayPalPaymentProcessor("something@something.com", authorizer)


if order.status == "paid":
    print("Payment succeeded!")
