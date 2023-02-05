class PassengerError(Exception):
    def __init__(self, explanation, cause):
        self.explanation = explanation
        self.cause = cause

    def print_obj(self):
        print(self.explanation, self.cause)


class Passenger:
    def __init__(self, name="", city="", rooms={}):
        if isinstance(name, str):
            self.__name = name
        else:
            raise PassengerError("The name should be a string", name)
        if isinstance(city, str):
            self.__city = city
        else:
            raise PassengerError("The city name should be a string", city)
        if isinstance(rooms, dict):
            self.__rooms = rooms
        else:
            raise PassengerError("The rooms info should be in a dictionary format", rooms)

    def __repr__(self):
        return repr(f"This is {self.__name}, who is going to fly to {self.__city}.")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self.__name = value
        else:
            raise PassengerError("The name should be a string", value)

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, value):
        if isinstance(value, str):
            self.__city = value
        else:
            raise PassengerError("The city name should be a string", value)

    @property
    def rooms(self):
        return self.__rooms

    @rooms.setter
    def rooms(self, value):
        if isinstance(value, dict):
            self.__rooms = value
        else:
            raise PassengerError("The rooms info should be in a dictionary format", value)


class HotelError(Exception):
    def __init__(self, explanation, cause):
        self.explanation = explanation
        self.cause = cause

    def print_obj(self):
        print(self.explanation, self.cause)


class Hotel:
    def __init__(self, name="", city="", rooms={}):
        """The name here refers to the name of the Hotel."""
        if isinstance(name, str):
            self.__name = name
        else:
            raise PassengerError("The name should be a string", name)
        if isinstance(city, str):
            self.__city = city
        else:
            raise PassengerError("The city name should be a string", city)
        if isinstance(rooms, dict):
            self.__rooms = rooms
        else:
            raise PassengerError("The rooms info should be in a dictionary format", rooms)

    def __repr__(self):
        return repr(f"This is Hotel {self.__name} in the city of {self.__city}.")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self.__name = value
        else:
            raise PassengerError("The name should be a string", value)

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, value):
        if isinstance(value, str):
            self.__city = value
        else:
            raise PassengerError("The city name should be a string", value)

    @property
    def rooms(self):
        return self.__rooms

    @rooms.setter
    def rooms(self, value):
        if isinstance(value, dict):
            self.__rooms = value
        else:
            raise PassengerError("The rooms info should be in a dictionary format", value)

    def free_rooms_list(self, room_type):
        if room_type in self.__rooms:
            return self.__rooms[room_type]
        return "No such room."

    def reserve_rooms(self, room_type, count):
        if room_type in self.__rooms:
            if self.__rooms[room_type] >= count:
                self.__rooms[room_type] -= count
                return "Reservation Made."
            return "Not enough free rooms at the moment."
        return "No such room."


def book():
    passenger1 = Passenger("Artak", "Tokyo", {"1 bed": 3, "2 beds": 2})
    passenger2 = Passenger("John", "New York", {"presidential lux": 10})
    print(passenger1)
    print(passenger2)
    hotel1 = Hotel("Hilton", "Moscow", {"1 bed": 253, "2 beds": 190, "presidential lux": 15})
    print(hotel1)
    print(hotel1.rooms)
    print(hotel1.free_rooms_list("1 bed"))
    print(hotel1.reserve_rooms("2 beds", 25))
    print(hotel1.free_rooms_list("2 beds"))


book()
