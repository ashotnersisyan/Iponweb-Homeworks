from General_Classes import Person
import datetime
from datetime import datetime as dt
"""Please also check in General_Classes I have modified the Person class to satisfy the specifications of this 
exact problem"""


class PatientError(Exception):
    def __init__(self, explanation, cause):
        self.explanation = explanation
        self.cause = cause

    def print_obj(self):
        print(self.explanation, self.cause)


class Patient(Person):
    def __init__(self, name="", surname="", gender="", age=0, id=0):
        super().__init__(name, surname, gender, age)
        if isinstance(id, int):
            self.__id = id
        else:
            raise PatientError("The id should be an integer", id)

    def __repr__(self):
        return f"{self.name} {self.surname} - {self.gender}, {self.age} years old."

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        if isinstance(value, int):
            self.__id = value
        else:
            raise PatientError("The id should be an integer", value)

    def __eq__(self, other):
        if self.name == other.name and self.surname == other.surname and self.age == other.age \
                and self.gender == other.gender:
            return True
        return False

    def __ne__(self, other):
        return not self == other


class DoctorError(Exception):
    def __init__(self, explanation, cause):
        self.explanation = explanation
        self.cause = cause

    def print_obj(self):
        print(self.explanation, self.cause)


class Doctor(Person):
    """I will assume that Doctor works from 10 in the morning to 18 in the evening, 8 straight hours.
    I will use IDs in the schedule dictionary to fix the patients"""
    def __init__(self, name="", surname="", schedule={}):
        super().__init__(name, surname,)
        if isinstance(schedule, dict):
            self.__schedule = schedule
        else:
            raise DoctorError("The schedule should be a dictionary", schedule)

    @property
    def schedule(self):
        return self.__schedule

    @schedule.setter
    def schedule(self, value):
        if isinstance(value, dict):
            self.__schedule = value
        else:
            raise DoctorError("The schedule should be a dictionary", value)

    def __repr__(self):
        sch = ""
        for pat_id in self.__schedule:
            sch += str(pat_id) + ": " + str(self.__schedule[pat_id]) + "\n"
        return f"{self.name} {self.surname}, schedule" + "\n" + sch

    def is_free(self, when):
        when_time = dt.strptime(when.strftime("%H:%M:%S"), "%H:%M:%S").time()
        if when_time < datetime.time(hour=10, minute=0, second=0) or when_time > datetime.time(hour=17, minute=30,
                                                                                               second=0):
            return False
        before = when - datetime.timedelta(minutes=30)
        after = when + datetime.timedelta(minutes=30)
        for pat_id in self.__schedule:
            if self.__schedule[pat_id] > before and self.__schedule[pat_id] < after:
                return False
        return True

    def is_registered(self, pat):
        if pat.id in self.__schedule:
            return True
        return False

    def register_patient(self, pat, when):
        if self.is_registered(pat):
            return "The patient is already registered."
        if self.is_free(when):
            self.__schedule[pat.id] = when
            return "Patient Registered!"
        return "Not available at the specified time."


patient1 = Patient("George", "Pitt", "M", 25, 1903)
patient2 = Patient("Vahan", "Martirosyan", "M", 38, 9006)
patient3 = Patient("Armine", "Petrosyan", "F", 22, 8310)
print(patient1)
print(patient2)
print(patient3)
doctor1 = Doctor("Arsem", "Movsisyan")
print(doctor1)
print(doctor1.register_patient(patient1, dt(year=2023, month=2, day=13, hour=12, minute=33, second=50)))
print(doctor1.register_patient(patient2, dt(year=2023, month=2, day=14, hour=12, minute=33, second=50)))
print(doctor1.register_patient(patient3, dt(year=2023, month=2, day=13, hour=12, minute=43, second=50)))
print(doctor1.register_patient(patient2, dt(year=2023, month=2, day=16, hour=12, minute=43, second=50)))
print(doctor1)










