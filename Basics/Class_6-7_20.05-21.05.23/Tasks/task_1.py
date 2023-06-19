from datetime import datetime


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def car_age(self):
        current_year = datetime.now().year
        return current_year - self.year


class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year)
        self.battery_size = battery_size


skoda = Car('Skoda', 'Fabia', 2018)
print(f"{skoda.make} {skoda.model}'s age is {skoda.car_age()}")

skoda_electric = ElectricCar('Skoda', 'Fabia', 2018, "240kWh")
print(f"Electric {skoda_electric.make} {skoda_electric.model}'s age is {skoda_electric.car_age()},"
      f" with a battery size of {skoda_electric.battery_size}.")
