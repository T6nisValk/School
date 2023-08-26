from abc import ABC, abstractmethod


class Remote(ABC):
    @abstractmethod
    def execute(self, channel):
        pass


class TVRemote(Remote):
    def __init__(self, company):
        self.company = company
        self.channels = {1: "Discovery", 2: "The Cooking Show", 3: "BBC"}

    def execute(self, channel):
        if int(channel) > len(self.channels):
            return "Nothing hhaha"

        print(
            f"Clicked the remote of company {self.company} to switch the channel to {channel}"
        )
        return self.channels[channel]


class Person(ABC):
    @abstractmethod
    def click(self, command, button):
        pass

    @abstractmethod
    def see(self):
        pass


class CouchPotato(Person):
    def __init__(self):
        self.result = ""

    def click(self, command, button):
        self.result = command(button)

    def see(self):
        print(f"The TV is showing this: {self.result}")


if __name__ == "__main__":
    potatoMonster = CouchPotato()
    samsungRemote = TVRemote("SAMSUNG")

    potatoMonster.click(samsungRemote.execute, 2)
    potatoMonster.see()
