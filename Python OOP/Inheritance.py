#Base Parent class
class Car:
    brand = "Tesla"
    model = "Model X"

    def start(self):
        print(f"This {self.brand} is started.")

    def stop(self):
        print(f"This {self.brand} is stopped.")


# Child class
class EV(Car):
    battery = 100

    def start(self):
        super().start()
        print(f"{self.brand} is starting with battery power.")

    def charge(self):
        print(f"This {self.brand} {self.model} is being charged with {self.battery} kilo-watt battery.")


car2 = EV()
car2.start()
car2.stop()
car2.charge()
print("------")
print("")

#Multi Level Inheritance:
class self_drive(EV):
    def start(self):
        super().start()
        print(f"{self.brand} is working.")
    def auto(self):
        print(f"{self.brand} {self.model} is in auto-pilot mode.")

sdc1 = self_drive()
sdc1.start()
sdc1.auto()