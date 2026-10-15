#class creation
class Student:
    name = ""
    age = ""
    roll = ""
    level = ""

    def show_info(self):
        print(f"Name : {self.name} \nAge : {self.age} \nClass : {self.level} \nRoll : {self.roll}")
        print("---------------------------")


#object creation
st1 = Student()
st1.name = "Jakir"
st1.age = 12
st1.level = 6
st1.roll = 1

#Second object creation
st2 = Student()
st2.name = "Rayaan"
st2.age = 13
st2.level = 7
st2.roll = 2

st1.show_info()
print("")
st2.show_info()
