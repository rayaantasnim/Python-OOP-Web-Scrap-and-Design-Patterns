#Preparing class for car:
class Car:
    Name = ""
    Brand = ""
    Color = ""
    Price = ""
    Horsepower = ""

    def __init__(self, n, b, c, p, h):
        self.Name = n
        self.Horsepower = h
        self.Brand = b
        self.Color = c
        self.Price = p

    def show(self):
        print (f"Car Name: {self.Name} \nManufacturur Brand: {self.Brand} \nColor Shade: {self.Color} \nPrice: {self.Price} \nHorse Power: {self.Horsepower}")
        print ("")

#First Car Info:
car1 = Car("Toyota Corrola Cross","Toyota",  "Wind Chill Pearl", "4.2 Million Tk", 170)
car1.show()

#Second car Info:
car2 = Car("Mercedes-Maybach", "Mercedes-Benz Automotive manufacturer", "Obsidian Black", "48 Million Tk" ,496)
car2.show()

#Third Car Info:
car3 = Car("KIA Sportage", "KIA Automobile", "Snow White Pearl", "6.4 Million Tk", 154)
car3.show()

#Fouth Car Info:
car4 = Car("Rolse-Royce Spectre", "Rolse-Royce Motor Car", "Black Diamond", "88 Million Tk", 577)
car4.show()

#Fifth car Info:
car5 = Car("Range Rover Sport", "Range Rover", "Light Blue", "70 Million Tk", 625)
car5.show()

#Sixth Car info:
car6 = Car("Toyota Fortuner", "Toyota", "Platinum White Pearl", "20 Million Tk", 235 )
car6.show()

#Seventh car info:
car7 = Car("BMW M8 Series", "BMW", "Black Sapphire Metallic","60 Million Tk", 625)
car7.show()

#Eighth car info:
car8 = Car("Hyundai Tucson", "Hyundai", "Serenity White Pearl", "8 Million Tk", 268)
car8.show()

#Ninth car info:
car9 = Car("Mitsubishi Outlander","Mitsubishi Motors" , "White Diamond", "6.3 Million BDT", 248)
car9.show()

#10th car info:
car10 = Car("Land Cruiser Prado", "Toyota", "Smoky Blue", "22.5 Million Tk", 326)
car10.show()