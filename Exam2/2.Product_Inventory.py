class ProductError(Exception):
    def __init__(self, explanation, cause):
        self.explanation = explanation
        self.cause = cause

    def print_obj(self):
        print(self.explanation, self.cause)


class Product:
    def __init__(self, price=0, id=0, quantity=0):
        if isinstance(price, int):
            self.__price = price
        else:
            raise ProductError("The price should be an integer", price)
        if isinstance(id, int):
            self.__id = id
        else:
            raise ProductError("The id should be an integer", id)
        if isinstance(quantity, int):
            self.__quantity = quantity
        else:
            raise ProductError("The quantity should be an integer", quantity)

    def __repr__(self):
        return repr(f"{self.__quantity} {self.__id} left, at price {self.__price}.")

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if isinstance(value, int):
            self.__price = value
        else:
            raise ProductError("The price should be an integer", value)

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        if isinstance(value, int):
            self.__id = value
        else:
            raise ProductError("The id should be an integer", value)

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        if isinstance(value, int):
            self.__quantity = value
        else:
            raise ProductError("The quantity should be an integer", value)

    def buy(self, quant):
        if self.__quantity >= quant:
            self.__quantity -= quant
        else:
            raise ProductError("There is not available quantity of the product that was requested.", self.__quantity)


class InventoryError(Exception):
    def __init__(self, explanation, cause):
        self.explanation = explanation
        self.cause = cause

    def print_obj(self):
        print(self.explanation, self.cause)


class Inventory:
    def __init__(self, prod_list=[]):
        if isinstance(prod_list, list):
            self.__prod_list = prod_list
        else:
            raise InventoryError("The prod_list should be a list", prod_list)

    def __repr__(self):
        return repr(f"Total {len(self.__prod_list)} different products, with valuation of {self.sum_of_products()}.")

    @property
    def prod_list(self):
        return self.__prod_list

    @prod_list.setter
    def prod_list(self, value):
        if isinstance(value, list):
            self.__prod_list = value
        else:
            raise InventoryError("The prod_list should be a list", value)

    def get_by_id(self, search_id):
        for prod in self.__prod_list:
            if prod.id == search_id:
                return prod
        return "Not found"

    def sum_of_products(self):
        """The function will return the total value of the inventory."""
        total_value = 0
        for prod in self.__prod_list:
            total_value += prod.quantity * prod.price
        return total_value


product1 = Product(100, 190123, 10000)
product2 = Product(3000, 618199, 500)
product3 = Product(12000, 739182, 1500)
print(product1)
print(product2)
print(product3)
inventory1 = Inventory([product1, product2, product3])
print(inventory1)
print(inventory1.sum_of_products())
print(inventory1.get_by_id(618199))
