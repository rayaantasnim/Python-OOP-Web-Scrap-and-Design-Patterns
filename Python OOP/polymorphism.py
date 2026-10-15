class Car:
    def start(self):
        print("Car is starting with a key.")

class Bike:
    def start(self):
        print("Bike is starting with a kick.")

class Airplane:
    def start(self):
        print("Airplane is starting with button.")

def start_vehicle(vehicle):
    vehicle.start()

v1 = Car()
start_vehicle(v1)

v2 = Bike()
start_vehicle(v2)

v3 = Airplane()
start_vehicle(v3)