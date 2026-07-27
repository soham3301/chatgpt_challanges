
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

    def recommend_promotion(self, the_company, employee):
        for the_ceo in the_company.emp_list:
            if the_ceo.role == "ceo":
                if employee:
                    the_ceo.inbox.append({
                        "For Promotion":employee,
                    })
                    return True
                else:
                    return False

class Accountant(Employee):
    def __init__(self, name, id, password, salary, role):
        super().__init__(name, id, password, salary, role)

    def allot_budget_to_depts(self, the_dept, the_company, budget_to_allocate):
        if the_dept and the_company and budget_to_allocate:
            the_dept.department_budget += budget_to_allocate
            the_company.budget -= budget_to_allocate
            return True
        else:
            return False

    def print_financial_report(self, the_company):
        available_budget = the_company.budget
        budget_inside_departments = {}
        for dept in the_company.dept_list:
            budget_inside_departments.update({
                dept.department_name:dept.department_budget,
            })
        upcoming_salary = 0
        for emp in the_company.emp_list:
            upcoming_salary += emp.salary
        return [available_budget, budget_inside_departments, upcoming_salary]


    def give_salary(self, employee_list, the_company):
        available_budget = the_company.budget
        total_salary_amount = 0
        for emp in employee_list:
            total_salary_amount += emp.salary
        if available_budget >= total_salary_amount:
            for empl in employee_list:
                the_company.budget -= empl.salary
            return True
        else:
            return False

    def increase_salary(self, the_employee, new_salary):
        if the_employee and new_salary:
            the_employee.salary += new_salary
            return True
        else:
            return False

class CEO(Employee):
    def __init__(self, name, id, password, salary, role):
        super().__init__(name, id, password, salary, role)

    #* Show Salary
    #* Check Inbox

    def id_pass_generator(self, name, company):
        counter = 0
        for emp in company.emp_list:
            counter = emp.id
        final_id = counter + 1
        final_password = name[0] + str(final_id)
        print(f"ID: {final_id} | Password: {final_password}")
        return final_id, final_password

    def helper_check_dept_emp(self, name, depts):
        for dept in depts:
            for emp in dept.department_employees:
                if emp.name == name:
                    if len(dept.department_employees) > 1:
                        dept.department_employees.remove(emp)
                        return True
                    else:
                        return False

    def helper_check_dept_mang(self, name, depts):
        for dept in depts:
            for man in dept.department_manager:
                if man.name == name:
                    if len(dept.department_manager) > 1:
                        dept.department_manager.remove(man)
                        return True
                    else:
                        return False

    def hire_employee(self, new_name, the_company):
        the_name = new_name.title()
        the_id, the_password = self.id_pass_generator(new_name, the_company)
        the_salary = 8000
        the_role = "employee"
        print(len(the_company.emp_list))
        the_company.emp_list.append(Employee(the_name, the_id, the_password, the_salary, the_role))
        print(len(the_company.emp_list))
        return True

    def fire_employee(self, fire_name, the_compnay, all_depts):
        the_name = fire_name.title()
        if self.helper_check_dept_emp(the_name, all_depts):
            for emp in the_compnay.emp_list:
                if emp.name == the_name:
                    the_compnay.emp_list.remove(emp)
                    return True
            return False
        else:
            return False

    def hire_manager(self, new_name, the_company):
        the_name = new_name.title()
        the_id, the_password = self.id_pass_generator(new_name, the_company)
        the_salary = 10000
        the_role = "manager"
        print(len(the_company.emp_list))
        the_company.emp_list.append(Manager(the_name, the_id, the_password, the_salary, the_role))
        print(len(the_company.emp_list))
        return True

    def fire_manager(self, fire_name, the_company, all_depts):
        the_name = fire_name.title()
        if self.helper_check_dept_mang(the_name, all_depts):
            for emp in the_company.emp_list:
                if emp.name == the_name:
                    the_company.emp_list.remove(emp)
                    return True
            return False
        else:
            return False

    def give_promotion(self):
        print("You are promoted")

    def add_new_department(self):
        print("New Department Added")

    def attach_employee_to_a_department(self):
        print("Employee Attached")

    def deattach_employee_from_a_department(self):
        print("Employee De-attached")

    def attach_manager_to_a_department(self):
        print("Manager Attached")

    def deattach_manager_from_a_department(self):
        print("Manager De-attached")

    def allot_work_to_anyone(self):
        print("Work Alloted")

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

#* ---------------------------------------------------------------------------------------------------

all_staff_list = [
    Employee(name="Aarav", id=1, password="a1", salary=8000, role="employee"),
    Employee(name="Vivaan", id=2, password="v2", salary=8000, role="employee"),
    Employee(name="Sanvi", id=3, password="s3", salary=8000, role="employee"),
    Employee(name="Diya", id=4, password="d4", salary=8000, role="employee"),
    Employee(name="Aditya", id=5, password="a5", salary=8000, role="employee"),
    Employee(name="Arjun", id=6, password="a6", salary=8000, role="employee"),
    Employee(name="Ananya", id=7, password="a7", salary=8000, role="employee"),
    Employee(name="Meera", id=8, password="m8", salary=8000, role="employee"),
    Employee(name="Sai", id=9, password="s9", salary=8000, role="employee"),
    Manager(name="Rhea", id=10, password="r10", salary=10000, role="manager"),
    Manager(name="Krish", id=11, password="k11", salary=10000, role="manager"),
    Manager(name="Isha", id=12, password="i12", salary=10000, role="manager"),
    Accountant(name="Rudra", id=13, password="r13", salary=10000, role="accountant"),
    CEO(name="Soham", id=14, password="s14", salary=12000, role="ceo")
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

#? ------------------------MAJOR DISPLAYS------------------------

def display_ceo_board():
    print('''
1. Show Salary
2. Check Inbox
3. Hire Employee
4. Fire Employee
5. Hire Manager
6. Fire Manager
7. Give Promotion
8. Add New Department
9. Attach Employee to a Department
10. De-attach Employee from a Department
11. Attach Manager to a Department
12. De-attach Manager from a Department
13. Allot Work to Anyone
14. Logout
''')

def display_accountant_board():
    print('''
1. Show Salary
2. Check Inbox
3. Allot Budget to Departments
4. Give Salary
5. Increase Salary
6. Print Financial Report
7. Logout
''')

def display_manager_board():
    print('''
1. Show Salary
2. Check Inbox
3. Allot Work
4. Recommend Promotion
5. View Departmental Budget
6. Logout''')

def display_employee_board():
    print('''
1. Show Salary
2. Check Inbox
3. Logout
''')


#? ------------------------HELPERS------------------------

def get_id():
    try:
        the_id = abs(round(int(input("Enter ID: "))))
        return the_id
    except ValueError:
        display_invalid_input()
        return None

def get_password():
    return input("Enter Password: ")

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

def display_everyone_with_salary(total_list):
    for employee in total_list:
        print(f"Name: {employee.name} | Salary: {employee.salary}")

def salary_print(name, salary):
    print(f"Name: {name}, Salary: {salary} /-")

def logout_print():
    print("Successfully Logged Out")

def available_employees():
    print("Available Employees")

def display_financial_report(data):
    print(f"Available Budget to spend: {data[0]}/-")
    print(f"Amount for upcoming Salary: {data[2]}/-")
    print("Budget Allocated to Departments:")
    for key, value in data[1].items():
        print(f"{key}: {value}/-")

def print_available_depts(dept_list):
    for dept in dept_list:
        print(f"{(dept.department_name).title()}")

def choose_amount(budget):
    try:
        enter_amount = abs(round(int(input("Enter Amount: "))))
        if enter_amount < budget:
            return enter_amount
    except ValueError:
        display_invalid_input()
        return None

def show_inbox(box):
    if box:
        for item in box:
            print(f"{item}")
    else:
        print("There is nothing in Inbox as of now")

def budget_viewer(amount):
    print(f"Available Budget: {amount} /-")

def get_dept(staff, all_depts):
    for the_dept in all_depts:
        if the_dept.department_manager[0].id == staff.id:
            return the_dept

def display_all_employees(the_compnay):
    for emp in the_compnay.emp_list:
        print(f"Name: {emp.name} | Role: {emp.role}")


#? ------------------------MAPPERS------------------------

def role_mapper(employee):
    saved_roles_displays = {
        "employee":display_employee_board,
        "manager":display_manager_board,
        "accountant":display_accountant_board,
        "ceo":display_ceo_board,
    }
    if employee.role in saved_roles_displays:
        saved_roles_displays[employee.role]()

def employee_functions_mapper(the_staff, user_choice, depts, compnay):
    if user_choice == 1:
        the_name, the_salary = the_staff.show_salary()
        salary_print(the_name, the_salary)
    elif user_choice == 2:
        inbox = the_staff.check_inbox()
        show_inbox(inbox)
    else:
        display_invalid_input()

def manager_functions_mapper(the_staff, user_choice, depts, compnay):
    dept = get_dept(the_staff, depts)
    emp_list = dept.return_dept_employees()
    if user_choice == 1:
        the_name, the_salary = the_staff.show_salary()
        salary_print(the_name, the_salary)
    elif user_choice == 2:
        inbox = the_staff.check_inbox()
        show_inbox(inbox)
    elif user_choice == 3:
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
        available_employees()
        for employee in emp_list:
            print(f"{(employee.name).title()}")
        input_name = user_input_name()
        for empl in emp_list:
            if empl.name.lower() == input_name:
                if the_staff.recommend_promotion(compnay, empl):
                    print("Recommended for Promotion")
                    return
    elif user_choice == 5:
        budget = dept.view_dept_budget()
        budget_viewer(budget)
    else:
        display_invalid_input()

def accountant_functions_mapper(the_staff, user_choice, depts, compnay):
    emp_list = compnay.emp_list
    if user_choice == 1:
        the_name, the_salary = the_staff.show_salary()
        salary_print(the_name, the_salary)
    elif user_choice == 2:
        inbox = the_staff.check_inbox()
        show_inbox(inbox)
    elif user_choice == 3:
        print_available_depts(depts)
        print(f"Available Budget: {compnay.budget} /-")
        dept_name = user_input_name()
        amount = choose_amount(compnay.budget)
        if amount:
            for dept in depts:
                if dept.department_name == dept_name.title():
                    if the_staff.allot_budget_to_depts(dept, compnay, amount):
                        print(f"Budget Allocated to {(dept_name).title()}")
                    else:
                        print("Budget Allocation Failed.")
        else:
            print("Budget Restriction")
    elif user_choice == 4:
        if the_staff.give_salary(emp_list, compnay):
            print("Salary Given")
        else:
            print("Not Enough Budget")
    elif user_choice == 5:
        available_employees()
        display_everyone_with_salary(emp_list)
        staff_name = user_input_name()
        for emp in emp_list:
            if emp.name == staff_name.title():
                new_amount = choose_amount(compnay.budget)
                if new_amount:
                    if the_staff.increase_salary(emp, new_amount):
                        print("Salary Increased")
                        return
                    else:
                        display_invalid_input()
                else:
                    display_invalid_input()
    elif user_choice == 6:
        the_report_data = the_staff.print_financial_report(compnay)
        display_financial_report(the_report_data)
    else:
        display_invalid_input()


def ceo_functions_mapper(the_staff, user_choice, depts, compnay):
    if user_choice == 1:
        the_name, the_salary = the_staff.show_salary()
        salary_print(the_name, the_salary)
    elif user_choice == 2:
        inbox = the_staff.check_inbox()
        show_inbox(inbox)
    elif user_choice == 3:
        new_emp_name = user_input_name()
        if new_emp_name:
            if the_staff.hire_employee(new_emp_name, compnay):
                print("Employee Joined Company")
        else:
            display_invalid_input()
    elif user_choice == 4:
        display_all_employees(compnay)
        choosen_name = user_input_name()
        if the_staff.fire_employee(choosen_name, compnay, depts):
            print("Employee Removed")
        else:
            print("Employee Not Removed")
    elif user_choice == 5:
        new_manager_name = user_input_name()
        if new_manager_name:
            if the_staff.hire_manager(new_manager_name, compnay):
                print("Manager Joined Company")
        else:
            display_invalid_input()
    elif user_choice == 6:
        display_all_employees(compnay)
        choosen_manager = user_input_name()
        if the_staff.fire_manager(choosen_manager, compnay, depts):
            print("Manager Removed")
        else:
            print("Manager Not Removed")

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
    elif staff.role == "manager" and command == 6:
        logout_print()
        return True
    elif staff.role == "accountant" and command == 7:
        logout_print()
        return True
    elif staff.role == "ceo" and command == 14:
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
