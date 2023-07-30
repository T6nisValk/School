import abc
from collections import deque
import time


class Client(abc.ABC):
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
        return self.queue.pop(0)


class CashRegister:
    def __init__(self):
        self.queue = FiFolist()

    def add_client(self, client):
        self.queue.append(client)
        # print(f"{client} joined the queue.")

    def process(self):
        client = self.queue.pop()
        # print(f"{client} left the store.")


class FasterCashRegister(CashRegister):

    def __init__(self):
        super().__init__()
        self.queue = deque()

    def process(self):
        client = self.queue.popleft()
        # print(f"{client} has left the store.")


client1 = Woman("Anna", "Johnson")
client2 = Man("John", "Smith")
client3 = Child("Chris", "Novak")

cr = FasterCashRegister()

cr.add_client(client1)
cr.add_client(client2)
cr.add_client(client3)

# print("-" * 120)

cr.process()
cr.process()
cr.process()

# print("-" * 120)

start = time.perf_counter()
cr = CashRegister()
for i in range(100000):
    cr.add_client(client1)
for i in range(100000):
    cr.process()
end = time.perf_counter()

start2 = time.perf_counter()
fcr = FasterCashRegister()
for i in range(100000):
    fcr.add_client(client1)
for i in range(100000):
    fcr.process()
end2 = time.perf_counter()

print(f"Time for normal cash register: {end - start}\n"
      f"Time for fast cash register: {end2 - start2}")
