from HelperClasses import Date
from HelperClasses import Person
from HelperClasses import City


class UniversityError(Exception):
    def __init__(self, explanation, cause):
        self.explanation = explanation
        self.cause = cause

    def print_obj(self):
        print(self.explanation, self.cause)


class University:
    def __init__(self, name="", founded_at=Date(), rector=Person(), city=City()):
        if isinstance(name, str):
            self.__name = name
        else:
            raise UniversityError("The name should be a string", name)
        if isinstance(founded_at, Date):
            self.__founded_at = founded_at
        else:
            raise UniversityError("The founded_at field should be a Date class member", founded_at)
        if isinstance(rector, Person):
            self.__rector = rector
        else:
            raise UniversityError("The rector should be a Person class member", rector)
        if isinstance(city, City):
            self.__city = city
        else:
            raise UniversityError("The city should be a City class member", city)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self.__name = value
        else:
            raise UniversityError("The name should be a string", value)

    @property
    def founded_at(self):
        return self.__founded_at

    @founded_at.setter
    def founded_at(self, value):
        if isinstance(value, Date):
            self.__founded_at = value
        else:
            raise UniversityError("The founded_at field should be a Date class member", value)

    @property
    def rector(self):
        return self.__rector

    @rector.setter
    def rector(self, value):
        if isinstance(value, Person):
            self.__rector = value
        else:
            raise UniversityError("The rector should be a Person class member", value)

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, value):
        if isinstance(value, City):
            self.__city = value
        else:
            raise UniversityError("The city should be a City class member", value)

    def __repr__(self):
        return repr(f"This is the {self.__name} University in the {self.__city.name} city. "
                    f"It was founded at the year of {self.__founded_at.year}. "
                    f"The rector is {self.__rector.name} {self.__rector.surname}.")


university1 = University("EPH", Date(1953, 12, 5), Person("Armen", "Patvakanyan", "Male", 73),
                         City("New York", Person("Vahag", "Tadevosyan", "Male", 55), 150000, "Armenian"))
print(university1)
