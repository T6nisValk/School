class Addition:
    def __init__(self):
        self.number = 0

    def add(self, number_to_add):
        self.number += number_to_add

    def state(self):
        print(self.number)


if __name__ == "__main__":
    instance_1 = Addition()
    instance_2 = Addition()
    instance_3 = Addition()

    instances = [instance_1, instance_2, instance_3]
    for instance in instances:
        instance.state()
