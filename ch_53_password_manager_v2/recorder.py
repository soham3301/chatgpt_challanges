
import csv
from encryption import Encryption

class Recorder:
    def __init__(self):
        self.name = "Data Recorder"
        self.security = Encryption()

    def read_files(self):
        with open("./data/letters.csv") as nums:
            render_number = csv.reader(nums)
            for row in render_number:
                print(len(row))

    def receive_credentials(self):
        #* Open credentials csv file
        #* Load it into a dict
        #* Send it to password manager
        pass

    def send_data_for_generator(self):
        #* Open letters, numbers and symbols csv files
        #* Send the raw data to password generator
        pass

    def write_credentials(self, data):
        #* Open credentials csv in write mode
        #* Save the data
        pass
                

rec = Recorder()

rec.read_files()