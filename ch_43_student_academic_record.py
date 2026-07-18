
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
        self.subjects = {
            "first_semester":[semester_list[0].sub1["subject_name"], semester_list[0].sub2["subject_name"], semester_list[0].sub3["subject_name"]],
            "second_semester":[semester_list[1].sub1["subject_name"], semester_list[1].sub2["subject_name"], semester_list[1].sub3["subject_name"]]
        }


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
    if len(subjects) == 4:
        return subjects[0], subjects[1], subjects[2], subjects[3]
    else:
        return None, None, None, 0

def add_student(subject_list):
    name = input("Enter Student Name: ")
    subject_marks = []
    for subject in subject_list:
        try:
            mark = input(f"Enter marks obtained in {subject}\n")
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

def enter_into_student_report_card(all_students_list):
    try:
        roll = int(input("Enter Your Roll Number: "))
        for student in all_students_list:
            if student.roll_no == roll:
                print(f"Welcome {student.name}")
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
            all_subjects.append(subject1)
            all_subjects.append(subject2)
            all_subjects.append(subject3)
            all_subjects.append(topic1)
            all_subjects.append(topic2)
            all_subjects.append(topic3)
            second_sem_subjects = Subjects(topic1, topic2, topic3, full_mark)
            #* Some Sample Students Added.
            roll_number += 1
            student1 = Student("Soham", roll_number, [first_sem_subjects, second_sem_subjects], [76, 89, 90, 56, 59, 44])
            roll_number += 1
            student2 = Student("Amitabh", roll_number, [first_sem_subjects, second_sem_subjects], [39, 99, 65, 80, 81, 73])
            all_students.append(student1)
            all_students.append(student2)
            while True:
                program_running, user_input = display_and_user_input()
                if not program_running:
                    break
                if user_input == 1:
                    roll_number += 1
                    name, sub_wise_marks = add_student(all_subjects)
                    print(f"Student added. Roll Number: {roll_number}")
                    added_student = Student(name, roll_number, [first_sem_subjects, second_sem_subjects], [sub_wise_marks])
                    all_students.append(added_student)
                elif user_input == 2:
                    enter_into_student_report_card(all_students)




main()