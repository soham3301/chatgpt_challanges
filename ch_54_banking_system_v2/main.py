
from bank import Bank
from user_input import UserInput
from display import Display

my_bank = Bank()
user_input = UserInput()
the_display = Display()

#* Testing Ground


#* Testing Ground End

def create_account_flow():
    the_display.enter_name()
    name = user_input.text_input()
    if name:
        the_display.enter_age()
        age = user_input.number_input()
        if age:
            if Bank.validate_age(age):
                the_display.enter_email()
                email = user_input.text_input()
                if not my_bank.is_data_exist(email.lower()):
                    if Bank.validate_email(email.lower()):
                        the_display.enter_mobile_number()
                        mobile = user_input.number_input()
                        if not my_bank.is_data_exist(mobile):
                            if Bank.validate_mobile(mobile):
                                the_display.enter_first_deposit()
                                first_deposit = user_input.number_input()
                                if first_deposit:
                                    if Bank.validate_first_deposit(first_deposit):
                                        the_display.comfirm_amount(first_deposit, "deposit")
                                        first_dep_confirmation = user_input.text_input().lower()
                                        if first_dep_confirmation == "y":
                                            customer = my_bank.create_customer(name, age, email.lower(), mobile)
                                            account = my_bank.create_account(customer.cust_id)
                                            account.cash_deposit(first_deposit)
                                            customer.attach_account_number(account)
                                            return customer.cust_id, customer.password
                                        else:
                                            the_display.transaction_cancelled()
                                            return None, None
                                    else:
                                        the_display.deposit_amount_problem()
                                        return None, None
                                else:
                                    the_display.invalid_input()
                                    return None, None
                            else:
                                the_display.mobile_format_problem()
                                return None, None
                        else:
                            the_display.mobile_already_exist(mobile)
                            return None, None
                    else:
                        the_display.email_format_problem()
                        return None, None
                else:
                    the_display.email_already_exist(email.lower())
                    return None, None
            else:
                the_display.age_problem()
                return None, None
        else:
            the_display.invalid_input()
            return None, None
    else:
        the_display.invalid_input()
        return None, None


def login_flow():
    the_display.enter_customer_id()
    cust_id = user_input.text_input()
    if my_bank.validate_customer_id(cust_id):
        if not my_bank.is_account_locked(cust_id):
            login_chance = 3
            while True:
                the_display.enter_password(login_chance)
                the_password = user_input.text_input()
                if my_bank.customers[cust_id].check_login(cust_id, the_password):
                    customer = my_bank.get_customer(cust_id)
                    account = my_bank.get_account(customer.account_number)
                    return customer, account
                else:
                    the_display.incorrect_password()
                    login_chance -= 1
                if login_chance == 0:
                    my_bank.lock_account(cust_id)
                    the_display.account_locked()
                    my_bank.save_data()
                    return None, None
        else:
            the_display.account_locked()
            return None, None
    else:
        the_display.id_not_exist()
        return None, None

def command_deposit(ac):
    the_display.enter_amount()
    amount = user_input.number_input()
    if amount:
        the_display.comfirm_amount(amount, "deposit")
        dep_confirmation = user_input.text_input().lower()
        if dep_confirmation == "y":
            if ac.cash_deposit(amount):
                the_display.deposit_successfull(amount)
                my_bank.save_data()
            else:
                the_display.deposit_unsuccessfull()
        else:
            the_display.transaction_cancelled()
    else:
        the_display.invalid_input()

def command_check_balance(ac):
    balance = ac.check_balance()
    the_display.show_balance(balance)

def command_mapper(the_user_input, customer, account):
    saved_commands = {
        "1": command_deposit,
        "2": ...,
        "3": ...,
        "4": command_check_balance,
        "5": ...,
        "6": ...,
        "7": ...,
        "8": ...,
        "9": ...
    }
    if the_user_input in ["1", "2", "3", "4", "5", "7"]:
        saved_commands[the_user_input](account)
    else:
        saved_commands[the_user_input](customer)


bank_open = True
while bank_open:
    the_display.the_first_screen()
    first_user_input = user_input.text_input()
    if first_user_input == "0":
        the_display.thanks_exit_screen()
        bank_open = False
    elif first_user_input == "1":       #? The Login
        the_customer, the_account = login_flow()
        if the_customer and the_account:
            the_display.welcome_screen(the_customer.name, the_account.number)
            while True:                 #? After Logged In
                the_display.after_login_activity_screen()
                second_user_input = user_input.text_input()
                if second_user_input == "0":
                    my_bank.save_data()
                    the_display.logged_out()
                    break
                elif second_user_input in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    command_mapper(second_user_input, the_customer, the_account)
                else:
                    the_display.invalid_input()
        else:
            the_display.login_failed()
    elif first_user_input == "2":       #? Create AC
        the_display.account_creation_rules()
        c_id, c_pass = create_account_flow()
        if c_id and c_pass:
            my_bank.save_data()
            the_display.ac_open_successfull(c_id, c_pass)
        else:
            the_display.ac_open_failed()
    elif first_user_input == "manager": #? Special Privilages
        ...
    else:
        the_display.invalid_input()