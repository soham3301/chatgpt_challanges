
from password_generator import PasswordGenerator
from recorder import Recorder
from credential import Credential

class PasswordManager:
    def __init__(self):
        self.generator = PasswordGenerator()
        self.recorder = Recorder()
        self.saved_credentials = {}
        self.load_credentials()

    def condition_chekcer(self, received_pass):
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

    def get_generated_password(self, strength):
        generated_password = self.generator.generate_password(self.recorder.saved_data, strength)
        return generated_password

    def load_credentials(self):
        #* Generate Credential Object using that data
        #* Load the data into saved_credentials
        pass

    def save_credentials(self):
        self.recorder.write_credentials(self.saved_credentials)

    def save_new_credential(self, cred):
        pass

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
        