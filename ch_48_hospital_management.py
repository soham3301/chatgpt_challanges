
class Human:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.inbox = []

class Admin(Human):
    def __init__(self, name, password):
        super().__init__(name, password)
        self.status = "admin"

class Doctor(Human):
    def __init__(self, name, password, specialist, fee):
        super().__init__(name, password)
        self.status = "doctor"
        self.specialist = specialist
        self.fee = fee
        self.is_assigned = False

class Patient(Human):
    def __init__(self, name, password):
        super().__init__(name, password)
        self.status = "patient"
        self.billbox = []

class Ward:
    def __init__(self, name):
        self.name = name
        self.beds = []
        self.meds = []

class Bed:
    def __init__(self, number):
        self.bed_number = number
        self.patient = None
        self.charge = 20

    def admit_patient(self, new_patient):
        if new_patient:
            self.patient = new_patient
            self.patient.billbox.append(self.charge)
            return True
        else:
            return False

class Medicine:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

class Hospital:
    def __init__(self, name):
        self.name = name
        self.admin = None
        self.doctors = []
        self.patients = []
        self.wards = []
        self.beds = []
        self.meds = []

    def authentication(self):
        print("Authenticated")

    def assign_doctor(self):
        print("Doctor Assigned")

    def discharge_patient(self):
        print("Patient Discharged")

sample_patients = [
    Patient("Rajiv", 1),
    Patient("Amitabh", 2),
    Patient("Souvik", 3),
    Patient("Subhadeep", 4),
    Patient("Manidipa", 5),
    Patient("Joydeep", 6),
    Patient("Gautam", 7),
    Patient("Rohan", 8),
    Patient("Shouni", 9),
]

sample_doctors = [
    Doctor("Kallol", 11, "ent", 25),
    Doctor("Abhishek", 12, "gastro", 17),
    Doctor("Priya", 13, "cardio", 22),
    Doctor("Nandita", 14, "children", 20),
    Doctor("Srijit", 15, "emergency", 18),
]

admin = Admin("Soham", 0)

total_beds = [Bed(1), Bed(2), Bed(3), Bed(4), Bed(5), Bed(6), Bed(7), Bed(8), Bed(9), Bed(10), Bed(11), Bed(12), Bed(13), Bed(14), Bed(15),]

total_wards = [
    Ward("ent"),
    Ward("gastro"),
    Ward("cardio"),
    Ward("children"),
    Ward("emergency"),
]