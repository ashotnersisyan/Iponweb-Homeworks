class PersonError(Exception):
    def __init__(self, explanation, cause):
        self.explanation = explanation
        self.cause = cause

    def print_obj(self):
        print(self.explanation, self.cause)


class Person:
    def __init__(self, name="", surname="", gender="", age=None, address="", friends=[], job=[]):
        if isinstance(name, str):
            self.__name = name
        else:
            raise PersonError("The name should be a string", name)
        if isinstance(surname, str):
            self.__surname = surname
        else:
            raise PersonError("The surname should be a string", surname)
        if gender == "M" or gender == "F" or gender == "":
            self.__gender = gender
        else:
            raise PersonError("The gender should be a string", gender)
        if isinstance(age, int) or age is None:
            if isinstance(age, int):
                if age < 101 and age > 17:
                    self.__age = age
                else:
                    raise PersonError("The age should be an integer in the range from 18 to 100", age)
            else:
                self.__age = age
        else:
            raise PersonError("The age should be an integer or None if unknown", age)
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
        if value == "M" or value == "F" or value == "":
            self.__gender = value
        else:
            raise PersonError("The gender should be a string", value)

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if isinstance(value, int) or value is None:
            if isinstance(value, int):
                if value < 101 and value > 17:
                    self.__age = value
                else:
                    raise PersonError("The age should be an integer in the range from 18 to 100", value)
            else:
                self.__age = value
        else:
            raise PersonError("The age should be an integer or None if unknown", value)

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
