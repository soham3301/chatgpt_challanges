
from bank import Bank
from user_input import UserInput
from display import Display

my_bank = Bank()
user_input = UserInput()
the_display = Display()

#* Testing Ground
# my_bank.save_data()
# print(my_bank.manager.approved_loans)
#! Task - Repay Loan --- point 11

#* Testing Ground End

#* ======================== USER ACCOUNT CREATION ========================

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

#* ======================== USER LOGIN ========================

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

#* ======================== USERS AREA ========================

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
                the_display.transaction_unsuccessfull("deposit")
        else:
            the_display.transaction_cancelled()
    else:
        the_display.invalid_input()

def command_withdraw(ac):
    the_display.enter_amount()
    amount = user_input.number_input()
    if amount:
        if ac.is_balance_sufficient(amount):
            the_display.comfirm_amount(amount, "withdraw")
            wit_confirmation = user_input.text_input().lower()
            if wit_confirmation == "y":
                if ac.cash_withdraw(amount):
                    the_display.withdraw_successfull(amount)
                    my_bank.save_data()
                else:
                    the_display.transaction_unsuccessfull("withdraw")
            else:
                the_display.transaction_cancelled()
        else:
            the_display.insufficient_balance()
    else:
        the_display.invalid_input()

def command_transfer(ac):
    the_display.enter_amount()
    amount = user_input.number_input()
    if amount:
        if ac.is_balance_sufficient(amount):
            the_display.comfirm_amount(amount, "transfer")
            tran_confirmation = user_input.text_input().lower()
            if tran_confirmation == "y":
                the_display.enter_recepients_account_number()
                ac_no = user_input.number_input()
                if ac_no:
                    to_account = my_bank.get_account(ac_no)
                    if to_account:
                        transaction_object = ac.send_amount(amount, to_account.number)
                        if transaction_object:
                            if to_account.receive_amount(amount, transaction_object):
                                the_display.transaction_successfull(amount, to_account.number)
                                my_bank.save_data()
                            else:
                                the_display.transaction_unsuccessfull("transfer")
                        else:
                            the_display.transaction_unsuccessfull("transfer")
                    else:
                        the_display.account_not_exist(ac_no)
                else:
                    the_display.invalid_input()
            else:
                the_display.transaction_cancelled()
        else:
            the_display.insufficient_balance()
    else:
        the_display.invalid_input()

def command_check_balance(ac):
    balance = ac.check_balance()
    the_display.show_balance(balance)

def command_tran_history(ac):
    the_history, last_bal = ac.check_transaction_history()
    the_display.show_transactions()
    for each_transaction in the_history:
        if each_transaction["type"] == "deposit":
            the_display.tran_show_deposits(each_transaction["amount"], each_transaction["balance"], each_transaction["tran_id"])
        elif each_transaction["type"] == "withdraw":
            the_display.tran_show_withdraws(each_transaction["amount"], each_transaction["balance"], each_transaction["tran_id"])
        elif each_transaction["type"] == "transfer" and each_transaction["from_account"] == ac.number:
            the_display.tran_show_sent(each_transaction["amount"], each_transaction["balance"], each_transaction["tran_id"], each_transaction["to_account"])
        elif each_transaction["type"] == "transfer" and each_transaction["to_account"] == ac.number:
            the_display.tran_show_received(each_transaction["amount"], each_transaction["balance"], each_transaction["tran_id"], each_transaction["from_account"])
    the_display.show_final_balance(last_bal)

def command_change_pass(cust):
    the_display.enter_old_password()
    old_pass = user_input.text_input()
    if old_pass:
        if cust.validate_password(old_pass):
            the_display.enter_new_password()
            new_pass = user_input.text_input()
            if new_pass:
                the_display.confirm_password()
                new_pass_again = user_input.text_input()
                if new_pass_again:
                    if new_pass == new_pass_again:
                        cust.change_password(new_pass_again)
                        the_display.pass_changed()
                        my_bank.save_data()
                    else:
                        the_display.password_doesnot_match()
                else:
                    the_display.invalid_input()
            else:
                the_display.invalid_input()
        else:
            the_display.incorrect_password()
    else:
        the_display.invalid_input()

def command_show_account_details(ac):
    ac_data = ac.send_account_information()
    the_display.show_ac_info(ac_data["number"], ac_data["balance"], ac_data["interest_gained"], ac_data["customer_id"], ac_data["total_transactions"])

def command_show_customer_details(cust):
    cust_data = cust.check_customer_details()
    the_display.show_customer_info(cust_data["name"], cust_data["age"], cust_data["email"], cust_data["mobile"], cust_data["account_number"], cust_data["loan_account_number"], cust_data["customer_id"], cust_data["password"])

def command_apply_for_loan(cust, ac):
    if not my_bank.manager.is_already_applied(cust.cust_id):
        the_display.loan_application_started()
        the_display.how_much_loan_you_need()
        requested_loan_amount = user_input.number_input()
        if requested_loan_amount:
            the_display.monthly_income()
            entered_monthly_income = user_input.number_input()
            if entered_monthly_income:
                possible_loans = my_bank.manager.get_possible_loan_data(cust.cust_id, requested_loan_amount, entered_monthly_income, ac.balance)
                if len(possible_loans) == 0:
                    the_display.not_eligible_for_loan()
                else:
                    loan_numbers = []
                    for loan_serial, loan_item in possible_loans.items():
                        loan_numbers.append(loan_serial)
                        the_display.show_possible_loans(loan_serial, loan_item["loan_amount"], loan_item["repayment_amount"], loan_item["tanure_in_months"], loan_item["yearly_interest"], loan_item["monthly_emi"])
                    the_display.choose_the_loan_number()
                    loan_number = user_input.number_input()
                    if loan_number:
                        if loan_number in loan_numbers:
                            final_loan_data = possible_loans[loan_number]
                            the_display.apply_loan_confirmation(final_loan_data["loan_amount"], final_loan_data["repayment_amount"], final_loan_data["tanure_in_months"], final_loan_data["yearly_interest"], final_loan_data["monthly_emi"])
                            loan_confirmation = user_input.text_input().lower()
                            if loan_confirmation == "y":
                                my_bank.manager.receive_loan_application(final_loan_data, cust.cust_id)
                                the_display.loan_applied_successfully()
                                my_bank.save_data()
                            else:
                                the_display.loan_application_cancelled()
                        else:
                            the_display.loan_application_cancelled()
                    else:
                        the_display.invalid_input()
            else:
                the_display.invalid_input()
        else:
            the_display.invalid_input()
    else:
        the_display.already_applied()

def command_show_loan_status(cust):
    if cust.loan_account_number:
        loan = my_bank.get_loan(cust.loan_account_number)
        loan_status = cust.prepare_loan_data(loan)
        the_display.show_loan_status(loan_status)
    else:
        the_display.no_loan_available()

def command_repay_loan(cust, ac):
    print("Loan Repayment Section")

def command_mapper(the_user_input, customer, account):
    saved_commands = {
        "1": command_deposit,
        "2": command_withdraw,
        "3": command_transfer,
        "4": command_check_balance,
        "5": command_tran_history,
        "6": command_change_pass,
        "7": command_show_account_details,
        "8": command_show_customer_details,
        "9": command_apply_for_loan,
        "10": command_show_loan_status,
        "11": command_repay_loan,
    }
    if the_user_input in ["1", "2", "3", "4", "5", "7"]:
        saved_commands[the_user_input](account)
    elif the_user_input in ["6", "8", "10"]:
        saved_commands[the_user_input](customer)
    else:
        saved_commands[the_user_input](customer, account)

#* ======================== MANAGERS AREA ========================

def manager_unlock_account():
    locked_list = my_bank.manager.get_locked_account_numbers()
    if locked_list:
        for ac_no in locked_list:
            the_display.show_locked_accounts(ac_no)
        the_display.enter_account_number()
        account_number_for_unlock = user_input.number_input()
        if account_number_for_unlock:
            if account_number_for_unlock in locked_list:
                account_for_unlock = my_bank.get_account(account_number_for_unlock)
                my_bank.manager.unlock_account(account_for_unlock)
                the_display.account_unlocked(account_for_unlock.number)
                my_bank.save_data()
            else:
                the_display.invalid_input()
        else:
            the_display.invalid_input()
    else:
        the_display.nothing_to_unlock()

def manager_check_loan_applications():
    applications_dict = my_bank.manager.show_loan_applications()
    if applications_dict:
        the_display.pending_applications_screen()
        for cust_id, loan_details in applications_dict.items():
            the_display.view_pending_loan_applications(cust_id, loan_details["loan_amount"], loan_details["monthly_emi"], loan_details["repayment_amount"])
    else:
        the_display.no_pending_loan_application()

def manager_approve_loan():
    the_display.enter_customer_id()
    entered_cust_id = user_input.text_input()
    if entered_cust_id:
        if my_bank.manager.is_this_customer_applied(entered_cust_id):
            the_loan_application = my_bank.manager.show_loan_applications()[entered_cust_id]
            loan_customer = my_bank.get_customer(entered_cust_id)
            loan_cust_account = my_bank.get_account(loan_customer.account_number)
            loan_customer_details = loan_customer.send_customer_info_for_manager()
            loan_cust_account_details = loan_cust_account.send_account_information()
            the_display.varify_loan_display(loan_customer_details["name"], loan_customer_details["age"], the_loan_application["loan_amount"], the_loan_application["repayment_amount"], the_loan_application["tanure_in_months"], the_loan_application["monthly_emi"], loan_cust_account_details["number"], loan_cust_account_details["balance"], loan_cust_account_details["total_transactions"], the_loan_application["monthly_income"])
            the_display.loan_approval_confirmation(loan_customer_details["name"], the_loan_application["loan_amount"])
            loan_confirmation_consent = user_input.text_input().lower()
            if loan_confirmation_consent == "y":
                loan_ac_no = my_bank.manager.approve_loan(the_loan_application, loan_customer, loan_cust_account)
                the_display.loan_approved(loan_ac_no)
                my_bank.save_data()
            else:
                the_display.loan_processing_cancelled(loan_customer_details["name"])
        else:
            the_display.id_not_exist()
    else:
        the_display.invalid_input()

def manager_mapper(m_choice):
    saved_managers_commands = {
        "1": manager_unlock_account,
        "2": manager_check_loan_applications,
        "3": manager_approve_loan,
        "4": ...,
        "5": ...,
        "6": ...,
        "7": ...,
        "8": ...,
        "9": ...,
    }
    saved_managers_commands[m_choice]()

#* ======================== THE MAIN LOOP ========================

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
                elif second_user_input in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]:
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
        the_display.enter_managers_password()
        m_password = user_input.text_input()
        if m_password:
            if my_bank.manager.validate_login(m_password):
                while True:
                    the_display.managers_screen()
                    managers_choice = user_input.text_input()
                    if managers_choice == "0":
                        the_display.logged_out()
                        break
                    elif managers_choice in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                        manager_mapper(managers_choice)
                    else:
                        the_display.invalid_input()
            else:
                the_display.incorrect_password()
        else:
            the_display.invalid_input()
    else:
        the_display.invalid_input()