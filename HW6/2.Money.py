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


money1 = Money(50000, "AMD")
money2 = Money(100, "USD")
money3 = money1 - money2
money4 = Money(40000, "AMD")
print(money1)
print(money2)
print(money3)
print(money4 == money2)
print(money3 > money1)
print(money4 <= money2)
print(money4 <= money1)
# money5 = Money("100", "asda")
# money6 = Money("asdas", "USD")