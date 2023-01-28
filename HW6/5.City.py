from HelperClasses import Person


class CityError(Exception):
    def __init__(self, explanation, cause):
        self.explanation = explanation
        self.cause = cause

    def print_obj(self):
        print(self.explanation, self.cause)


class City:
    def __init__(self, name="", mayor=Person(), population=0, language=""):
        if isinstance(name, str):
            self.__name = name
        else:
            raise CityError("The name should be a string", name)
        if isinstance(mayor, Person):
            self.__mayor = mayor
        else:
            raise CityError("The mayor should be a Person class", mayor)
        if isinstance(population, int):
            self.__population = population
        else:
            raise CityError("The population should be an integer", population)
        if isinstance(language, str):
            self.__language = language
        else:
            raise CityError("The language should be a string", language)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self.__name = value
        else:
            raise CityError("The name should be a string", value)

    @property
    def mayor(self):
        return self.__mayor

    @mayor.setter
    def mayor(self, value):
        if isinstance(value, Person):
            self.__mayor = value
        else:
            raise CityError("The mayor should be a Person class", value)

    @property
    def population(self):
        return self.__population

    @population.setter
    def population(self, value):
        if isinstance(value, int):
            self.__population = value
        else:
            raise CityError("The population should be an integer", value)

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, value):
        if isinstance(value, str):
            self.__language = value
        else:
            raise CityError("The language should be a string", value)

    def __repr__(self):
        return repr(f"This is the city of {self.__name}, with Mayor {self.__mayor.name} {self.__mayor.surname}."
                    f"The population of the city is {self.__population} and the official language is "
                    f"{self.__language}.")


city1 = City("New York", Person("Vahag", "Tadevosyan", "Male", 55), 150000, "Armenian")
print(city1)
