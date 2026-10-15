#hierchical inharitance method overriding

# grand parent class
class car: 
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
    
    def show(self):
        print(f"{self.brand} is running with fuel now.")
        

# Child 1
class electric_car(car):
    def __init__(self,battery_size,brand,model,year):
        super().__init__(brand,model,year)
        self.battery_size = battery_size
    
    def show(self):
        super().show()
        print(f"{self.brand} {self.model} is running with {self.battery_size} battery power now.")

# Child 2
class petrol_car(car):
    def __init__(self,engine_size,brand,model,year):
        super().__init__(brand,model,year)
        self.engine_size=engine_size
    
    def show(self):
        super().show()
        print(f"{self.brand} is running with petrol oil.")

while True:
    print("1. Electric Car")
    print("2. Petrol Car")