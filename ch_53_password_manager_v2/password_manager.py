
from password_generator import PasswordGenerator
from recorder import Recorder
from credential import Credential

class PasswordManager:
    def __init__(self):
        self.generator = PasswordGenerator()
        self.recorder = Recorder()
        self.saved_credentials = {}
        self.load_credentials()

    def password_condition_chekcer(self, received_pass):
        small_l = 0
        cap_l = 0
        num = 0
        sym = 0
        error = 0
        for char in received_pass:
            if char in self.recorder.saved_data["small_letters"]:
                small_l += 1
            elif char in self.recorder.saved_data["capital_letters"]:
                cap_l += 1
            elif char in self.recorder.saved_data["numbers"]:
                num += 1
            elif char in self.recorder.saved_data["symbols"]:
                sym += 1
            else:
                error += 1
        if not error and small_l and cap_l and num and sym and len(received_pass) >= 8:
            return True
        else:
            return False

    def username_validation(self, the_url, the_username):
        if the_url in self.saved_credentials:
            if the_username in self.saved_credentials[the_url]:
                return False
            else:
                return True
        else:
            return True

    def generate_credential(self, the_url, the_username, the_confirmed_password):
        if the_url in self.saved_credentials:
            self.saved_credentials[the_url][the_username] = Credential(the_url, the_username, the_confirmed_password)
        else:
            self.saved_credentials[the_url] = {
                    the_username: Credential(the_url, the_username, the_confirmed_password)
                }
        self.save_credentials()

    def get_generated_password(self, strength):
        generated_password = self.generator.generate_password(self.recorder.saved_data, strength)
        return generated_password

    def load_credentials(self):
        loaded_data = self.recorder.load_cred_data()
        if loaded_data:
            for url, cred in loaded_data.items():
                for username, password in cred.items():
                    if url in self.saved_credentials:
                        self.saved_credentials[url][username] = Credential(url, username, password)
                    else:
                        self.saved_credentials[url] = {
                            username: Credential(url, username, password)
                        }
        print(self.saved_credentials)

    def save_credentials(self):
        self.recorder.write_cred_data(self.saved_credentials)

    def generate_password(self):
        new_password = self.generator.generate_password(self.recorder.saved_data)
        return new_password

    def validate_admin_password(self, received_from_user):
        if received_from_user == self.recorder.load_admin_pass():
            return True
        else:
            return False

    def save_admin_password(self, received_new_password):
        self.recorder.write_admin_password(received_new_password)

    def validate_url(self, url):
        if url in self.saved_credentials:
            return True
        else:
            return False

    def validate_username(self, url, username):
        #* This code runs after url validation
        if username in self.saved_credentials[url]:
            return True
        else:
            return False

    def is_password_different(self, url, username, password):
        #* This code runs after url validation and username validation
        if password == self.saved_credentials[url][username].password:
            return False
        else:
            return True

    def get_cred(self, url, username):
        #* This code runs after confirming credential exist
        return self.saved_credentials[url][username]

    def update_password(self, url, username, new_password):
        self.saved_credentials[url][username].password = new_password
        self.save_credentials()
        self.load_credentials()

    def search_by_username(self, the_username):
        result_data = []
        for url, data_dict in self.saved_credentials.items():
            for username, cred_object in data_dict.items():
                if username == the_username:
                    result_data.append({
                        url: cred_object.password
                    })
        return result_data

    def search_by_url(self, url):
        result_data = []
        if url in self.saved_credentials:
            for username, cred_object in self.saved_credentials[url].items():
                result_data.append({
                    username: cred_object.password
                })
        return result_data

    def delete_credential(self, url, username):
        #* This code runs after all the necessary validations
        if len(self.saved_credentials[url]) > 1:
            del self.saved_credentials[url][username]
        else:
            del self.saved_credentials[url]
        self.save_credentials()

