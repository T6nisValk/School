class Observer:
    def update(self, *args, **kwargs):
        print(f"I see things: {args}")


class Observable:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self, *args, **kwargs):
        for observer in self.observers:
            observer.update(*args, **kwargs)


observer = Observer()
thing = Observable()

thing.add_observer(observer)
thing.notify_observers("ASKSKS")
