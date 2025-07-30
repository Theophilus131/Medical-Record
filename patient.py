class Patient:
    def init(self, name, patient_id, date_of_birth, gender, phone_number):
        self._name = name
        self._patient_id = patient_id
        self._date_of_birth = date_of_birth
        self._gender = gender
        self._phone_number = phone_number
        self.medical_history = []

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_phone_number(self):
        return self._phone_number

    def set_phone_number(self, phone_number):
        self._phone_number = phone_number

    def get_patient_id(self):
        return self._patient_id

    def get_date_of_birth(self):
        return self._date_of_birth

    def get_gender(self):
        return self._gender

    def add_medical_history(self, record):
        self.medical_history.append(record)

    def update_detail(self, name=None, phone_number=None):
        if name:
            self.set_name(name)
        if phone_number:
            self.set_phone_number(phone_number)