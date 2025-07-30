from MedicalRecord.DoctorReport import Doctor
from MedicalRecord.PatientReport import Patient
import datetime


class Admin:
    def _init_(self):
        self.patients = []
        self.doctors = []
        self.appointments = []

    def add_patient(self, patient: Patient):
        self.patients.append(patient)

    def add_doctor(self, doctor: Doctor):
        self.doctors.append(doctor)

    def find_patient_by_id(self, patient_id: int):
        for patient in self.patients:
            if patient.patient_id == patient_id:
                return patient

    def find_doctor_by_id(self, doctor_id: int):
        for doctor in self.doctors:
            if doctor.doctor_id == doctor_id:
                return doctor

    def scheduling_appointment(self, doctor_id: int, patient_id: int, purpose: str, date_time: datetime):
        doctor = self.find_doctor_by_id(doctor_id)
        patient = self.find_patient_by_id(patient_id)
        if doctor and patient:
            appointment = Appointment(doctor, patient, date_time)
            appointment.scheduling()
            self.apointments.append(appointment)
            return appointment
        else:
            print("Doctor or Patient not found.")
            return None