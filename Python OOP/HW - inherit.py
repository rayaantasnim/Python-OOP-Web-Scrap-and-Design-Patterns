#Main source class
class Vehicle:
    distance = 1000

    def __init__(self, speed):
        # declare variable
        self.speed = speed 

#Car Class
class Car(Vehicle):
    def __init__(self, speed):
        super().__init__(speed)
        self.distance = super().distance
    
    def show_time(self): 
        #Final Output
        time = (self.distance/self.speed)
        print(f"The Car will take {time} hours to cover 1000 km at {self.speed} km/h speed.")

#User Input:
print("The distance is 1000 km.")
a = int(input("Enter your car's speed: "))
car1 = Car(a)
car1.show_time()

#Break for second input procedure
print("")
print("----------------------")
print("")

#Bike Class
class Bike(Vehicle):
    def __init__(self, speed):
        super().__init__(speed)
        self.distance = super().distance
    
    def show_time(self): 
        #Final Output
        time = (self.distance/self.speed)
        print(f"The bike will take {time} hours to cover 1000 km at {self.speed} km/h speed.")

#User Input
print("The distance is 1000 km.")
b = int(input("Enter your bike's speed:  "))
bike1 = Bike(b)
bike1.show_time()