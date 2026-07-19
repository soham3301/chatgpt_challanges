
#? NOTE:-
#? There are 2 semesters - This is a one year course.
#? Every Semester has 3 subjects - total 6 subjects.

class Subjects:
    def __init__(self, sub1, sub2, sub3, total_mark_of_each_subject):
        self.sub1 = {
            "subject_name":sub1,
            "total_marks":total_mark_of_each_subject
        }
        self.sub2 = {
            "subject_name":sub2,
            "total_marks":total_mark_of_each_subject
        }
        self.sub3 = {
            "subject_name":sub3,
            "total_marks":total_mark_of_each_subject
        }



class Student:
    def __init__(self, name, roll_no, semester_list, subject_wise_marks_lsit):
        self.name = name
        self.roll_no = roll_no
        self.semester_list = semester_list
        self.subject_wise_marks_list = subject_wise_marks_lsit
        self.subjects = {
            "first_semester":{
                "subject_1":{
                    "name":semester_list[0].sub1["subject_name"],
                    "total_marks":semester_list[0].sub1["total_marks"],
                    "marks_obtained":subject_wise_marks_lsit[0],
                    },
                "subject_2":{
                    "name":semester_list[0].sub2["subject_name"],
                    "total_marks":semester_list[0].sub2["total_marks"],
                    "marks_obtained":subject_wise_marks_lsit[1],
                },
                "subject_3":{
                    "name":semester_list[0].sub3["subject_name"],
                    "total_marks":semester_list[0].sub3["total_marks"],
                    "marks_obtained":subject_wise_marks_lsit[2],
                },
            },
            "second_semester":{
                "subject_1":{
                    "name":semester_list[1].sub1["subject_name"],
                    "total_marks":semester_list[1].sub1["total_marks"],
                    "marks_obtained":subject_wise_marks_lsit[3],
                },
                "subject_2":{
                    "name":semester_list[1].sub2["subject_name"],
                    "total_marks":semester_list[1].sub2["total_marks"],
                    "marks_obtained":subject_wise_marks_lsit[4],
                },
                "subject_3":{
                    "name":semester_list[1].sub3["subject_name"],
                    "total_marks":semester_list[1].sub3["total_marks"],
                    "marks_obtained":subject_wise_marks_lsit[5],
                }
            }
        }

    def add_marks(self):
        print("Marks Added")

    def calculate_percentage(self):
        total_marks_obtained = sum(self.subject_wise_marks_list)
        total_marks = (self.semester_list[0].sub1["total_marks"] * 3) + (self.semester_list[1].sub1["total_marks"] * 3)
        percentage = round((total_marks_obtained / total_marks), 2) * 100
        print(f"Percentage : {percentage}%")

    def calculate_grade(self):
        print("Grade Calculated")

    def print_report(self):
        print(f'''
Student Name: {self.name}
Roll Number: {self.roll_no}
Semesters: First Sem and Second Sem
Subjects:
First Sem: {self.semester_list[0].sub1["subject_name"], self.semester_list[0].sub2["subject_name"], self.semester_list[0].sub3["subject_name"]} | Total Marks: {self.semester_list[0].sub1["total_marks"] * 3}
Second Sem: {self.semester_list[1].sub1["subject_name"], self.semester_list[1].sub2["subject_name"], self.semester_list[1].sub3["subject_name"]} | Total Marks: {self.semester_list[1].sub1["total_marks"] * 3}
Subject Wise Marks:
{self.subjects["first_semester"]["subject_1"]["name"]}: {self.subjects["first_semester"]["subject_1"]["marks_obtained"]} / {self.subjects["first_semester"]["subject_1"]["total_marks"]}
{self.subjects["first_semester"]["subject_2"]["name"]}: {self.subjects["first_semester"]["subject_2"]["marks_obtained"]} / {self.subjects["first_semester"]["subject_2"]["total_marks"]}
{self.subjects["first_semester"]["subject_3"]["name"]}: {self.subjects["first_semester"]["subject_3"]["marks_obtained"]} / {self.subjects["first_semester"]["subject_3"]["total_marks"]}
{self.subjects["second_semester"]["subject_1"]["name"]}: {self.subjects["second_semester"]["subject_1"]["marks_obtained"]} / {self.subjects["second_semester"]["subject_1"]["total_marks"]}
{self.subjects["second_semester"]["subject_2"]["name"]}: {self.subjects["second_semester"]["subject_2"]["marks_obtained"]} / {self.subjects["second_semester"]["subject_2"]["total_marks"]}
{self.subjects["second_semester"]["subject_3"]["name"]}: {self.subjects["second_semester"]["subject_3"]["marks_obtained"]} / {self.subjects["second_semester"]["subject_3"]["total_marks"]}
''')

    def check_gpa(self):
        print("GPA Calculated")


def add_subjects():
    subjects = []
    for _ in range(3):
        sub = input("Enter Subject Name: ").title()
        subjects.append(sub)
    try:
        total_mark = int(input("Enter Total Mark: "))
        if total_mark >= 0:
            subjects.append(total_mark)
        else:
            total_mark = 0
            helper_invalid()
    except ValueError:
        helper_invalid()
    if len(subjects) == 4 and subjects[0] != subjects[1] and subjects[1] != subjects[2] and subjects[2] != subjects[0]:
        return subjects[0], subjects[1], subjects[2], subjects[3]
    else:
        return None, None, None, 0

def add_student(subject_list):
    name = input("Enter Student Name: ")
    subject_marks = []
    for subject in subject_list:
        try:
            mark = int(input(f"Enter marks obtained in {subject}\n"))
            if mark >= 0 and mark <= 100:
                subject_marks.append(mark)
            else:
                mark = None
                subject_marks.append(mark)
        except ValueError:
            helper_invalid()
    if len(subject_marks) == 6:
        return name, subject_marks
    else:
        helper_invalid()
        return None, []

def display_and_user_input():
    try:
        user_choice = int(input(f'''
1. Add Student
2. Enter Your Roll No
3. Close Application
'''))
        if user_choice == 3:
            print("Thanks for using Student Report Card")
            return False, None
        elif user_choice in [1, 2]:
            return True, user_choice
        else:
            helper_invalid()
            return True, None
    except ValueError:
        helper_invalid()
        return True, None

def after_login_user_input():
    try:
        user_choice = int(input(f'''
1. Add Marks
2. Calculate Percentage
3. Calculate Grade
4. Print Report
5. Rank Students
6. Check GPA
7. Exit
'''))
        if user_choice == 7:
            print("Successfully Logged Out.")
            return False, None
        elif user_choice in [1, 2, 3, 4, 5, 6]:
            return True, user_choice
        else:
            helper_invalid()
            return True, None
    except ValueError:
        helper_invalid()
        return True, None

def rank_students(the_whole_list):          #! The whole list operation
    print("All student list printed")

def after_login_command_mapper(single_student, all_students, the_command):
    saved_commands = {
        1: single_student.add_marks,
        2: single_student.calculate_percentage,
        3: single_student.calculate_grade,
        4: single_student.print_report,
        5: rank_students,
        6: single_student.check_gpa,
    }
    if the_command in saved_commands:
        if the_command == 5:
            saved_commands[the_command](all_students)
        else:
            saved_commands[the_command]()

def after_roll_no_login(one_student, whole_list):
    while True:
        after_login_running, user_input = after_login_user_input()
        if not after_login_running:
            break
        if user_input:
            after_login_command_mapper(one_student, whole_list, user_input)

def enter_into_student_report_card(all_students_list):
    try:
        roll = int(input("Enter Your Roll Number: "))
        for student in all_students_list:
            if student.roll_no == roll:
                print(f"Welcome {student.name}")
                after_roll_no_login(student, all_students_list)
                return
        print("Wrong Roll Number Entered.")
    except ValueError:
        helper_invalid()

def helper_invalid():
    print("Invalid Input")


def main():
    all_subjects = []
    all_students = []
    roll_number = 0
    print("Add 3 subjects and their highest mark for first semester")
    subject1, subject2, subject3, total_mark = add_subjects()
    if total_mark != 0:
        first_sem_subjects = Subjects(subject1, subject2, subject3, total_mark)
        print("Add 3 subjects and their highest mark for second semester")
        topic1, topic2, topic3, full_mark = add_subjects()
        if full_mark != 0:
            all_topics = [subject1, subject2, subject3, topic1, topic2, topic3]
            for subj in all_topics:
                all_subjects.append(subj)
            second_sem_subjects = Subjects(topic1, topic2, topic3, full_mark)
            #* Some Sample Students Added.
            roll_number += 1
            student1 = Student("Soham Datta", roll_number, [first_sem_subjects, second_sem_subjects], [76, 89, 90, 56, 59, 44])
            roll_number += 1
            student2 = Student("Amitabh Deb", roll_number, [first_sem_subjects, second_sem_subjects], [39, 99, 65, 80, 81, 73])
            all_students.append(student1)
            all_students.append(student2)
            while True:
                program_running, user_input = display_and_user_input()
                if not program_running:
                    break
                if user_input == 1:
                    name, sub_wise_marks = add_student(all_subjects)
                    if name == None or None in sub_wise_marks:
                        helper_invalid()
                    else:
                        roll_number += 1
                        print(f"Student added. Roll Number: {roll_number}")
                        added_student = Student(name, roll_number, [first_sem_subjects, second_sem_subjects], [sub_wise_marks])
                        all_students.append(added_student)
                elif user_input == 2:
                    enter_into_student_report_card(all_students)
        else:
            helper_invalid()
    else:
        helper_invalid()




main()