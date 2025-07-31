from admin import Admin
from doctor_report import Doctor
from patient_report import Patient
from datetime import datetime

admin = Admin()

def print_patient_info(patient: Patient):
    print(f"\n=== Patient Info ===")
    print(f"Name: {patient.name}")
    print(f"ID: {patient.patient_id}")
    print(f"DOB: {patient.date_of_birth}")
    print(f"Gender: {patient.gender}")
    print(f"Phone: {patient.phone_number}")
    print(f"Medical History:")
    for record in patient.medical_history:
        print(f"  - {record.date}: {record.record_details}")


def print_doctor_info(doctor: Doctor):
    print(f"\n=== Doctor Info ===")
    print(f"Name: {doctor.name}")
    print(f"Specialization: {doctor.specialization}")
    print(f"ID: {doctor.doctor_id}")
    print(f"Phone: {doctor.phone_number}")
    print(f"Appointments: {len(doctor.appointments)}")



def main(admin):
    global choice
    while True:
        print("""
======= MEDICAL RECORD SYSTEM =======
1. Add Patient
2. Add Doctor
3. View Patient Info
4. View Doctor Info
5. Add Patient Medical History
6. Schedule Appointment
7. Exit
""")
        try:
            choice = int(input("Enter choice (1-7): "))
        except ValueError:
            print("Invalid input. Enter a number.")
            continue

        match choice:
            case 1:
                name = input("Enter name: ")
                pid = int(input("Enter patient ID: "))
                dob = input("Enter date of birth (YYYY-MM-DD): ")
                gender = input("Enter gender: ")
                phone = input("Enter phone number: ")
                patient = Patient(name, pid, dob, gender, phone)
                admin.add_patient(patient)
                print(f"Patient {name} added.")

            case 2:
                name = input("Enter doctor name: ")
                did = int(input("Enter doctor ID: "))
                specialization = input("Enter specialization: ")
                phone = input("Enter phone number: ")
                doctor = Doctor(name, specialization, did, phone)
                admin.add_doctor(doctor)
                print(f"Doctor {name} added")

            case 3:
                pid = int(input("Enter patient ID: "))
                patient = admin.find_patient_by_id(pid)
                if patient:
                    print_patient_info(patient)
                else:
                    print("Patient not found")

            case 4:
                did = int(input("Enter doctor ID: "))
                doctor = admin.find_doctor_by_id(did)
                if doctor:
                    print_doctor_info(doctor)
                else:
                    print("Doctor not found")

            case 5:
                pid = int(input("Enter patient ID: "))
                patient = admin.find_patient_by_id(pid)
                if patient:
                    note = input("Enter medical record details: ")
                    date = input("Enter date (YYYY-MM-DD): ")
                    record = MedicalRecord(note, date)
                    patient.add_medical_history(record)
                    print(f"Medical Record added.")
                    print("Medical record added")
                else:
                    print("Patient not found")

            case 6:
                did = int(input("Enter doctor ID: "))
                pid = int(input("Enter patient ID: "))
                purpose = input("Enter purpose: ")
                try:
                    date_input = input("Enter appointment datetime (YYYY-MM-DD HH:MM): ")
                    date_time = datetime.strptime(date_input, "%Y-%m-%d %H:%M")
                    appointment = admin.scheduling_appointment(did, pid, purpose, date_time)
                    if appointment:
                        print("Appointment scheduled successfully")
                    else:
                        print("Appointment failed")
                except ValueError:
                    print("Invalid datetime format")

            case 7:
                print("Goodbye!")
                break

            case _:
                print("Invalid option. Do want to try again!")


if _name_ == "_main_":
    main()