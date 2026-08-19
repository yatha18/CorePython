class StudentInfo:
    def __init__(self, rollno, name):
        self.rollno = rollno
        self.name = name

class Studentmarks:
    def __init__(self, rollno, marks_1, marks_2, marks_3):
        self.rollno = rollno
        self.marks_1= marks_1
        self.marks_2 = marks_2
        self.marks_3 = marks_3

    def calculate_total(self):
        return self.marks_1 + self.marks_2 + self.marks_3
    def calculate_average(self):
        return self.calculate_total() / 3

def calculate_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

class main:
    def __init__(self):
        s = int(input("Enter the number of students: "))

        for i in range(s):
            print("\nEnter details for student {i + 1}:")

            rollno = input("Roll Number: ")
            name = input("Name: ")
            print("Enter marks for three subjects:")
            marks_1 = float(input("Marks for Subject 1: "))
            marks_2 = float(input("Marks for Subject 2: ")) 
            marks_3 = float(input("Marks for Subject 3: "))

            student_info = StudentInfo(rollno, name)
            student_marks = Studentmarks(rollno, marks_1, marks_2, marks_3)
            
            total = student_marks.calculate_total()
            average = student_marks.calculate_average()
            grade = calculate_grade(average)

            print("\nStudent Results:")
            print(f"Roll Number: {student_info.rollno}")
            print(f"Name: {student_info.name}") 
            print(f"Total Marks: {total}")
            print(f"Average Marks: {average}")
            print(f"Grade: {grade}")

object = main()


