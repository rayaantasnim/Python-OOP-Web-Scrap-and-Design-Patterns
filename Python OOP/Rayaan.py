class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def show_info(self):
        print (f"The name of the employee: {self.name} \nID number: {self.id}")

class FullTime(Employee):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary
    
    def show_salary(self):
        final = (self.salary + (self.salary* 20/100))
        print (f"His final salary amount is {final}")

class PartTime(Employee):
    def __init__(self, name, id, hourly_rate, hours_worked):
        super().__init__(name, id)
        self.rate = hourly_rate
        self.hour = hours_worked
    
    def show_salary(self):
        final = (self.hour * self.rate)
        print (f"His Final salary amount is {final}")

class HighClassOfficer(Employee):
    def __init__(self, name, id, salary, position):
        super().__init__(name, id)
        self.position = position
        self.salary = salary
    
    def show_salary(self):
        final = (self.salary + (self.salary * 25/100))
        print(f"This {self.position} will get {final} BDT per month.")

while True:
    print("1. Full Time Employee")
    print("2. Part Time Employee")
    print("3. high positioned Officer")
    choice = int(input("Enter your choice number:"))
    print("")

    name = input("Enter employee's name:")
    id = int(input("Enter the ID number:"))

    if(choice == 1):
        salary = int(input("Enter the amount of salary:"))
        print("")

        emp = FullTime(name, id, salary)
        emp.show_info()
        emp.show_salary()
        print("")
    
    elif(choice == 2):
        rate = int(input("Enter the hourly rate of of the job:"))
        hour = int(input("How many hours do you work every day:"))
        print("")

        emp = PartTime(name, id, rate, hour)
        emp.show_info()
        emp.show_salary()
        print("")

    elif(choice == 3):
        salary = int(input("Enter this officer's salary here:"))
        position = input("Enter his position in the company:")
        print("")

        emp = HighClassOfficer(name, id, salary, position)
        emp.show_info()
        emp.show_salary()
        print("")

    else:
        print("")
        print("Invalid Choice")