

class Product:
    """The Product class represents a specific type of product available in the store"""

    def __init__(self, name, price, quantity):
        """Initializes the Product with a name, price, and quantity."""
        if not isinstance(name, str) or not name:
            raise TypeError(f"ERROR: 'name' must be a string, but got {type(name).__name__} or empty string.")
        if not isinstance(price, (int, float)):
            raise TypeError(f"ERROR: 'price' must be a number, but got {type(price).__name__}")
        if not isinstance(quantity, int):
            raise TypeError(f"ERROR: 'quantity' must be an integer, but got {type(quantity).__name__}")
        if price < 0:
            raise ValueError("ERROR: 'price' must be positive!")
        if quantity < 0:
            raise ValueError("ERROR: 'quantity' must be 0 or higher")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True


    def get_quantity(self):
        """ returns the quantity of the given Product. """
        return self.quantity

    def set_quantity(self, quantity):
        """ lets the user enter a new quantity. Deactivates the Product in the store, if 0 or less. """
        if not isinstance(quantity, int):
            raise TypeError(f"ERROR: Wrong datatype in input.")
        if quantity < 0:
            raise ValueError("Quantity must be 0 or higher.")

        self.quantity = quantity
        if quantity == 0:
            self.deactivate()


    def is_active(self):
        """returns True if Product is active in the store and False if the Product is not available. """
        return self.active


    def deactivate(self):
        """ Deactivates the availability of the Product in the store."""
        self.active = False


    def show(self):
        """ Returns an f-string to show infos about the Product (quantity left and if its active in the store). """
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}"


    def buy(self, quantity):
        """
        :param quantity: Number of products the user wants to buy.
        :return: The total price, if quantity is valid. """

        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer.")
        if quantity <= 0:
            raise ValueError("You have to buy at least 1 product.")
        if quantity > self.quantity:
            raise ValueError(f"Sorry, only {self.quantity} products left.")
        else:
            # Calculate & Return total price
            total_price = quantity * self.price
            self.set_quantity(self.quantity - quantity)
            return total_price


class NonStockedProduct(Product):
    """  """

    def __init__(self, name, price):
        super().__init__(name, price, 0)
        self.__quantity = 0


    def show(self):
        """  """
        return f"{self.name}, Price: ${self.price}. Non-Stocked Product"


    def set_quantity(self, quantity):
        """ lets the user enter a new quantity. Deactivates the Product in the store, if 0 or less. """
        if not isinstance(quantity, int):
            raise TypeError(f"ERROR: Wrong datatype in input.")
        print(f"{self.name} is not stocked.")


    def buy(self, quantity):
        """
        :param quantity: Number of products the user wants to buy.
        :return: The total price, if quantity is valid. """

        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer.")
        if quantity <= 0:
            raise ValueError("You have to buy at least 1 product.")
        else:
            # Calculate & Return total price
            total_price = quantity * self.price
            return total_price


class LimitedProduct(Product):
    """ """

    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum


    def show(self):
        """  """
        return f"{self.name}, Price: ${self.price}. Maximum in order: {self.maximum}"


    def buy(self, quantity):
        """
        :param: quantity: Number of products the user wants to buy.
        :param: maximum: Number of max. purchasable products.
        :return: The total price, if quantity is valid. """

        if quantity > self.maximum:
            raise ValueError(f"{self.name} can only be added {self.maximum} times to cart.")
        else:
            return super().buy(quantity)



if __name__ == "__main__":
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()

    print(Product("Bose QuietComfort Earbuds", price=250, quantity=500).show())

    print(NonStockedProduct("Windows License", price=125).show())
    print(LimitedProduct("Shipping", price=10, quantity=250, maximum=1).show())

