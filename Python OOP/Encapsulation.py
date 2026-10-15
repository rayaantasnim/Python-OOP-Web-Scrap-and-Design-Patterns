#Public encapsule 

print("Encapsulation - Public Mode")
class Students:
    def __init__(self,name):
        self.name = name    #Public methode

obj = Students("Yasir") 
print(obj.name) 
# -> Yasir; direct access

obj.name = "Rahim"
print (obj.name)
# -> Rahim
#Can be changed any time when need


#Protected mode
print("")
print("----------------------")
print("Protected encapsule")


class Person:
    def __init__(self):
        self._age = 20    #Protected, not changable

class Student(Person):
    def show(self):
        print("Age:", self._age)

obj = Student()
obj.show() 
#Access from sub class, not direct

print(obj._age) 
#Can be printed, not correct yet


#Private mode - Highest security
#only readable

print("")
print("----------------------")
print("Private mode")

class Account: 
    def __init__(self):
        self.__balance = 1000 #Privare mode
    
    def show_balance(self):
        print("Balance:", self.__balance)

object = Account()
object.show_balance()
#Can be accessed through methode


#print (obj.__balance)
# -> Invalid 

#Methodes of private encapsule
print("Methodes of private encapsule")

print("Methode Getter: only read")
print("Methode Setter: can be updated")
print("----------------------")


class Stu():
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get(self): #Getter Methode
        return(self.__age)
    
    def set(self, new):
        if (new>0):
            self.__age = new
        
        else:
            print ("Cannot be proceed as you entered negative integer.")

print("")
obj2 = Stu("Rayaan Tasnim", 12)
print("Age:", obj2.get())
#Getter Methode, can be read

obj2.set(20) #Setter methode to update the value
print("New updated age:", obj2.get())

#obj2.__age = 9999 
# -> Declares new variable, not update the object
#Can't be updated directly 