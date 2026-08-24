
from bank import Bank
from user_input import UserInput
from display import Display

my_bank = Bank()
user_input = UserInput()
the_display = Display()

#* Testing Ground

#* Testing Ground End

def create_account():
    the_display.enter_name()
    name = user_input.text_input()
    if name:
        the_display.enter_age()
        age = user_input.number_input()
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
                            if Bank.validate_first_deposit(first_deposit):
                                customer = my_bank.create_customer(name, age, email.lower(), mobile)
                                account = my_bank.create_account(customer.cust_id)
                                account.cash_deposit(first_deposit)
                                customer.attach_account_number(account)
                                return customer.cust_id, customer.password
                            else:
                                the_display.deposit_amount_problem()
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




bank_open = True
while bank_open:
    the_display.the_first_screen()
    first_user_input = user_input.text_input()
    if first_user_input == "0":
        the_display.thanks_exit_screen()
        bank_open = False
    elif first_user_input == "1":       #? LOGIN
        ...
    elif first_user_input == "2":       #? Create AC
        the_display.account_creation_rules()
        c_id, c_pass = create_account()
        if c_id and c_pass:
            my_bank.save_data()
            the_display.ac_open_successfull(c_id, c_pass)
        else:
            the_display.ac_open_failed()
    elif first_user_input == "manager": #? Special Privilages
        ...
    else:
        the_display.invalid_input()