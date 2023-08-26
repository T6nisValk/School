from abc import ABC, abstractmethod


class Logger(ABC):
    def __init__(self, next_logger):
        self.next_logger = next_logger

    @abstractmethod
    def make_entry(self, message):
        pass

    def log(self, message):
        self.make_entry(message)

        if self.next_logger is None:
            return
        self.next_logger.log(message)


class FileLogger(Logger):
    def make_entry(self, message):
        print(f"{' FILE '.center(22, '-')} => {message}")


class ConsoleLogger(Logger):
    def make_entry(self, message):
        print(f"{' CONSOLE '.center(22, '-')} => {message}")


class DatabaseLogger(Logger):
    def make_entry(self, message):
        print(f"{' DATABASE '.center(22, '-')} => {message}")


if __name__ == "__main__":
    console = ConsoleLogger(None)
    _file = FileLogger(console)
    database = DatabaseLogger(_file)

    database.log("Test")
