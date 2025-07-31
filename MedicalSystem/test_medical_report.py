import unittest
from datetime import datetime

import admin
import doctor_report
import patient_report

class TestDoctor(unittest.TestCase):

    def setUp(self):
        self.admin = admin.Admin()

        self.doctor = doctor_report.Doctor("Dr. Ekwe", "09156360746", "201", "Dermatologist", )
        self.patient = patient_report.Patient("Ayimde", "08099887766", "1001", "1985-03-21", "Male", )

        self.admin.add_patient(self.patient)
        self.admin.add_doctor(self.doctor)

        def test_add_patient_and_doctor(self):
            self.assertIn(self.patient, self.admin.doctors)
            self.assertIn(self.doctor, self.admin.doctors)

        def test_find_patient_by_id(self):
            found_patient = self.admin.find_patient_by_id(1001)
            self.assertEqual(found_patient.name, "Ayomide")

        def test_find_doctor_by_id(self):
            found_doctor = self.admin.find_doctor_by_id(1)
            self.assertEqual(found_doctor.name, "Dr. Ekwe")

        def test_schedule_appointment_successfully(self):
            appointment_time = datetime(2025, 8, 1, 15, 30)
            appointment = self.admin.scheduling_appointment(1, 1001, "Skin rash check", appointment_time)

            self.assertIsNotNone(appointment)
            self.assertIn(appointment, self.admin.appointments)
            self.assertIn(appointment, self.doctor.appointments)

        def test_schedule_appointment_with_invalid_ids(self):
            appointment = self.admin.scheduling_appointment(99, 888, "Unknown issue", datetime.now())
            self.assertIsNone(appointment)

        def test_update_doctor_details(self):
            self.doctor.update_details(name="Dr. Ekwe", phone_number="09156360746")
            self.assertEqual(self.doctor.name, "Dr. Ekwe")
            self.assertEqual(self.doctor.phone_number, "09156360746")

        def test_update_patient_details(self):
            self.patient.update_details(name="Robert Marley", phone_number="09156360746")
            self.assertEqual(self.patient.name, "Robert Marley")
            self.assertEqual(self.patient.phone_number, "09156360746")


