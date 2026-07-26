
class Employee:
    def __init__(self, name, id, password, salary, role):
        self.name = name
        self.id = id
        self.password = password
        self.salary = salary
        self.role = role
        self.inbox = []

    def login(self, user_id, user_password):
        if user_id == self.id and user_password == self.password:
            return True
        else:
            return False

    def check_inbox(self):
        if self.inbox:
            return self.inbox
        else:
            return None

    def show_salary(self):
        return self.name, self.salary


class Manager(Employee):
    def __init__(self, name, id, password, salary, role):
        super().__init__(name, id, password, salary, role)

    def allot_work(self, employee):
        employee.inbox.append("Sample Work Given")
        return True

    def recommend_promotion(self):
        print("Promotion Recommended")

class Accountant(Employee):
    def __init__(self, name, id, password, salary, role):
        super().__init__(name, id, password, salary, role)

    def allot_budget(self):
        print("Budget Alloted")

    def print_financial_report(self):
        print("Financial Report Printed")

    def give_salary(self):
        print("Salary Disbursed")

    def increase_salary(self):
        print("Salary Increased")

class CEO(Employee):
    def __init__(self, name, id, password, salary, role):
        super().__init__(name, id, password, salary, role)

    def hire(self):
        print("You are hired")

    def fire(self):
        print("You are fired")

#* ---------------------------------------------------------------------------------------------------

class Department:
    def __init__(self, dept_name):
        self.department_name = dept_name
        self.department_manager = []
        self.department_employees = []
        self.department_budget = 0

    def view_dept_budget(self):
        return self.department_budget

    def add_dept_employees(self, employee):
        self.department_employees.append(employee)

    def add_dept_manager(self, manager):
        self.department_manager.append(manager)

    def return_dept_employees(self):
        emp_box = []
        for emp in self.department_employees:
            emp_box.append(emp)
        return emp_box

class Compnay:
    def __init__(self, company_name):
        self.company_name = company_name
        self.budget = 12000000
        self.emp_list = []
        self.dept_list = []

    def helper_employee_adding(self, employee):
        if employee:
            self.emp_list.append(employee)
            return True
        else:
            return False

    def helper_add_departments(self, dept):
        if dept:
            self.dept_list.append(dept)
            return True
        else:
            return False

    def helper_authentication(self, id, password):
        for emp in self.emp_list:
            if emp.id == id:
                if emp.login(id, password):
                    return emp
                else:
                    return False
        return False

    def show_employees(self):
        print("Employees Displayed")

all_staff_list = [
    Employee(name="Aarav", id="001", password="a001", salary=8000, role="employee"),
    Employee(name="Vivaan", id="002", password="v002", salary=8000, role="employee"),
    Employee(name="Sanvi", id="003", password="s003", salary=8000, role="employee"),
    Employee(name="Diya", id="004", password="d004", salary=8000, role="employee"),
    Employee(name="Aditya", id="005", password="a005", salary=8000, role="employee"),
    Employee(name="Arjun", id="006", password="a006", salary=8000, role="employee"),
    Employee(name="Ananya", id="007", password="a007", salary=8000, role="employee"),
    Employee(name="Meera", id="008", password="m008", salary=8000, role="employee"),
    Employee(name="Sai", id="009", password="s009", salary=8000, role="employee"),
    Manager(name="Rhea", id="010", password="r010", salary=10000, role="manager"),
    Manager(name="Krish", id="011", password="k011", salary=10000, role="manager"),
    Manager(name="Isha", id="012", password="i012", salary=10000, role="manager"),
    Accountant(name="Rudra", id="013", password="r013", salary=10000, role="accountant"),
    CEO(name="Soham", id="014", password="s014", salary=12000, role="ceo")
]

marketing = Department("Marketing")
marketing.add_dept_manager(all_staff_list[9])
for index in range(0, 3):
    marketing.add_dept_employees(all_staff_list[index])

product = Department("Product")
product.add_dept_manager(all_staff_list[10])
for index in range(3, 6):
    product.add_dept_employees(all_staff_list[index])

operation = Department("Operation")
operation.add_dept_manager(all_staff_list[11])
for index in range(6, 9):
    operation.add_dept_employees(all_staff_list[index])

all_department_list = [
    marketing,
    product,
    operation,
]

def get_id():
    return input("Enter ID: ")

def get_password():
    return input("Enter Password: ")

def display_ceo_board():
    pass

def display_accountant_board():
    pass

def display_manager_board():
    print('''
1. Show Salary
2. Allot Work
3. Recommend Promotion
4. View Departmental Budget
5. Logout''')

def display_employee_board():
    print('''
1. Show Salary
2. Check Inbox
3. Logout
''')

def user_input():
    try:
        return int(input("Choose from above: "))
    except ValueError:
        display_invalid_input()

def user_input_name():
    return input("Enter Name: ").lower()

def display_invalid_input():
    print("Invalid Input")

def helper_welcome_board(staff):
    print(f"Welcome {staff.name} | Role: {(staff.role).title()}")

def role_mapper(employee):
    saved_roles_displays = {
        "employee":display_employee_board,
        "manager":display_manager_board,
        "accountant":display_accountant_board,
        "ceo":display_ceo_board,
    }
    if employee.role in saved_roles_displays:
        saved_roles_displays[employee.role]()

def salary_print(name, salary):
    print(f"Name: {name}, Salary: {salary} /-")

def logout_print():
    print("Successfully Logged Out")

def available_employees():
    print("Available Employees")

def show_inbox(box):
    if box:
        for item in box:
            print(f"{item}")
    else:
        print("There is nothing in Inbox as of now")

def budget_viewer(amount):
    print(f"Available Budget: {amount} /-")

def employee_functions_mapper(the_staff, user_choice, depts, compnay):
    if user_choice == 1:
        the_name, the_salary = the_staff.show_salary()
        salary_print(the_name, the_salary)
    if user_choice == 2:
        inbox = the_staff.check_inbox()
        show_inbox(inbox)
    else:
        display_invalid_input()

def get_dept(staff, all_depts):
    for the_dept in all_depts:
        if the_dept.department_manager[0].id == staff.id:
            return the_dept

def manager_functions_mapper(the_staff, user_choice, depts, compnay):
    dept = get_dept(the_staff, depts)
    if user_choice == 1:
        the_name, the_salary = the_staff.show_salary()
        salary_print(the_name, the_salary)
    elif user_choice == 2:
        emp_list = dept.return_dept_employees()
        available_employees()
        for employee in emp_list:
            print(f"{(employee.name).title()}")
        name_input = user_input_name()
        for emp in emp_list:
            if emp.name.lower() == name_input:
                if the_staff.allot_work(emp):
                    print("Work Alloted")
                    return
        display_invalid_input()
    elif user_choice == 4:
        budget = dept.view_dept_budget()
        budget_viewer(budget)

def accountant_functions_mapper(the_staff, user_choice, depts, compnay):
    pass

def ceo_functions_mapper(the_staff, user_choice, depts, compnay):
    pass

def user_choice_mapper(staff, user_input, all_depts, brand):
    mapper_functions = {
        "employee":employee_functions_mapper,
        "manager":manager_functions_mapper,
        "accountant":accountant_functions_mapper,
        "ceo":ceo_functions_mapper,
    }
    if staff.role in mapper_functions:
        mapper_functions[staff.role](staff, user_input, all_depts, brand)

def exit_check(staff, command):
    if staff.role == "employee" and command == 3:
        logout_print()
        return True
    elif staff.role == "manager" and command == 5:
        logout_print()
        return True


def main():
    rebelcode = Compnay("Rebelcode")
    for emp in all_staff_list:
        rebelcode.helper_employee_adding(emp)
    for dept in all_department_list:
        rebelcode.helper_add_departments(dept)
    program_running = True
    while program_running:
        id = get_id()
        password = get_password()
        the_staff = rebelcode.helper_authentication(id=id, password=password)
        if the_staff:
            helper_welcome_board(the_staff)
            while True:
                role_mapper(the_staff)
                user_choice = user_input()
                if exit_check(the_staff, user_choice):
                    break
                else:
                    user_choice_mapper(the_staff, user_choice, all_department_list, rebelcode)
        else:
            display_invalid_input()
            program_running = False

main()
