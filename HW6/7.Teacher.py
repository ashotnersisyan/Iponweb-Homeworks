from HelperClasses import Person
from HelperClasses import Money
from HelperClasses import University
from HelperClasses import Date
from HelperClasses import City


class TeacherError(Exception):
    def __init__(self, explanation, cause):
        self.explanation = explanation
        self.cause = cause

    def print_obj(self):
        print(self.explanation, self.cause)


class Teacher(Person):
    def __init__(self, name="", surname="", gender="", age=0, address="", friends=[], job=[],
                 university=University(), faculty="", experience=0, start_work_at=Date(), subject="", salary=Money()):
        super().__init__(name, surname, gender, age, address, friends, job)
        if isinstance(university, University):
            self.__university = university
        else:
            raise TeacherError("The university should be a Univesity class member", university)
        if isinstance(faculty, str):
            self.__faculty = faculty
        else:
            raise TeacherError("The faculty should be a string", faculty)
        if isinstance(experience, int):
            self.__experience = experience
        else:
            raise TeacherError("The experience should be an integer", experience)
        if isinstance(start_work_at, Date):
            self.__start_work_at = start_work_at
        else:
            raise TeacherError("The start_work_at should be a Date class member", start_work_at)
        if isinstance(subject, str):
            self.__subject = subject
        else:
            raise TeacherError("The subject should be a string", subject)
        if isinstance(salary, Money):
            self.__salary = salary
        else:
            raise TeacherError("The salary should be a Money class member", salary)

    @property
    def university(self):
        return self.__university

    @university.setter
    def university(self, value):
        if isinstance(value, University):
            self.__university = value
        else:
            raise TeacherError("The university should be a Univesity class member", value)

    @property
    def experience(self):
        return self.__experience

    @experience.setter
    def experience(self, value):
        if isinstance(value, int):
            self.__experience = value
        else:
            raise TeacherError("The experience should be an integer", value)

    @property
    def faculty(self):
        return self.__faculty

    @faculty.setter
    def faculty(self, value):
        if isinstance(value, str):
            self.__faculty = value
        else:
            raise TeacherError("The faculty should be a string", value)

    @property
    def start_work_at(self):
        return self.__start_work_at

    @start_work_at.setter
    def start_work_at(self, value):
        if isinstance(value, Date):
            self.__start_work_at = value
        else:
            raise TeacherError("The start_work_at should be a Date class member", value)

    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, value):
        if isinstance(value, str):
            self.__subject = value
        else:
            raise TeacherError("The subject should be a string", value)

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if isinstance(value, Money):
            self.__salary = value
        else:
            raise TeacherError("The salary should be a Money class member", value)

    def __repr__(self):
        return repr(f"This is Teacher {self.name} {self.surname}. From University {self.__university.name}."
                    f"From the faculty of {self.__faculty}.")


date1 = Date(2003, 10, 1)
money1 = Money(2000, "USD")
university1 = University("EPH", Date(1953, 12, 5), Person("Armen", "Patvakanyan", "Male", 73),
                         City("New York", Person("Vahag", "Tadevosyan", "Male", 55), 150000, "Armenian"))
doctor1 = Teacher("Artak", "Aristakesyan", "Male", 45, "Zeytun Taxamas", [], [], university1, "Mathematics", 20, date1,
                  "Number Theory", money1)
print(doctor1)
print(doctor1.name)
#doctor1.department = 1231
# print(doctor1)
