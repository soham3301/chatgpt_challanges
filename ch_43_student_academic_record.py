
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

    def helper_grade_calc(self, sem_name):
        grade_wise_list = []
        for sub, details in self.subjects[sem_name].items():
                if details["marks_obtained"] >= 90:
                    grade_wise_list.append({
                        "sub_name":details["name"],
                        "sub_grade":"A+"
                    })
                elif details["marks_obtained"] >= 80:
                    grade_wise_list.append({
                        "sub_name":details["name"],
                        "sub_grade":"A"
                    })
                elif details["marks_obtained"] >= 60:
                    grade_wise_list.append({
                        "sub_name":details["name"],
                        "sub_grade":"B"
                    })
                elif details["marks_obtained"] >= 33:
                    grade_wise_list.append({
                        "sub_name":details["name"],
                        "sub_grade":"C"
                    })
                else:
                    grade_wise_list.append({
                        "sub_name":details["name"],
                        "sub_grade":"F"
                    })
        return grade_wise_list

    def helper_marks_calc(self):
        total_marks_obtained_list = []
        for semester in self.subjects.values():
            for subject in semester.values():
                total_marks_obtained_list.append(subject["marks_obtained"])
        total_marks_obtained = sum(total_marks_obtained_list)
        total_marks = (self.semester_list[0].sub1["total_marks"] * 3) + (self.semester_list[1].sub1["total_marks"] * 3)
        percentage = round((total_marks_obtained / total_marks), 2) * 100
        return total_marks_obtained, total_marks, percentage

    def helper_add_mark(self):
        all_subject_names = []
        enter_subject_name = input("Enter Subject Name: ").title()
        for sem in self.semester_list:
            all_subject_names.append(sem.sub1["subject_name"])
            all_subject_names.append(sem.sub2["subject_name"])
            all_subject_names.append(sem.sub3["subject_name"])
        if enter_subject_name in all_subject_names:
            try:
                enter_marks = int(input("Enter Marks: "))
                if enter_marks > 0 and enter_marks <= 100:
                    previous_mark = 0
                    for key, value in self.subjects["first_semester"].items():
                        if value["name"] == enter_subject_name:
                            previous_mark += value["marks_obtained"]
                    for key, value in self.subjects["second_semester"].items():
                        if value["name"] == enter_subject_name:
                            previous_mark += value["marks_obtained"]
                    if previous_mark + enter_marks > 100:
                        return None, None
                    else:
                        return enter_subject_name, enter_marks
                else:
                    print("This mark is not accaptable")
                    return None, None
            except ValueError:
                helper_invalid()
                return None, None
        else:
            print("This subject is not in your course.")
            return None, None

    def add_marks(self):
        sub_name, mark_for_addition = self.helper_add_mark()
        if sub_name != None:
            for key, value in self.subjects["first_semester"].items():
                if value["name"] == sub_name:
                    value["marks_obtained"] += mark_for_addition
            for key, value in self.subjects["second_semester"].items():
                if value["name"] == sub_name:
                    value["marks_obtained"] += mark_for_addition
            print("Marks Added")

    def calculate_percentage(self):
        total_m_obtained, total_m, percentage = self.helper_marks_calc()
        print(f"Percentage : {percentage}%")

    def calculate_grade(self):
        first_sem_grade_list = self.helper_grade_calc("first_semester")
        second_sem_grade_list = self.helper_grade_calc("second_semester")
        print(f"Here is the Grade List of {self.name}")
        for result in first_sem_grade_list:
            print(f"{result["sub_name"]}: {result["sub_grade"]}")
        for result in second_sem_grade_list:
            print(f"{result["sub_name"]}: {result["sub_grade"]}")

    def print_report(self):
        total_m_obtained, total_m, percentage = self.helper_marks_calc()
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
Total: {total_m_obtained} / {total_m}
Percentage: {percentage}
''')

    def check_gpa(self):
        #!NOTE: I don't know how to calculate GPA, Leaving it as of now.
        print("GPA Unavailable as of now")

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

def rank_students(the_whole_list):
    students_with_their_percentage = []
    for student in the_whole_list:
        obtained, total, percentage = student.helper_marks_calc()
        name = student.name
        students_with_their_percentage.append({
            "name":name,
            "percentage":percentage
        })
    n = len(students_with_their_percentage)
    for i in range(n):
        for j in range(0, n - i - 1):
            current_student_pct = students_with_their_percentage[j]['percentage']
            next_student_pct = students_with_their_percentage[j + 1]['percentage']
            if current_student_pct < next_student_pct:
                students_with_their_percentage[j], students_with_their_percentage[j + 1] = students_with_their_percentage[j + 1], students_with_their_percentage[j]
    for student in students_with_their_percentage:
        print(f"Name: {student["name"]} | Percentage: {student["percentage"]}")

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
                        added_student = Student(name, roll_number, [first_sem_subjects, second_sem_subjects], sub_wise_marks)
                        all_students.append(added_student)
                elif user_input == 2:
                    enter_into_student_report_card(all_students)
        else:
            helper_invalid()
    else:
        helper_invalid()

main()