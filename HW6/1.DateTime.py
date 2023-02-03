from HelperClasses import Date
from HelperClasses import Time


class DateTimeError(Exception):
    def __init__(self, explanation, cause):
        self.explanation = explanation
        self.cause = cause

    def print_obj(self):
        print(self.explanation, self.cause)


class DateTime(Date, Time):
    def __init__(self, date=Date(), time=Time()):
        if isinstance(date, Date):
            self.__date = date
        else:
            raise DateTimeError("The date should be of Date format", date)
        if isinstance(time, Time):
            self.__time = time
        else:
            raise DateTimeError("The time should be of Time format", time)

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, value):
        if isinstance(value, Date):
            self.__date = value
        else:
            raise DateTimeError("The date should be of Date format", value)

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, value):
        if isinstance(value, Time):
            self.__time = value
        else:
            raise DateTimeError("The time should be of Time format", value)

    def add_year(self, y):
        self.__date.add_year(y)

    def sub_year(self, y):
        self.__date.sub_year(y)

    def add_month(self, m):
        self.__date.add_month(m)

    def sub_month(self, m):
        self.__date.sub_month(m)

    def add_day(self, d):
        self.__date.add_day(d)

    def sub_day(self, d):
        self.__date.sub_day(d)

    def add_hour(self, h):
        new_hour = self.__time.hour + h
        self.__date.add_day(new_hour // 24)
        self.__time.add_hour(h)

    def sub_hour(self, h):
        new_hour = self.__time.hour - h
        self.__date.sub_day(-(new_hour // 24))
        self.__time.sub_hour(h)

    def add_minute(self, m):
        new_min = self.__time.minute + m
        self.add_hour(new_min // 60)
        self.__time.minute = new_min % 60

    def sub_minute(self, m):
        new_min = self.__time.minute - m
        self.sub_hour(-(new_min // 60))
        self.__time.minute = -(new_min // 60)*60 + new_min

    def add_second(self, s):
        new_sec = self.__time.second + s
        self.add_minute(new_sec // 60)
        self.__time.second = new_sec % 60

    def sub_second(self, s):
        new_sec = self.__time.second - s
        self.sub_minute(-(new_sec // 60))
        self.__time.second = -(new_sec // 60)*60 + new_sec

    # def add_minute(self, m):
    #     self.__time.add_minute(m)
    #
    # def sub_minute(self, m):
    #     self.__time.sub_minute(m)
    #
    # def add_second(self, s):
    #     self.__time.add_second(s)
    #
    # def sub_second(self, s):
    #     self.__time.sub_second(s)

    def __add__(self, other):
        result = DateTime(Date(self.__date.year, self.__date.month, self.__date.day),
                          Time(self.__time.hour, self.__time.minute, self.__time.second))
        result.__time.add_second(other.time.second)
        result.__time.add_minute(other.time.minute)
        result.__time.add_hour(other.time.hour)
        result.__date.add_day(other.date.day)
        result.__date.add_month(other.date.month)
        result.__date.add_year(other.date.year)
        return result

    def __sub__(self, other):
        result = DateTime(Date(self.__date.year, self.__date.month, self.__date.day),
                          Time(self.__time.hour, self.__time.minute, self.__time.second))
        result.__time.sub_second(other.time.second)
        result.__time.sub_minute(other.time.minute)
        result.__time.sub_hour(other.time.hour)
        result.__date.sub_day(other.date.day)
        result.__date.sub_month(other.date.month)
        result.__date.sub_year(other.date.year)
        return result

    def __repr__(self):
        return repr(f"Date {self.__date.day}.{self.__date.month}.{self.__date.year} "
                    f"Time {self.__time.hour}:{self.__time.minute}:{self.__time.second}")


datetime1 = DateTime(Date(1996, 12, 25), Time(10, 50, 3))
datetime2 = DateTime(Date(1965, 1, 12), Time(15, 42, 21))
print(datetime1-datetime2)
datetime1.add_hour(100)
datetime1.add_day(10)
print(datetime1)
print(datetime1+datetime2)
print(datetime1)
datetime3 = DateTime(Date(1996, 1, 1), Time(0, 0, 0))
datetime3.sub_second(1)
print(datetime3)
