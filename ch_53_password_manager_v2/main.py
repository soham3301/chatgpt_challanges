
from password_manager import PasswordManager
from user_input import Input
from output import Output

manager = PasswordManager()
user_input = Input()
output = Output()

manager_running = True
while manager_running:
    output.login()
    login_choice = user_input.text_input()
    if login_choice == "1":
        output.enter_password()
        input_password = user_input.text_input()
        if manager.validate_admin_password(input_password):
            login_successful = True
            while login_successful:
                output.primary_display()
                primary_input = user_input.text_input()
                if primary_input == "0":
                    login_successful = False
                elif primary_input in ["1", "2", "3", "4"]:
                    if primary_input == "1":
                        # output.enter_url()
                        # url = user_input.text_input()
                        # output.enter_username()
                        # username = user_input.text_input()
                        print("Save Password Section")
                    elif primary_input == "2":
                        print("Update Password Section")
                    elif primary_input == "3":
                        print("Search Password Section")
                    elif primary_input == "4":
                        print("Delete Password Section")
                    else:
                        output.invalid_entry()
                else:
                    output.invalid_entry()
        else:
            output.incorrect_password()
    elif login_choice == "2":
        output.password_rules()
        output.previous_password()
        old_password = user_input.text_input()
        if manager.validate_admin_password(old_password):
            output.generate_password()
            generate_consent = user_input.text_input()
            if generate_consent.lower() == "y":
                output.password_category()
                input_category = user_input.text_input()
                if input_category in ["1", "2", "3"]:
                    gen_password = manager.get_generated_password(input_category)
                    manager.save_admin_password(gen_password)
                    output.password_changed(gen_password)
                else:
                    output.invalid_entry()
            else:
                output.new_password()
                new_password = user_input.text_input()
                if manager.condition_chekcer(new_password):
                    output.confirm_password()
                    confirmed_new_password = user_input.text_input()
                    if new_password == confirmed_new_password:
                        manager.save_admin_password(confirmed_new_password)
                        output.password_changed(confirmed_new_password)
                    else:
                        output.incorrect_password()
                else:
                    output.short_password()
        else:
            output.incorrect_password()
    elif login_choice == "0":
        manager_running = False
    else:
        output.invalid_entry()





