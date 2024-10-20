from abc import ABC


class Vehicle(ABC):
    def no_of_wheels(self):
        pass


class Cycle(Vehicle):
    def no_of_wheels(self):
        print("Cycle have 2 wheels")


class Car(Vehicle):
    def no_of_wheels(self):
        print("Car have 4 wheels")


class HeavyTruck(Vehicle):
    def no_of_wheels(self):
        print("HeavyTruck have 8 wheels")


Cycle = Cycle()
Cycle.no_of_wheels()
Car = Car()
Car.no_of_wheels()
HeavyTruck = HeavyTruck()
HeavyTruck.no_of_wheels()
