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

    def pay(self, payment_type, security_code):
        if payment_type == "debit":
            print("Processing debit card..")
            print(f"Verifying security code {security_code}")
            self.status = "paid"

        elif payment_type == "credit":
            if payment_type == "debit":
                print("Processing credit card..")
                print(f"Verifying security code {security_code}")
                self.status = "paid"

        else:
            print(f"Unknown payment type {payment_type}")


order = Order()
order.add_item("Item1", 70)
order.add_item("Item2", 170)
order.add_item("Item3", 20)

print(order.total_price())
order.pay("debit", "12132413212")
