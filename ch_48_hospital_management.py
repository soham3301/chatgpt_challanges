
class Person:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.id = ""
        self.inbox = []

    def helper_generate_id(self):
        self.id = self.name[0].lower() + (str(self.password))[0]

    def login(self, input_id, input_password):
        if input_id and input_password:
            if input_id == self.id and int(input_password) == self.password:
                return True
            else:
                return False
        else:
            return False

    def check_details(self):
        return [self.name, self.id, self.password]

    def check_inbox(self):
        return self.inbox

class Admin(Person):
    def __init__(self, name, password):
        super().__init__(name, password)
        self.status = "admin"

    def add_new_doctor(self, data, hospital):
        if data[0] and data[1] and data[3]:
            new_doctor = Doctor(data[0], data[1], data[2], data[3])
            new_doctor.helper_generate_id()
            hospital.doctors.append(new_doctor)
            return True
        else:
            return False

    def add_new_ward(self, ward_name, hospital):
        if ward_name:
            hospital.wards.append(Ward(ward_name))
            return True
        else:
            return False

    def add_new_med(self, med_name, med_cost, hospital):
        if med_name and med_cost:
            hospital.meds.append(Medicine(med_name, med_cost))
            return True
        else:
            return False

#? NOTE:- The responsibility of adding new Data into hospital, like adding a new doc, new ward or new meds, is intentionally given to admin so Hospital Object doesn't become too large.

class Doctor(Person):
    def __init__(self, name, password, specialist, fee):
        super().__init__(name, password)
        self.status = "doctor"
        self.specialist = specialist
        self.fee = fee
        self.push_injection_cost = 5
        self.assigned_patients = []

    def helper_need_this_medicine(self, medicine_name, the_admin):
        the_admin.inbox.append({
            "medicine_needed":medicine_name,
        })
        return None

    def helper_get_medicine(self, med_list, med_name, admin):
        if med_name and med_list:
            for med in med_list:
                if med.name == med_name:
                    return med
            return self.helper_need_this_medicine(med_name, admin)

    def check_assigned_patients(self):
        return self.assigned_patients

    def reccomend_medicine(self, medicine_name, medicine_list, the_admin, the_patient):
        the_medicine = self.helper_get_medicine(medicine_list, medicine_name, the_admin)
        if the_medicine and the_patient:
            the_patient.billbox.append(the_medicine.cost)
            return True
        else:
            return False

    def give_injection(self, the_patient):
        if the_patient:
            the_patient.billbox.append(self.push_injection_cost)
            return True
        else:
            return False

class Patient(Person):
    def __init__(self, name, password):
        super().__init__(name, password)
        self.status = "patient"
        self.is_admitted = False
        self.billbox = []

    def check_bill(self):
        bill = 0
        for bill in self.billbox:
            bill += bill
        return bill

    def pay_bill(self, generated_bill, received_amount):
        if received_amount >= generated_bill:
            self.billbox.clear()
            return received_amount - generated_bill
        else:
            return None

class Ward:
    def __init__(self, name):
        self.name = name
        self.supervisor = None
        self.beds = []

    def add_bed(self, bed_number):
        if bed_number:
            new_bed = Bed(bed_number)
            self.beds.append(new_bed)
            return True
        else:
            return False

    def add_supervisor(self, the_doctor):
        if not self.supervisor:
            if self.name == "emergency" and not the_doctor.specialist:
                self.supervisor = the_doctor
                return True
            elif self.name == the_doctor.specialist:
                self.supervisor = the_doctor
                return True
            else:
                return False
        else:
            return False

class Bed:
    def __init__(self, number):
        self.bed_number = number
        self.patient = None
        self.charge = 20

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
        self.meds = []

    def helper_get_ward(self, name_of_ward):
        for ward in self.wards:
            if ward.name == name_of_ward:
                return ward
        return None

    def helper_add_patient(self, data):
        if data[0] and data[1]:
            the_patient = Patient(data[0], data[1])
            the_patient.helper_generate_id()
            self.patients.append(the_patient)
            return the_patient
        else:
            return None

    def add_new_bed(self, ward_name):
        new_bed_no = 0
        available_beds = []
        for ward in self.wards:
            for bed in ward.beds:
                available_beds.append(bed.bed_number)
        for bed_no in available_beds:
            if bed_no > new_bed_no:
                new_bed_no = bed_no
        new_bed_no += 1
        the_ward = self.helper_get_ward(ward_name)
        if new_bed_no and the_ward:
            if the_ward.add_bed(new_bed_no):
                return True
            else:
                return False

    def admit_patient(self, patient_data, ward_name):
        if patient_data and ward_name:
            new_patient = self.helper_add_patient(patient_data)        
            the_ward = self.helper_get_ward(ward_name)
            if new_patient and the_ward:
                for bed in the_ward.beds:
                    if bed.patient == None:
                        new_patient.is_admitted = True
                        new_patient.billbox.append(bed.charge)
                        bed.patient = new_patient
                        return True
            else:
                return False
        else:
            return False

    def authentication(self, user_id, user_password):
        the_user = None
        if self.admin.id == user_id:
            if self.admin.login(user_id, user_password):
                the_user = self.admin
                return the_user
            else:
                return None
        else:
            for doctor in self.doctors:
                if doctor.id == user_id:
                    if doctor.login(user_id, user_password):
                        the_user = doctor
                        return the_user
                    else:
                        return None
            for patient in self.patients:
                if patient.id == user_id:
                    if patient.login(user_id, user_password):
                        the_user = patient
                        return the_user
                    else:
                        return None
            return None

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
    Doctor("Srijit", 15, None, 18),
]

total_wards = [
    Ward("ent"),
    Ward("gastro"),
    Ward("cardio"),
    Ward("children"),
    Ward("emergency"),
]

for ward in total_wards:
    for doc in sample_doctors:
        ward.add_supervisor(doc)

for bed in range(1, 4):
    total_wards[0].beds.append(Bed(bed))
for bed in range(4, 7):
    total_wards[1].beds.append(Bed(bed))
for bed in range(7, 10):
    total_wards[2].beds.append(Bed(bed))
for bed in range(10, 13):
    total_wards[3].beds.append(Bed(bed))
for bed in range(13, 16):
    total_wards[4].beds.append(Bed(bed))

total_meds = [
    Medicine("Paracetamol", 13),
    Medicine("Ibuprofen", 17),
    Medicine("Dolo650", 27),
    Medicine("Amlodec2.5", 14),
    Medicine("Pan40", 8),
    Medicine("Voveran", 18),
    Medicine("Azithral", 20),
]

soham = Admin("Soham", 0)
soham.helper_generate_id()
goodcare = Hospital("GoodCare")
goodcare.admin = soham

for doctor in sample_doctors:
    doctor.helper_generate_id()
    goodcare.doctors.append(doctor)

for patient in sample_patients:
    patient.helper_generate_id()
    goodcare.patients.append(patient)

for ward in total_wards:
    goodcare.wards.append(ward)

for med in total_meds:
    goodcare.meds.append(med)



#* ----------------------------------------- INPUTS ------------------------------------------

def get_id():
    return input("Enter ID: ")

def get_password():
    return input("Enter Password: ")

def get_input():
    return input("Choose from above: ")





#* ----------------------------------------- DISPLAYS ------------------------------------------


def display_welcome_board(user):
    print(f"Welcome {user.name} | Status: {user.status.title()}")

def display_mapper(user):
    saved_displays = {
        "admin":admin_display,
        "doctor":doctor_display,
        "patient":patient_display,
    }
    if user.status in saved_displays:
        saved_displays[user.status]()

def admin_display():
    print('''
1. Check Details
2. Check Inbox
3. Add a new Doctor
4. Add a new Ward
5. Add a new Medicine
6. Add more Bed
7. Admit a Patient
8. Assign a Dcotor
9. Discharge Patient
10. Add a Ward Supervisor
0. Exit
''')

def doctor_display():
    print('''
1. Check Details
2. Check Inbox
3. Check Assigned Patient
4. Check Ward Patients
0. Exit
''')

def doctor_display_2():
    print('''
1. Recommend Medicine
2. Give Injection
0. Back
''')

def patient_display():
    print('''
1. Check Details
2. Check Inbox
3. Check Bill
4. Pay Bill
0. Exit
''')

#* ----------------------------------------- FUNCTIONS ------------------------------------------















#* ----------------------------------------- DISPATCHERS ------------------------------------------

def admin_mapper(the_user, the_input, the_hospital):
    print("You Reached Admin Mapper")

def doctor_mapper(the_user, the_input, the_hospital):
    print("You Reached Doctor Mapper")

def patient_mapper(the_user, the_input, the_hospital):
    print("You Reached Patient Mapper")

def input_dispatcher(user, input, hospital):
    saved_input_mapper_functions = {
        "admin":admin_mapper,
        "doctor":doctor_mapper,
        "patient":patient_mapper,
    }
    if user.status in saved_input_mapper_functions:
        saved_input_mapper_functions[user.status](user, input, hospital)

def main():
    program_running = True
    while program_running:
        id = get_id()
        password = get_password()
        the_user = goodcare.authentication(id, password)
        if the_user:
            while True:
                display_welcome_board(the_user)
                display_mapper(the_user)
                user_input = get_input()
                if user_input == "0":
                    print("logged Out")
                    break
                else:
                    input_dispatcher(the_user, user_input, goodcare)
        else:
            print("User Not Found")
            break

main()