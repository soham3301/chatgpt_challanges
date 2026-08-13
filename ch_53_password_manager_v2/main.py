
from password_manager import PasswordManager
from user_input import Input
from output import Output

manager = PasswordManager()
user_input = Input()
output = Output()

def generate_password_flow():
    while True:
        output.password_category()
        input_category = user_input.text_input()
        if input_category == "0":
            return None
        elif input_category in ["1", "2", "3"]:
            gen_password = manager.get_generated_password(input_category)
            if gen_password:
                output.password_keeper(gen_password)
                keeping_consent = user_input.text_input()
                if keeping_consent == "0":
                    return None
                elif keeping_consent == "1":
                    return gen_password
                elif keeping_consent == "2":
                    continue
                else:
                    output.invalid_entry()
                    return None
            else:
                output.invalid_entry()
                return None
        else:
            output.invalid_entry()
            return None

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
                        output.enter_url()
                        url = user_input.text_input()
                        output.enter_username()
                        username = user_input.text_input()
                        if manager.username_validation(url, username):
                            output.generate_password()
                            gen_consent = user_input.text_input()
                            if gen_consent.lower() == "y":
                                generated_pass = generate_password_flow()
                                if generated_pass:
                                    manager.generate_credential(url, username, generated_pass)
                                    output.credentials_saved(username, generated_pass, url)
                            else:
                                output.password_rules()
                                output.enter_password()
                                password = user_input.text_input()
                                if manager.password_condition_chekcer(password):
                                    output.confirm_password()
                                    confirmed_password = user_input.text_input()
                                    if password == confirmed_password:
                                        manager.generate_credential(url, username, confirmed_password)
                                        output.credentials_saved(username, confirmed_password, url)
                                    else:
                                        output.incorrect_password()
                                else:
                                    output.password_breaks_rules()
                        else:
                            output.username_already_exist(username)
                    elif primary_input == "2":
                        output.enter_url()
                        url_updt = user_input.text_input()
                        if manager.validate_url(url_updt):
                            output.enter_username()
                            username_updt = user_input.text_input()
                            if manager.validate_username(url_updt, username_updt):
                                output.generate_password()
                                gen_pass_updt = user_input.text_input()
                                if gen_pass_updt.lower() == "y":
                                    generated_pass_updt = generate_password_flow()
                                    if generated_pass_updt:
                                        manager.update_password(url_updt, username_updt, generated_pass_updt)
                                        output.password_updated(url_updt, username_updt, generated_pass_updt)
                                else:
                                    output.password_rules()
                                    output.enter_password()
                                    password_updt = user_input.text_input()
                                    if manager.validate_password(url_updt, username_updt, password_updt):
                                        if manager.password_condition_chekcer(password_updt):
                                            output.confirm_password()
                                            confirmed_password_updt = user_input.text_input()
                                            if password_updt == confirmed_password_updt:
                                                manager.update_password(url_updt, username_updt, confirmed_password_updt)
                                                output.password_updated(url_updt, username_updt, confirmed_password_updt)
                                            else:
                                                output.incorrect_password()
                                        else:
                                            output.password_breaks_rules()
                                    else:
                                        output.current_password_error(password_updt)
                            else:
                                output.entry_not_exist(username_updt, "Username")
                        else:
                            output.entry_not_exist(url_updt, "URL")
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
                gen_password = generate_password_flow()
                if gen_password:
                    manager.save_admin_password(gen_password)
                    output.password_changed(gen_password)
            else:
                output.new_password()
                new_password = user_input.text_input()
                if manager.password_condition_chekcer(new_password):
                    output.confirm_password()
                    confirmed_new_password = user_input.text_input()
                    if new_password == confirmed_new_password:
                        manager.save_admin_password(confirmed_new_password)
                        output.password_changed(confirmed_new_password)
                    else:
                        output.incorrect_password()
                else:
                    output.password_breaks_rules()
        else:
            output.incorrect_password()
    elif login_choice == "0":
        manager_running = False
    else:
        output.invalid_entry()








