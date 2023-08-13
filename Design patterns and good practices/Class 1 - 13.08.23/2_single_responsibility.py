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


class PaymentProcessor:
    def pay_debit(self, order, security_code):
        print("Processing debit card...")
        print(f"Verifying security code {security_code}")
        order.status = "paid"

    def pay_credit(self, order, security_code):
        print("Processing credit card..")
        print(f"Verifying security code {security_code}")
        order.status = "paid"


order = Order()
order.add_item("Item1", 70)
order.add_item("Item2", 170)
order.add_item("Item3", 20)

processor = PaymentProcessor()
processor.pay_debit(order, "1321424123")
