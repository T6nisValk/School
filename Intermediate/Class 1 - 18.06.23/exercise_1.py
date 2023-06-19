from math import sqrt


class Calculator:
    def __init__(self):
        self.memory = 0

    def add(self, num):
        self.memory += num
        return self.memory

    def subs(self, num):
        self.memory -= num
        return self.memory

    def div(self, num):
        self.memory /= num
        return self.memory

    def mult(self, num):
        self.memory *= num
        return self.memory

    def squareroot(self):
        self.memory = sqrt(self.memory)
        return self.memory

    def clear(self):
        self.memory = 0
        return self.memory
