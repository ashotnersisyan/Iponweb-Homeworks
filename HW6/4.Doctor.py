from HelperClasses import Person


class DoctorError(Exception):
    def __init__(self, explanation, cause):
        self.explanation = explanation
        self.cause = cause

    def print_obj(self):
        print(self.explanation, self.cause)


class Doctor(Person):
    def __init__(self, name="", surname="", gender="", age=0, address="", friends=[], job=[],
                 department="", profession="", patronymic="", salary=0):
        super().__init__(name, surname, gender, age, address, friends, job)
        if isinstance(department, str):
            self.__department = department
        else:
            raise DoctorError("The department name should be a string", department)
        if isinstance(profession, str):
            self.__profession = profession
        else:
            raise DoctorError("The profession name should be a string", profession)
        if isinstance(patronymic, str):
            self.__patronymic = patronymic
        else:
            raise DoctorError("The patronymic should be a string", patronymic)
        if isinstance(salary, int) or isinstance(salary, float):
            self.__salary = salary
        else:
            raise DoctorError("The salary should be an integer or a float", salary)

    @property
    def department(self):
        return self.__department

    @department.setter
    def department(self, value):
        if isinstance(value, str):
            self.__department = value
        else:
            raise DoctorError("The department name should be a string", value)

    @property
    def profession(self):
        return self.__profession

    @profession.setter
    def profession(self, value):
        if isinstance(value, str):
            self.__profession = value
        else:
            raise DoctorError("The profession name should be a string", value)

    @property
    def patronymic(self):
        return self.__patronymic

    @patronymic.setter
    def patronymic(self, value):
        if isinstance(value, str):
            self.__patronymic = value
        else:
            raise DoctorError("The patronymic should be a string", value)

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if isinstance(value, int) or isinstance(value, float):
            self.__salary = value
        else:
            raise DoctorError("The salary should be an integer or a float", value)

    def __repr__(self):
        return repr(f"This is Doctor {self.name} {self.__patronymic} {self.surname}."
                    f"Working at the department of {self.__department}, professionalized in {self.__profession}, "
                    f"with salary {self.__salary}"
                    f"A {self.gender}, {self.age} years of age. "
                    f"Residing at {self.address}")


doctor1 = Doctor("Artak", "Aristakesyan", "Male", 45, "Zeytun Taxamas", [], [], "Medical service policy",
                 "Chemist", "Vahani", 550000)
print(doctor1)
print(doctor1.name)
#doctor1.department = 1231
# print(doctor1)
