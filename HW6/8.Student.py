from HelperClasses import Person
from HelperClasses import City
from HelperClasses import University
from HelperClasses import Date


class StudentError(Exception):
    def __init__(self, explanation, cause):
        self.explanation = explanation
        self.cause = cause

    def print_obj(self):
        print(self.explanation, self.cause)


class Student(Person):
    def __init__(self, name="", surname="", gender="", age=0, address="", friends=[], job=[],
                 university=University(), faculty="", course=0, start_at=Date()):
        super().__init__(name, surname, gender, age, address, friends, job)
        if isinstance(university, University):
            self.__university = university
        else:
            raise StudentError("The university should be a Univesity class member", university)
        if isinstance(faculty, str):
            self.__faculty = faculty
        else:
            raise StudentError("The faculty should be a string", faculty)
        if isinstance(course, int):
            self.__course = course
        else:
            raise StudentError("The experience should be an integer", course)
        if isinstance(start_at, Date):
            self.__start_at = start_at
        else:
            raise StudentError("The start_at should be a Date class member", start_at)

    @property
    def university(self):
        return self.__university

    @university.setter
    def university(self, value):
        if isinstance(value, University):
            self.__university = value
        else:
            raise StudentError("The university should be a Univesity class member", value)

    @property
    def course(self):
        return self.__course

    @course.setter
    def course(self, value):
        if isinstance(value, int):
            self.__course = value
        else:
            raise StudentError("The experience should be an integer", value)

    @property
    def faculty(self):
        return self.__faculty

    @faculty.setter
    def faculty(self, value):
        if isinstance(value, str):
            self.__faculty = value
        else:
            raise StudentError("The faculty should be a string", value)

    @property
    def start_at(self):
        return self.__start_at

    @start_at.setter
    def start_at(self, value):
        if isinstance(value, Date):
            self.__start_at = value
        else:
            raise StudentError("The start_at should be a Date class member", value)

    def __repr__(self):
        return repr(f"This is {self.name} {self.surname}. A student at the {self.__university.name}. "
                    f"At the faculty of {self.__faculty}")


university1 = University("EPH", Date(1953, 12, 5), Person("Armen", "Patvakanyan", "Male", 73),
                         City("New York", Person("Vahag", "Tadevosyan", "Male", 55), 150000, "Armenian"))
student1 = Student("Artak", "Aristakesyan", "Male", 45, "Zeytun Taxamas", [], [], university1, "Biology",
                   2, Date(2021, 9, 1))
print(student1)
print(student1.name)
