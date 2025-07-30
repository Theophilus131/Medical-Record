class Appointment:
    def __init__(self, patient, doctor, date_time):
        self._patient = patient
        self._doctor = doctor
        self._date_time = date_time
        self._status = "Scheduled"

    @property
    def patient(self):
        return self._patient

    @property
    def doctor(self):
        return self._doctor

    @property
    def date_time(self):
        return self._date_time

    @property
    def status(self):
        return self._status

    @patient.setter
    def patient(self, new_patient):
        if not isinstance(new_patient, str):
            raise TypeError('new_patient must be a string')
        else:
            self._patient = new_patient

    @doctor.setter
    def doctor(self, new_doctor):
        if not isinstance(new_doctor, str):
            raise TypeError('new_doctor must be a string')
        else:
            self._doctor = new_doctor

    @date_time.setter
    def date_time(self, new_date_time):
        if not isinstance(new_date_time, str):
            raise TypeError('new_date_time must be a string and follow "YYYY-MM-DD HH:MM" ')
        else:
            self._date_time = new_date_time

