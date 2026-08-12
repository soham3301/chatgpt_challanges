
from password_generator import PasswordGenerator
from recorder import Recorder
from credential import Credential

class PasswordManager:
    def __init__(self):
        self.name = "Password Manager"
        self.generator = PasswordGenerator()
        self.record = Recorder()
        self.saved_credentials = {}
        self.load_credentials()

    def load_credentials(self):
        data = self.record.receive_credentials()
        #* Generate Credential Object using that data
        #* Load the data into saved_credentials
        pass

    def save_credentials(self):
        self.record.write_credentials(self.saved_credentials)

    def generate_password(self):
        received_data = self.record.send_data_for_generator()
        new_password = self.generator.generate_password(received_data)
        return new_password