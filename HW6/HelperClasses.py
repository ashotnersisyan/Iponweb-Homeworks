class CompanyError(Exception):
    def __init__(self, explanation, cause):
        self.explanation = explanation
        self.cause = cause

    def print_obj(self):
        print(self.explanation, self.cause)


class Company:
    def __init__(self, company_name="", founded_at=0, employees_count=0):
        if isinstance(company_name, str):
            self.__company_name = company_name
        else:
            raise CompanyError("The company_name should be a string", company_name)
        if isinstance(founded_at, int):
            self.__founded_at = founded_at
        else:
            raise CompanyError("The founded_at should be an integer", founded_at)
        if isinstance(employees_count, int):
            self.__employees_count = employees_count
        else:
            raise CompanyError("The employees_count should be an integer", employees_count)

    @property
    def company_name(self):
        return self.__company_name

    @company_name.setter
    def company_name(self, value):
        if isinstance(value, str):
            self.__company_name = value
        else:
            raise CompanyError("The company_name should be a string", value)

    @property
    def founded_at(self):
        return self.__founded_at

    @founded_at.setter
    def founded_at(self, value):
        if isinstance(value, int):
            self.__founded_at = value
        else:
            raise CompanyError("The founded_at should be an integer", value)

    @property
    def employees_count(self):
        return self.__employees_count

    @employees_count.setter
    def employees_count(self, value):
        if isinstance(value, int):
            self.__employees_count = value
        else:
            raise CompanyError("The employees_count should be an integer", value)

    def __repr__(self):
        return repr(f"{self.__company_name} founded at {self.__founded_at} has {self.__employees_count} employees.")


class JobError(Exception):
    def __init__(self, explanation, cause):
        self.explanation = explanation
        self.cause = cause

    def print_obj(self):
        print(self.explanation, self.cause)


class Job:
    def __init__(self, company=Company(), salary=0, experience_year=0, position=""):
        if isinstance(company, Company):
            self.__company = company
        else:
            raise JobError("The company should be a Company class", company)
        if isinstance(salary, int) or isinstance(salary, float):
            self.__salary = salary
        else:
            raise JobError("The salary should be an integer or a float", salary)
        if isinstance(experience_year, int):
            self.__experience_year = experience_year
        else:
            raise JobError("The experience_year should be an integer", experience_year)
        if isinstance(position, str):
            self.__position = position
        else:
            raise JobError("The position should be a string", position)

    @property
    def company(self):
        return self.__company

    @company.setter
    def company(self, value):
        if isinstance(value, Company):
            self.__company = value
        else:
            raise JobError("The company should be a Company class", value)

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if isinstance(value, int) or isinstance(value, float):
            self.__salary = value
        else:
            raise JobError("The salary should be an integer or a float", value)

    @property
    def experience_year(self):
        return self.__experience_year

    @experience_year.setter
    def experience_year(self, value):
        if isinstance(value, int):
            self.__experience_year = value
        else:
            raise JobError("The experience_year should be an integer", value)

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if isinstance(value, str):
            self.__position = value
        else:
            raise JobError("The position should be a string", value)

    def __repr__(self):
        return repr(f"Vacancy at {self.__company.company_name}, with salary {self.__salary}. Expected "
                    f"{str(self.__experience_year)} years of experience for the {str(self.__position)} position")

    def change_salary(self, new_salary):
        self.__salary = new_salary

    def change_experience_year(self, new_experience_year):
        self.__experience_year = new_experience_year

    def change_position(self, new_position):
        self.__position = new_position


class PersonError(Exception):
    def __init__(self, explanation, cause):
        self.explanation = explanation
        self.cause = cause

    def print_obj(self):
        print(self.explanation, self.cause)


class Person:
    def __init__(self, name="", surname="", gender="", age=0, address="", friends=[], job=[]):
        if isinstance(name, str):
            self.__name = name
        else:
            raise PersonError("The name should be a string", name)
        if isinstance(surname, str):
            self.__surname = surname
        else:
            raise PersonError("The surname should be a string", surname)
        if isinstance(gender, str):
            self.__gender = gender
        else:
            raise PersonError("The gender should be a string", gender)
        if isinstance(age, int):
            self.__age = age
        else:
            raise PersonError("The age should be an integer", age)
        if isinstance(address, str):
            self.__address = address
        else:
            raise PersonError("The address should be a string", address)
        if isinstance(friends, list):
            self.__friends = friends
        else:
            raise PersonError("The friends should be an list", friends)
        if isinstance(job, list):
            self.__job = job
        else:
            raise PersonError("The job should be an list", job)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self.__name = value
        else:
            raise PersonError("The name should be a string", value)

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, value):
        if isinstance(value, str):
            self.__surname = value
        else:
            raise PersonError("The surname should be a string", value)

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, value):
        if isinstance(value, str):
            self.__gender = value
        else:
            raise PersonError("The gender should be a string", value)

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if isinstance(value, int):
            self.__age = value
        else:
            raise PersonError("The age should be an integer", value)

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        if isinstance(value, str):
            self.__address = value
        else:
            raise PersonError("The address should be a string", value)

    @property
    def friends(self):
        return self.__friends

    @friends.setter
    def friends(self, value):
        if isinstance(value, list):
            self.__friends = value
        else:
            raise PersonError("The friends should be an list", value)

    @property
    def job(self):
        return self.__job

    @job.setter
    def job(self, value):
        if isinstance(value, list):
            self.__job = value
        else:
            raise PersonError("The job should be an list", value)

    def __repr__(self):
        return repr(f"This is {self.__name} {self.__surname}. A {self.__gender}, {self.__age} years of age. "
                    f"Residing at {self.__address}")

    def add_friend(self, new_friend):
        self.__friends.append(new_friend)

    def remove_friend(self, ex_friend):
        self.__friends.remove(ex_friend)

    def add_job(self, new_job):
        new_job.company.employees_count += 1
        self.__job.append(new_job)

    def remove_job(self, ex_job):
        ex_job.company.employees_count -= 1
        self.__job.remove(ex_job)

    def display_job(self):
        print(*self.__job)


class MoneyError(Exception):
    def __init__(self, explanation, cause):
        self.explanation = explanation
        self.cause = cause

    def print_obj(self):
        print(self.explanation, self.cause)


class Money:
    # I will use a 1 common currency for conversion between all so the dictionary is not very big.
    CONVERSION_RATES = {"AMD": 15, "USD": 6000, "RUB": 100, "EUR": 6500, "GBP": 7500}

    def __init__(self, amount=0, currency="USD"):
        if isinstance(amount, int) or isinstance(amount, float):
            self.__amount = amount
        else:
            raise MoneyError("The amount of money should be a number", amount)
        if currency in Money.CONVERSION_RATES.keys():
            self.__currency = currency
        else:
            raise MoneyError("The currency you used does not exist", currency)

    def __repr__(self):
        return repr(f"{self.__amount} {self.__currency}")

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, value):
        if isinstance(value, int) or isinstance(value, float):
            self.__amount = value
        else:
            raise MoneyError("The amount of money should be a number", value)

    @property
    def currency(self):
        return self.__currency

    @currency.setter
    def currency(self, value):
        if value in Money.CONVERSION_RATES.keys():
            self.__currency = value
        else:
            raise MoneyError("The currency you used does not exist", value)

    def conversion(self, new_currency):
        gen_amount = self.__amount * Money.CONVERSION_RATES[self.__currency]
        new_amount = gen_amount / Money.CONVERSION_RATES[new_currency]
        self.__amount = new_amount
        self.__currency = new_currency

    def __add__(self, other):
        if self.__currency == other.currency:
            return Money(self.__amount + other.amount, self.__currency)
        else:
            other_copy = Money(other.amount, other.currency)
            other_copy.conversion(self.__currency)
            return Money(self.__amount + other_copy.amount, self.__currency)

    def __sub__(self, other):
        if self.__currency == other.currency:
            return Money(self.__amount - other.amount, self.__currency)
        else:
            other_copy = Money(other.amount, other.currency)
            other_copy.conversion(self.__currency)
            return Money(self.__amount - other_copy.amount, self.__currency)

    def __truediv__(self, other):
        if self.__currency == other.currency:
            return self.__amount / other.amount
        else:
            other_copy = Money(other.amount, other.currency)
            other_copy.conversion(self.__currency)
            return self.__amount / other_copy.amount

    def __eq__(self, other):
        if self.__currency == other.currency:
            return self.__amount == other.amount
        else:
            other_copy = Money(other.amount, other.currency)
            other_copy.conversion(self.__currency)
            return self.__amount == other_copy.amount

    def __ne__(self, other):
        if self.__currency == other.currency:
            return self.__amount != other.amount
        else:
            other_copy = Money(other.amount, other.currency)
            other_copy.conversion(self.__currency)
            return self.__amount != other_copy.amount

    def __lt__(self, other):
        if self.__currency == other.currency:
            return self.__amount < other.amount
        else:
            other_copy = Money(other.amount, other.currency)
            other_copy.conversion(self.__currency)
            return self.__amount < other_copy.amount

    def __gt__(self, other):
        if self.__currency == other.currency:
            return self.__amount > other.amount
        else:
            other_copy = Money(other.amount, other.currency)
            other_copy.conversion(self.__currency)
            return self.__amount > other_copy.amount

    def __le__(self, other):
        return self < other or self == other

    def __ge__(self, other):
        return self > other or self == other


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


class DateError(Exception):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def print_obj(self):
        print(self.a, self.b)


class Date:
    MONTH_DAYS = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 31, 12: 31}

    def __init__(self, year=1, month=1, day=1):
        if Date.is_leap(year):
            self.MONTH_DAYS[2] = 29
        else:
            self.MONTH_DAYS[2] = 28
        self.__year = year
        if month > 12 or month < 1:
            raise DateError("Date out of range:", month)
        else:
            self.__month = month
        if day > self.MONTH_DAYS[self.__month] or day < 1:
            raise DateError("Date out of range:", day)
        else:
            self.__day = day

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, value):
        if value > self.MONTH_DAYS[self.__month] or value < 1:
            raise DateError("Date out of range:", value)
        else:
            self.__day = value

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, value):
        if value > 12 or value < 1:
            raise DateError("Date out of range:", value)
        else:
            self.__month = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        self.__year = value

    def __repr__(self):
        return repr(f"{self.__day}.{self.__month}.{self.__year}")

    @staticmethod
    def is_leap(year):
        if (year % 400 == 0) and (year % 100 == 0):
            return True
        elif (year % 4 == 0) and (year % 100 != 0):
            return True
        else:
            return False

    @staticmethod
    def normalizer(year, month, day):
        if Date.is_leap(year):
            month_days_curr = Date.MONTH_DAYS
            month_days_curr[2] = 29
        else:
            month_days_curr = Date.MONTH_DAYS
            month_days_curr[2] = 28
        if day > month_days_curr[month]:
            day = month_days_curr[month]
        return year, month, day

    def add_year(self, y):
        new_year = self.__year + y
        new_year, new_month, new_day = Date.normalizer(new_year, self.__month, self.__day)
        self.__year = new_year
        self.__month = new_month
        self.__day = new_day

    def sub_year(self, y):
        new_year = self.__year - y
        new_year, new_month, new_day = Date.normalizer(new_year, self.__month, self.__day)
        self.__year = new_year
        self.__month = new_month
        self.__day = new_day

    def add_month(self, m):
        new_month = self.__month + m
        if new_month != 12:
            self.__month = new_month % 12
        else:
            self.__month = new_month
        self.add_year(new_month // 12)
        new_year, new_month, new_day = Date.normalizer(self.__year, self.__month, self.__day)
        self.__year = new_year
        self.__month = new_month
        self.__day = new_day

    def sub_month(self, m):
        new_month = self.__month - m
        if new_month == 0:
            self.__month = 12
            self.sub_year(1)
        elif new_month < 0:
            self.__month = -(new_month // 12)*12 + new_month
        else:
            self.__month = new_month
        self.sub_year(-(new_month // 12))
        new_year, new_month, new_day = Date.normalizer(self.__year, self.__month, self.__day)
        self.__year = new_year
        self.__month = new_month
        self.__day = new_day

    def add_day(self, d):
        new_day = self.__day + d
        month_days_curr = Date.MONTH_DAYS
        while new_day > month_days_curr[self.__month]:
            if Date.is_leap(self.__year):
                month_days_curr[2] = 29
            else:
                month_days_curr[2] = 28
            new_day -= month_days_curr[self.__month]
            self.add_month(1)
        new_year, new_month, new_day = Date.normalizer(self.__year, self.__month, new_day)
        self.__year = new_year
        self.__month = new_month
        self.__day = new_day

    def sub_day(self, d):
        new_day = self.__day - d
        month_days_curr = Date.MONTH_DAYS
        while new_day <= 0:
            if Date.is_leap(self.__year):
                month_days_curr[2] = 29
            else:
                month_days_curr[2] = 28
            new_day += month_days_curr[self.__month]
            self.sub_month(1)
        new_year, new_month, new_day = Date.normalizer(self.__year, self.__month, new_day)
        self.__year = new_year
        self.__month = new_month
        self.__day = new_day


class TimeError(Exception):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def print_obj(self):
        print(self.a, self.b)


class Time:
    def __init__(self, hour=0, minute=0, second=0):
        if hour > 23 or hour < 0:
            raise TimeError("Time out of range:", hour)
        else:
            self.__hour = hour
        if minute > 59 or minute < 0:
            raise TimeError("Time out of range:", minute)
        else:
            self.__minute = minute
        if second > 59 or second < 0:
            raise TimeError("Time out of range:", second)
        else:
            self.__second = second

    @property
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self, value):
        if value > 23 or value < 0:
            raise TimeError("Time out of range:", value)
        else:
            self.__hour = value

    @property
    def minute(self):
        return self.__minute

    @minute.setter
    def minute(self, value):
        if value > 59 or value < 0:
            raise TimeError("Time out of range:", value)
        else:
            self.__minute = value

    @property
    def second(self):
        return self.__second

    @second.setter
    def second(self, value):
        if value > 59 or value < 0:
            raise TimeError("Time out of range:", value)
        else:
            self.__second = value

    def __repr__(self):
        return repr(f"{self.__hour}:{self.__minute}:{self.__second}")

    def add_hour(self, h):
        new_hour = self.__hour + h
        self.__hour = new_hour % 24

    def sub_hour(self, h):
        new_hour = self.__hour - h
        self.__hour = -(new_hour // 24)*24 + new_hour

    def add_minute(self, m):
        new_min = self.__minute + m
        self.add_hour(new_min // 60)
        self.__minute = new_min % 60

    def sub_minute(self, m):
        new_min = self.__minute - m
        self.sub_hour(-(new_min // 60))
        self.__minute = -(new_min // 60)*60 + new_min

    def add_second(self, s):
        new_sec = self.__second + s
        self.add_minute(new_sec // 60)
        self.__second = new_sec % 60

    def sub_second(self, s):
        new_sec = self.__second - s
        self.sub_minute(-(new_sec // 60))
        self.__second = -(new_sec // 60)*60 + new_sec


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
        return repr(f"This is the {self.__name} University in the {self.__city.name} city."
                    f"It was founded at the year of {self.__founded_at.year}."
                    f"The rector is {self.__rector.name} {self.__rector.surname}.")


# time1 = Time(5, 56, 13)
# time2 = Time(10, 15, 13)
# time3 = Time(2, 10, 53)
# time1.add_minute(15)
# print(time1)
# time2.add_second(686)
# print(time2)
# time3.add_hour(25)
# print(time3)
#
#
# date1 = Date(2011, 10, 8)
# date2 = Date(1999, 11, 29)
# date3 = Date(1996, 4, 15)
# date1.add_year(10)
# print(date1)
# date2.add_month(3)
# print(date2)
# date2.add_year(1)
# print(date2)
# date2.add_day(1)
# print(date2)
# date3.add_day(1000)
# print(date3)

# time4 = Time(0, 0, 0)
# print(time4)
# time4.sub_second(1)
# print(time4)
# date4 = Date(2000, 1, 1)
# print(date4)
# date4.sub_day(1)
# print(date4)


