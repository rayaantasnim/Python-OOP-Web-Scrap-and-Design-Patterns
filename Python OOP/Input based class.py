#class creation
class student:
    name=""
    age=""
    level=""
    roll=""

    # constructor creation
    def __init__(self): 
        self.name=input("Enter your name: ")
        self.age=int(input("Enter your age: "))
        self.level=int(input("Enter your class: "))
        self.roll= int(input("Enter your roll: "))

     # method creation
    def show_info(self):
        print(f"Name : {self.name} \nAge:{self.age} \nClass:{self.level} \nRoll:{self.roll} ")
        print("----------------------")

    # destructor creation
    def __del__(self):  
        print(f"Student object for {self.name} is being deleted.")

#object creation
st1=student()
st1.show_info()

st2=student()
st2.show_info()