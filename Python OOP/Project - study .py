# Parent Class
class Student:
    def __init__(self, name, daily_study_hours, subjects):
        self.name = name
        self.daily_study_hours = daily_study_hours
        self.subjects = subjects


    def calculate_total_study(self, days_practiced):
        return (self.daily_study_hours * days_practiced)


    def analyze_performance(self, total_study):
        recommended_hours = self.subjects * 20
        buffer = recommended_hours * 0.05 

        if (total_study > recommended_hours):
            return "Way to go, you are a hardworking student."
        
        elif (total_study == recommended_hours):
            return "On Track, go ahead."
        
        elif (total_study >= recommended_hours - buffer):
            return "Be careful, you might need discipline."
        
        else:
            return "You Need Improvement."
    
    def show_summary(self, name, daily_study_hours, subjects):
        print(f"Name: {self.name}")
        print(f"Daily Study Hours: {self.daily_study_hours}")
        print(f"Subjects: {self.subjects}")

# Child Class 1: Science Student
class ScienceStudent(Student):
    def __init__(self, name, daily_study_hours, subjects, lab_hours):
        super().__init__(name, daily_study_hours, subjects)
        self.lab_hours = lab_hours

    def show_summary(self, name, daily_study_hours, subjects, lab_hours, days_practiced):
        total_study = self.calculate_total_study(days_practiced) + self.lab_hours
        print("\n--- Science Student Summary ---")
        super().show_summary(name, daily_study_hours, subjects) 


        print(f"Lab Hours: {self.lab_hours}")
        print(f"Total Study Hours (including lab): {total_study}")
        print(f"Recommended Hours: {self.subjects * 20}")
        print(f"Comment: {self.analyze_performance(total_study)}")

# Child Class 2: Arts Student
class ArtsStudent(Student):
    def __init__(self, name, daily_study_hours, subjects, practice_hours):
        super().__init__(name, daily_study_hours, subjects)
        self.practice_hours = practice_hours



    def show_summary(self, name, daily_study_hours, subjects, practice_hours, days_practiced):
        total_study = self.calculate_total_study(days_practiced) + self.practice_hours
        print("\n--- Arts Student Summary ---")
        super().show_summary(name, daily_study_hours, subjects) 

        print(f"Practice Hours: {self.practice_hours}")
        print(f"Total Study Hours (including practice): {total_study}")
        print(f"Recommended Hours: {self.subjects * 20}")
        print(f"Performance: {self.analyze_performance(total_study)}")



# Child Class 3: Sports Student
class SportsStudent(Student):
    def __init__(self, name, daily_study_hours, subjects, training_hours):
        super().__init__(name, daily_study_hours, subjects)
        self.training_hours = training_hours



    def show_summary(self, name, daily_study_hours, subjects, training_hours, days_practiced):
        total_study = self.calculate_total_study(days_practiced) + self.training_hours
        print("\n--- Sports Student Summary ---")
        super().show_summary(name, daily_study_hours, subjects)


        print(f"Training Hours: {self.training_hours}")
        print(f"Total Study Hours (including training): {total_study}")
        print(f"Recommended Hours: {self.subjects * 20}")
        print(f"Performance: {self.analyze_performance(total_study)}")


# User Input with while loop
while True:
    print("\nChoose your student type:")
    print("1. Science Student \n2. Arts Student \n3. Sports Student")
    ans = input("Enter your desired option: ")
    ans = ans.lower()
    ans = ans.lstrip()

    if (ans == "1" or ans == "science student" 
        or ans == "2" or ans == "arts student" 
        or ans == "3" or ans == "sports student"):

        name = input("Enter student's name: ")
        daily_hours = float(input("Enter daily study hours: "))
        subjects = int(input("Enter number of subjects: "))
        days_practiced = int(input("Enter number of days practiced in month: "))


        if (ans == "1" or ans == "science student"):
            lab = float(input("Enter total lab hours for the month: "))
            student = ScienceStudent(name, daily_hours, subjects, lab)
            student.show_summary(name, daily_hours, subjects, lab, days_practiced)



        elif (ans == "2" or ans == "arts student"):
            practice = float(input("Enter total arts practice hours for the month: "))
            student = ArtsStudent(name, daily_hours, subjects, practice)
            student.show_summary(name, daily_hours, subjects, practice, days_practiced)


        else:
            training = int(input("Enter total training hours for the month: "))
            student = SportsStudent(name, daily_hours, subjects, training)
            student.show_summary(name, daily_hours, subjects, training, days_practiced)

    else:
        print("\nInvalid Choice.")
        break