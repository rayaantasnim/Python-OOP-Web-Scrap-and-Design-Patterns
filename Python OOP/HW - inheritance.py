class Vehicle:
    # class variable
    unit = "Km/H speed"

    def __init__(self, speed):
        # declare variable
        self.speed = speed   

    def travel_time(self, distance):
        # Universal Formula = distance / speed
        return (distance / self.speed)

class Car(Vehicle):
    def __init__(self, speed, distance):
        # Call the "init" of parent class with "Super"
        super().__init__(speed)
        self.distance = distance

    def show_time(self): 
        #Final Output
        time = super().travel_time(self.distance)
        print(f"The Car will take {time} hours to cover {self.distance} km at {self.speed} {Vehicle.unit}.")


# User Input & Final Result for car
car_speed = int(input("Enter car speed (kilo meter per hour): "))
car_distance = int(input("Enter car distance (kilo meter): "))
car1 = Car(car_speed, car_distance)
car1.show_time()

#Class - Bike
class Bike(Vehicle):
    def __init__(self, speed, distance):
        super().__init__(speed)
        self.distance = distance

    def show_time(self):
        #Final Output
        time = super().travel_time(self.distance)
        print(f"The Bike will take {time} hours to cover {self.distance} km at {self.speed} {Vehicle.unit}.")


#Break for second input procedure
print("")
print("----------------------")
print("")

#User Input & Final Result for bike
bike_speed = int(input("Enter bike speed (kilo meter per hour): "))
bike_distance = int(input("Enter bike distance (kilo meter): "))
bike1 = Bike(bike_speed, bike_distance)
bike1.show_time()