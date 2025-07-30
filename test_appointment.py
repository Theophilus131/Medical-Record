import unittest

import Appointment

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.appointment = Appointment.Appointment("theo umar", "usman","2025-27-08  12:34")

    def test_patientsCanBeUpdated(self):
        self.appointment.patient = "theo umar"
        self.assertEqual(self.appointment.patient, "theo umar")

    def test_doctorsCanBeUpdated(self):
        self.appointment.doctor = "okafor james"
        self.assertEqual(self.appointment.doctor, "okafor james")

    def test_date_time(self):
        self.appointment.date_time = "2025-27-08 12:34"
        self.assertEqual(self.appointment.date_time, "2025-27-08 12:34")

    def test_check_if_i_can_schdule_Appointment_status(self):
        self.appointment.status= True
        self.assertTrue(self.appointment.status)






