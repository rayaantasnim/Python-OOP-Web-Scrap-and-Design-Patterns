class car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
class EV(car):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        self.battery_size=battery
    
    def auto(self):
        print(f"{self.brand} {self.model} is working with {self.battery_size} power.")

obj = EV("Toyota", "Corrola Cross", 2000)
obj.auto()
print("-------")
print("")

class auto(EV):
    def __init__(self, brand, model, battery, auto):
        super().__init__(brand, model, battery)
        self.auto=auto
    
    def start(self):
        print(f"{self.brand} {self.model} is working by {self.auto} power.")

car1 = auto("Tesla", "Model X", "2000", "CoPilot")
car1.start()
