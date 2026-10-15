class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show_info(self):
        print(f"Name: {self.name}, \nAge: {self.age}" )

class Student(Person):
    school_name = "Unique Progressive School, Mymensingh"
    def __init__(self, name, age, roll, marks, class_name):
        super().__init__(name, age)
        self.roll = int(roll)              
        self.__marks = int(marks)          
        self.class_name = int(class_name)  

    def set_marks(self, marks):
        self.__marks = int(marks)

    def get_marks(self):
        return self.__marks
    
    def grade(self):
        if self.__marks >= 80:
            return 'A+'
        elif self.__marks >= 70:
            return 'A'
        elif self.__marks >= 60:
            return 'A-'
        elif self.__marks >= 50:
            return 'B'
        elif self.__marks >= 40:
            return 'C'
        elif self.__marks >= 33:
            return 'D'
        else:
            return 'F'
        
    def show_info(self):
        super().show_info()
        print(f"Roll: {self.roll} \nClass: {self.class_name} \nMarks: {self.__marks} \nGrade: {self.grade()}")

    def __del__(self):
        print(f"Student {self.name} with roll {self.roll} is being deleted.")

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def show_info(self):
        super().show_info()
        print(f"Subject: {self.subject}")

class Admin(Teacher):
    def __init__(self, name, age, subject, password):
        super().__init__(name, age, subject)
        self.password = password

    def add_student(self, student_list, stu_obj):
        student_list.append(stu_obj)
        print(f"Student {stu_obj.name} added.")

    def remove_student(self, student_list, roll, class_name):
        roll = int(roll)
        class_name = int(class_name)
        for stu_obj in student_list:
            if stu_obj.roll == roll and stu_obj.class_name == class_name:
                student_list.remove(stu_obj)
                print(f"Student {stu_obj.name} removed.")
                return
        print(f"No student found with roll {roll} in class {class_name}.")

    def update_marks(self, student_list, roll, class_name, new_marks):
        roll = int(roll)
        class_name = int(class_name)
        new_marks = int(new_marks)

        for stu_obj in student_list:
            if stu_obj.roll == roll and stu_obj.class_name == class_name:
                stu_obj.set_marks(new_marks)
                print("Marks has been updated!")
                stu_obj.show_info()
                return
        print(f"No student found with roll {roll} in class {class_name}.")


admin_list = [
    Admin("Mr. Smith", 40, "Math", "admin123"),
    Admin("Mr. Rahman", 38, "English", "admin234"),
    Admin("Mr. Karim", 42, "Science", "admin345"),
    Admin("Mr. Jamil", 39, "History", "admin456"),
    Admin("Mr. Shahid", 41, "Geography", "admin567"),
    Admin("Mr. Nayeem", 37, "Biology", "admin678")
]


student_list = [
    Student("Rahim", 12, 301, 72, 7),
    Student("Karim", 13, 302, 85, 7),
    Student("Jamil", 12, 303, 90, 7),
    Student("Shahid", 13, 304, 78, 7),
    Student("Nayeem", 12, 305, 88, 7),
    Student("Rashed", 13, 306, 95, 7),
    Student("Tariq", 12, 307, 80, 7),
    Student("Sabbir", 13, 308, 83, 7),
    Student("Imran", 12, 309, 76, 7),
    Student("Farhan", 13, 310, 92, 7)
]

def main():
    print("================================ Welcome to Student Management System ================================")
    while True:
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Update Student Marks")
        print("4. Show All Students")
        print("5. Show All Admins Information")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            roll = int(input("Enter student roll: "))        
            class_name = int(input("Enter student class: ")) 
            marks = int(input("Enter student marks: "))      
            stu_obj = Student(name, age, roll, marks, class_name)
            admin_list[0].add_student(student_list, stu_obj)

        elif choice == '2':
            roll = int(input("Enter student roll to remove: "))       
            class_name = int(input("Enter student class to remove: "))
            admin_list[0].remove_student(student_list, roll, class_name)

        elif choice == '3':
            roll = int(input("Enter student roll to update marks: "))        
            class_name = int(input("Enter student class to update marks: "))  
            new_marks = int(input("Enter new marks: "))                      
            admin_list[0].update_marks(student_list, roll, class_name, new_marks)

        elif choice == '4':
            for stu_obj in student_list:
                stu_obj.show_info()
                print("_"*50)

        elif choice == '5':
            for adm in admin_list:
                adm.show_info()
                print("_"*50)
                print("")

        elif choice == '6':
            print("Exiting the system. Goodbye!")
            break

# admin login panel
print('==================== Admin Login Required ====================')
for i in range(3):
    admin_name = input("Enter admin name: ").lower()
    admin_password = input("Enter admin password: ")
   
    for adm in admin_list:
        if admin_name == adm.name.lower() and admin_password == adm.password:
            print("Login successful!")
            main()
            break   
    else:
        print("Invalid credentials, please try again.")