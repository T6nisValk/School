import abc
from collections import deque
import time


class Client:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @abc.abstractmethod
    def __str__(self):
        pass


class Woman(Client):
    def __str__(self):
        return f"Madam {self.first_name} {self.last_name}"


class Man(Client):
    def __str__(self):
        return f"Mr {self.first_name} {self.last_name}"


class Child(Client):
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class FiFolist:
    def __init__(self):
        self.queue = []

    def append(self, data):
        self.queue.append(data)

    def pop(self):
        removed_client = self.queue.pop(0)
        return removed_client


class CashRegister:
    def __init__(self):
        self.queue = FiFolist()

    def add_client(self, client):
        self.queue.append(client)
        print(f"{client} joined the queue")

    def process(self):
        client = self.queue.pop()
        print(f"{client} has been serviced.")


class FasterCashRegister(CashRegister):

    def __init__(self):
        super().__init__()
        self.queue = deque()

    def process(self):
        client = self.queue.popleft()
        print(f"{client} has been serviced.")


client1 = Woman("Anna", "Johnson")
client2 = Man("John", "Smith")
client3 = Child("Chris", "Novak")

cr = CashRegister()

cr.add_client(client1)
cr.add_client(client2)
cr.add_client(client3)

print("-" * 120)

cr.process()
cr.process()
cr.process()

print("-" * 120)

start = time.time()
cr = CashRegister()
for i in range(10000):
    cr.add_client(client1)
for i in range(10000):
    cr.process()
end = time.time()

start2 = time.time()
cr = FasterCashRegister()
for i in range(10000):
    cr.add_client(client1)
for i in range(10000):
    cr.process()
end2 = time.time()

print(f"Time for normal cash register: {end - start}\n"
      f"Time for fast cash register: {end2 - start2}")
