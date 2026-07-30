
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
            existing_ward_names = []
            for ward in hospital.wards:
                existing_ward_names.append(ward.name)
            if ward_name in existing_ward_names:
                return False
            else:
                hospital.wards.append(Ward(ward_name))
                return True
        else:
            return False

    def add_new_med(self, med_name, med_cost, hospital):
        if med_name and med_cost:
            hospital.meds.append(Medicine(med_name, int(med_cost)))
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

    def check_ward_patients(self, hospital):
        patients = []
        ward_name = ""
        for ward in hospital.wards:
            if ward.supervisor.specialist == self.specialist:
                ward_name = ward.name
                for bed in ward.beds:
                    if bed.occupied:
                        patients.append(bed.occupied)
        return patients, ward_name

    def reccomend_medicine(self, medicine_name, medicine_list, the_admin, the_patient):
        the_medicine = self.helper_get_medicine(medicine_list, medicine_name, the_admin)
        if the_medicine and the_patient:
            the_patient.billbox.append(the_medicine.cost)
            the_patient.inbox.append({
                "medicine recommended to you":the_medicine.name,
            })
            return True
        else:
            return False

    def give_injection(self, the_patient):
        if the_patient:
            the_patient.billbox.append(self.push_injection_cost)
            the_patient.inbox.append({
                "injection given by":f"doctor {self.name}",
            })
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
        for my_bill in self.billbox:
            bill += my_bill
        return bill

    def pay_bill(self, generated_bill, received_amount):
        if received_amount >= generated_bill:
            self.billbox.clear()
            return True, received_amount - generated_bill
        else:
            return False, None

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
        self.occupied = None
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

    def helper_get_patient(self, name):
        if name:
            for patient in self.patients:
                if patient.name == name:
                    return patient
            return None
        else:
            return None

    def helper_get_doctor(self, name):
        if name:
            for doctor in self.doctors:
                if doctor.name == name:
                    return doctor
            return None
        else:
            return None

    def helper_add_patient(self, data):
        if data[0] and data[1]:
            the_patient = Patient(data[0], data[1])
            the_patient.helper_generate_id()
            self.patients.append(the_patient)
            return the_patient
        else:
            return None

    def add_new_bed(self, the_ward):
        new_bed_no = 0
        available_beds = []
        for ward in self.wards:
            for bed in ward.beds:
                available_beds.append(bed.bed_number)
        for bed_no in available_beds:
            if bed_no > new_bed_no:
                new_bed_no = bed_no
        new_bed_no += 1
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
                    if not bed.occupied:
                        new_patient.is_admitted = True
                        new_patient.billbox.append(bed.charge)
                        bed.occupied = new_patient
                        return True
                return False
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

    def assign_doctor(self, patient_name, doctor_name):
        the_patient = self.helper_get_patient(patient_name)
        the_doctor = self.helper_get_doctor(doctor_name)
        if the_patient and the_doctor:
            the_doctor.assigned_patients.append(the_patient)
            the_doctor.inbox.append({
                "Got a new patient assigned":the_patient.name,
            })
            the_patient.billbox.append(the_doctor.fee)
            the_patient.inbox.append({
                "Doctor assigned to you":the_doctor.name,
            })
            return True
        else:
            return False

    def discharge_patient(self, patient_name):
        the_patient = self.helper_get_patient(patient_name)
        if the_patient:
            total_bill = sum(the_patient.billbox)
            if not total_bill:
                for ward in self.wards:
                    for bed in ward.beds:
                        if bed.occupied:
                            if bed.occupied.name == the_patient.name:
                                bed.occupied = None
                for patient in self.patients:
                    if patient.name == the_patient.name:
                        self.patients.remove(patient)
                return True
            else:
                the_patient.inbox.append({
                    "Pay bill for discharge": total_bill
                })
                return False

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

for ward in total_wards:
    goodcare.wards.append(ward)

for med in total_meds:
    goodcare.meds.append(med)

goodcare.admit_patient(["Rajiv", 1], "ent")
goodcare.admit_patient(["Amitabh", 2], "ent")
goodcare.admit_patient(["Souvik", 3], "gastro")
goodcare.admit_patient(["Subhadeep", 4], "cardio")
goodcare.admit_patient(["Manidipa", 5], "cardio")
goodcare.admit_patient(["Joydeep", 6], "cardio")
goodcare.admit_patient(["Gautam", 7], "children")
goodcare.admit_patient(["Rohan", 8], "children")
goodcare.admit_patient(["Shouni", 9], "emergency")

#* ----------------------------------------- INPUTS ------------------------------------------

def get_id():
    return input("Enter ID: ")

def get_password():
    return input("Enter Password: ")

def get_input():
    return input("Choose from above: ")

def get_name():
    return input("Enter Name: ")

def get_speciality():
    return input("Enter Speciality: ")

def get_patient():
    return input("Enter Patient's ID: ")

def get_bill():
    try:
        return abs(round(int(input("Enter Bill Amount: "))))
    except:
        invalid_input()
        return None

def get_fee():
    try:
        return abs(round(int(input("Enter Fee: "))))
    except ValueError:
        invalid_input()
        return None

def get_cost():
    try:
        return abs(round(int(input("Enter Cost: "))))
    except ValueError:
        invalid_input()
        return None

def get_how_many():
    try:
        number_of_beds = abs(round(int(input("Enter number of beds: "))))
        if number_of_beds > 0 and number_of_beds <= 5:
            return number_of_beds
        else:
            return None
    except ValueError:
        invalid_input()
        return None

def want_to_add_supervisor():
    return input("Want to add Supervisor? Y / N\n").lower()

def get_ward_name():
    return input("Enter Ward Name: ")

def get_doctor_name():
    return input("Enter Doctor Name: ")

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

def print_details(user_data):
    print(f"Name: {user_data[0].title()} | ID: {user_data[1]} | Password: {user_data[2]}")

def print_inbox(the_inbox):
    if the_inbox:
        for item in the_inbox:
            for key, value in item.items():
                print(f"{key}: {value}")
    else:
        print("Your Inbox is Empty")

def display_wards(hospital):
    for ward in hospital.wards:
        print(ward.name.title())

def choose_from_above(data):
    print(f"Please choose a {data} from above")

def choose_something_new(data):
    print(f"These {data} are available, choose something new.")

def choose_between():
    print("Choose between 1 to 5.")

def invalid_input():
    print("Invalid Input")

def doctor_add_announcment(consent):
    if consent:
        print("Doctor Added to Hospital")
    else:
        print("Doctor Recruitment Failed")

def ward_add_announcment(consent):
    if consent:
        print("Ward Added to Hospital")
    else:
        print("Ward addition Failed")

def med_add_announcment(consent):
    if consent:
        print("Medicine Added into Hospital")
    else:
        print("Medicine addition Failed")

def bed_addition_announcment(consent, the_ward, no_of_beds):
    if consent:
        print(f"{the_ward.name.title()} ward got {no_of_beds} new beds.")
    else:
        print("New bed not added.")

def display_empty_beds(hospital):
    for ward in hospital.wards:
        total_beds = 0
        occupied_beds = 0
        for bed in ward.beds:
            if bed.occupied:
                occupied_beds += 1
            total_beds += 1
        print(f"{ward.name.title()} ward has {total_beds - occupied_beds} free beds.")

def display_admit_confirmation(consent, name_of_patient, name_of_ward):
    if consent:
        print(f"{name_of_patient.title()} has been admitted into {name_of_ward.title()} ward.")
    else:
        print("Patient Admision Failed.")

def display_all_patients(hospital):
    print("ALL PATIENT NAMES")
    for patient in hospital.patients:
        print(patient.name.title())

def display_all_doctors(hospital):
    print("ALL DOCTORS")
    for doc in hospital.doctors:
        print(f"Name: {doc.name.title()} | Speciality: {doc.specialist}")

def display_doc_assigned(consent, patient_name, doctor_name):
    if consent:
        print(f"Doctor {doctor_name.title()} has been assigned to {patient_name.title()}.")
    else:
        print("Doctor not Assigned.")

def display_discharge_status(consent, patient_name):
    if consent:
        print(f"Patient named {patient_name.title()} has been discharged.")
    else:
        print(f"{patient_name.title()} has not been discharged.")

def print_final_bill(bill):
    print(f"Your Total Bill is INR: {bill} /- as of now.")

def display_bill_status(consent):
    if consent:
        print(f"You Paid the bill. Congrats")
    else:
        print("Bill Payment Not Done.")

def display_return_amount(return_amount):
    print(f"Here is your return amount, INR {return_amount} /-")

def display_choose_one_patient():
    print("Choose One Patient from Above")

def display_available_meds(the_hospital):
    print("Available Medicines")
    for med in the_hospital.meds:
        print(med.name)

def display_med_recommend_status(consent, medicine_name, patient_name):
    if consent:
        print(f"{medicine_name} Recommended to {patient_name}")
    else:
        print("Medicine is not available as of now.")

def display_injection_status(consent, doc, patient):
    if consent:
        print(f"An Injection was given by Doctor {doc} to {patient}")
    else:
        print("Injection Push Unsuccessful.")

def check_ward_details(hospital):
    the_decision = False
    all_have_supervisor = True
    for ward in hospital.wards:
        if not ward.supervisor:
            print(f"Ward Name: {ward.name} | Supervisor: Not Assigned")
            all_have_supervisor = False
            the_decision = True
    if all_have_supervisor:
        print("All Wards have Supervisor.")
    return the_decision

def display_supervisor_addition_status(consent, ward, doctor):
    if consent:
        print(f"Doctor {doctor.name} has been assigned to Ward {ward.name} as a Supervisor.")
    else:
        print("Supervisor Addition Failed")

def display_logged_out():
    print("logged Out")

def display_user_not_found():
    print("User Not Found")

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

def doctor_display_2(the_patient):
    print(f'''
Patient Name: {the_patient.name}
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

#* ----------------------------------------- DOC DISPLAY - 2 ------------------------------------------

def check_patients(patients_list, data, hospital, user):
    if patients_list:
        print(f"Available Patients | {data}")
        for patient in patients_list:
            print(f"Name: {patient.name} | ID: {patient.id}")
        display_choose_one_patient()
        patient_id = get_patient()
        for patient in patients_list:
            if patient.id == patient_id:
                while True:
                    doctor_display_2(patient)
                    input = get_input()
                    if input == "0":
                        break
                    elif input == "1":
                        display_available_meds(hospital)
                        med_name = get_name()
                        if user.reccomend_medicine(med_name, hospital.meds, hospital.admin, patient):
                            display_med_recommend_status(1, med_name, patient.name)
                        else:
                            display_med_recommend_status(0, med_name, patient.name)
                    elif input == "2":
                        if user.give_injection(patient):
                            display_injection_status(1, user.name, patient.name)
                        else:
                            display_injection_status(0, user.name, patient.name)
                    else:
                        invalid_input()
        invalid_input()
    else:
        print("No Patient available right now.")

#* ----------------------------------------- DISPATCHERS ------------------------------------------

def admin_mapper(the_user, the_input, the_hospital):
    if the_input == "1":
        data = the_user.check_details()
        print_details(data)
    elif the_input == "2":
        inbox = the_user.check_inbox()
        print_inbox(inbox)
    elif the_input == "3":
        name = get_name()
        password = get_password()
        speciality = get_speciality()
        fee = get_fee()
        if name and password and speciality and fee:
            if the_user.add_new_doctor([name.title(), password, speciality.lower(), fee], the_hospital):
                doctor_add_announcment(1)
            else:
                doctor_add_announcment(0)
        else:
            invalid_input()
    elif the_input == "4":
        display_wards(the_hospital)
        choose_something_new("wards")
        ward_name = get_name()
        if ward_name:
            if the_user.add_new_ward(ward_name.lower(), the_hospital):
                ward_add_announcment(1)
            else:
                ward_add_announcment(0)
        else:
            invalid_input()
    elif the_input == "5":
        medicine_name = get_name()
        medicine_cost = get_cost()
        if medicine_name and medicine_cost:
            if the_user.add_new_med(medicine_name, medicine_cost, the_hospital):
                med_add_announcment(1)
            else:
                med_add_announcment(0)
        else:
            invalid_input()
    elif the_input == "6":
        display_wards(the_hospital)
        choose_from_above("ward")
        ward_name = get_name()
        choose_between()
        how_many_beds = get_how_many()
        ward = the_hospital.helper_get_ward(ward_name.lower())
        if ward and how_many_beds:
            for _ in range(how_many_beds):
                the_hospital.add_new_bed(ward)
            bed_addition_announcment(1, ward, how_many_beds)
        else:
            bed_addition_announcment(0, ward, how_many_beds)
    elif the_input == "7":
        patient_name = get_name()
        patient_password = get_password()
        display_empty_beds(the_hospital)
        choose_from_above("ward")
        ward_name = get_name()
        if the_hospital.admit_patient([patient_name.title(), patient_password], ward_name.lower()):
            display_admit_confirmation(1, patient_name, ward_name)
        else:
            display_admit_confirmation(0, patient_name, ward_name)
    elif the_input == "8":
        display_all_patients(the_hospital)
        name_of_patient = get_name()
        display_all_doctors(the_hospital)
        name_of_doctor = get_name()
        if the_hospital.assign_doctor(name_of_patient.title(), name_of_doctor.title()):
            display_doc_assigned(1, name_of_patient, name_of_doctor)
        else:
            display_doc_assigned(0, name_of_patient, name_of_doctor)
    elif the_input == "9":
        display_all_patients(the_hospital)
        the_patient_name = get_name()
        if the_hospital.discharge_patient(the_patient_name.title()):
            display_discharge_status(1, the_patient_name)
        else:
            display_discharge_status(0, the_patient_name)
    elif the_input == "10":
        if check_ward_details(the_hospital):
            user_consent = want_to_add_supervisor()
            if user_consent == "y":
                name_of_ward = get_ward_name()
                the_ward = the_hospital.helper_get_ward(name_of_ward.lower())
                if the_ward:
                    display_all_doctors(the_hospital)
                    doc_name = get_doctor_name()
                    the_doctor = the_hospital.helper_get_doctor(doc_name.title())
                    if the_doctor:
                        if the_ward.add_supervisor(the_doctor):
                            display_supervisor_addition_status(1, the_ward, the_doctor)
                        else:
                            display_supervisor_addition_status(0, the_ward, the_doctor)
                    else:
                        invalid_input()
                else:
                    invalid_input()
    else:
        invalid_input()

def doctor_mapper(the_user, the_input, the_hospital):
    if the_input == "1":
        data = the_user.check_details()
        print_details(data)
    elif the_input == "2":
        inbox = the_user.check_inbox()
        print_inbox(inbox)
    elif the_input == "3":
        assigned_patients = the_user.check_assigned_patients()
        check_patients(assigned_patients, "Assigned to You", the_hospital, the_user)
    elif the_input == "4":
        ward_patients, name_of_ward = the_user.check_ward_patients(the_hospital)
        check_patients(ward_patients, f"Inside Ward: {name_of_ward.title()}", the_hospital, the_user)
    else:
        invalid_input()

def patient_mapper(the_user, the_input, the_hospital):
    if the_input == "1":
        data = the_user.check_details()
        print_details(data)
    elif the_input == "2":
        inbox = the_user.check_inbox()
        print_inbox(inbox)
    elif the_input == "3":
        final_bill = the_user.check_bill()
        print_final_bill(final_bill)
    elif the_input == "4":
        total_bill = the_user.check_bill()
        bill_amount = get_bill()
        if bill_amount:
            done_or_not, amount = the_user.pay_bill(total_bill, bill_amount)
            if done_or_not:
                display_bill_status(1)
                if amount:
                    display_return_amount(amount)
            else:
                display_bill_status(0)
        else:
            invalid_input()
    else:
        invalid_input()

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
            display_welcome_board(the_user)
            while True:
                display_mapper(the_user)
                user_input = get_input()
                if user_input == "0":
                    display_logged_out()
                    break
                else:
                    input_dispatcher(the_user, user_input, goodcare)
        else:
            display_user_not_found()
            break

main()