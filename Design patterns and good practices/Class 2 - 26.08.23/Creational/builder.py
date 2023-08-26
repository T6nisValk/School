class Builder:
    def build_part(self, element):
        pass

    def get_result(self):
        pass


class HexBuilder(Builder):
    def __init__(self):
        self.result_hex_string = ""

    def build_part(self, element):
        self.result_hex_string += f"0x{ord(element):02x} "

    def get_result(self):
        return self.result_hex_string


class UpperBuilder(Builder):
    def __init__(self):
        self.result_upper_string = ""

    def build_part(self, element):
        self.result_upper_string = element.upper()

    def get_result(self):
        return self.result_upper_string


class LowerBuilder(Builder):
    def __init__(self):
        self.result_lower_string = ""

    def build_part(self, element):
        self.result_lower_string = element.lower()

    def get_result(self):
        return self.result_lower_string


class CounterBuilder(Builder):
    def __init__(self):
        self.result_counter = 0

    def build_part(self, element):
        self.result_counter += 1

    def get_result(self):
        return self.result_counter


class Director:
    def __init__(self, file_name):
        self.file_name = file_name
        self.builder = None

    def constructor(self):
        with open(self.file_name) as f:
            for line in f:
                for char in line:
                    self.builder.build_part(char)

    def set_builder(self, builder):
        self.builder = builder

    def get_result(self):
        return self.builder.get_result()


director = Director("test.txt")
hex_builder = HexBuilder()
upper_builder = UpperBuilder()
lower_builder = LowerBuilder()
counter_builder = CounterBuilder()

director.set_builder(hex_builder)
director.constructor()
print(director.get_result())

director.set_builder(upper_builder)
director.constructor()
print(director.get_result())

director.set_builder(lower_builder)
director.constructor()
print(director.get_result())

director.set_builder(counter_builder)
director.constructor()
print(director.get_result())
