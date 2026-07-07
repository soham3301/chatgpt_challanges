students = {
    "Soham": 92,
    "Rahul": 81,
    "Amit": 67
}

def display_menu():
    user_input = int(input('''
1. Add Student
2. Search Student
3. Update Marks
4. Delete Student
5. Display All
6. Display by Marks
7. Exit                           
'''))
    return user_input

def getting_students_name():
    return input("Enter Student's Name: ").title()

def not_exist():
    print("This Student deosn't exist.")

def add_student():
    name = getting_students_name()
    if name in students:
        not_exist()
    else:
        marks = int(input("Enter Marks: "))
        students[name] = marks

def search_student():
    name = getting_students_name()
    if name in students:
        print(f'''
Student Found.
Name: {name}
Marks: {students[name]}
''')
    else:
        not_exist()

def update_marks():
    name = getting_students_name()
    if name in students:
        marks = int(input("Enter Marks: "))
        students[name] = marks
    else:
        not_exist()

def delete_student():
    name = getting_students_name()
    if name in students:
        students.pop(name)
    else:
        not_exist()

def display_all():
    for name in students:
        print(f'''
Name: {name}
Marks: {students[name]}
''')

def display_by_marks():
    by_marks_dict = {}
    copy_students = students.copy()
    for _ in range(len(copy_students)):
        base_mark = 0
        top_name = ""
        for name, marks in copy_students.items():
            if marks > base_mark:
                base_mark = marks
                top_name = name
        copy_students.pop(top_name)
        by_marks_dict.update({top_name: base_mark})
    for name, marks in by_marks_dict.items():
        print(f'''
Name: {name}
Marks: {marks}
''')

def mapping_user_input(user_input):
    saved_functions = {
        1: add_student,
        2: search_student,
        3: update_marks,
        4: delete_student,
        5: display_all,
        6: display_by_marks,
    }
    if user_input == 7:
        print("Thanks for using STUDENT DATABASE")
        return False
    elif user_input in saved_functions:
        saved_functions[user_input]()
        return True
    else:
        print("Invalid Input | Program Stopped")
        return False

def main():
    program_continues = True
    while program_continues:
        user_input_number = display_menu()
        program_continues = mapping_user_input(user_input_number)

main()