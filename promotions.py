from abc import abstractmethod

class Promotion:
    """ Abstract base class for defining promotions. """

    def __init__(self, name):
        if not isinstance(name, str) or not name:
            raise TypeError(f"ERROR: 'Promotion' must be a string, but got {type(name).__name__} or empty string.")
        self.name = name


    @abstractmethod
    def apply_promotion(self, product, quantity):
        """ Abstract method for calculating the promotion discount. """
        pass


class SecondHalfPrice(Promotion):
    """ Applies a second item at half price discount. """

    def __init__(self, name):
        super().__init__(name)


    def apply_promotion(self, product, quantity):
        """
        Calculates the total price after applying a "second item half price" promotion.

        :param product: The Product instance.
        :param quantity: Quantity of products purchased.
        :return: Adjusted total price.
        """

        discounted_items = quantity // 2
        price = product.price
        return (quantity - discounted_items) * price + discounted_items * (price / 2)


class ThirdOneFree(Promotion):
    """ Applies a "buy two, get one free" promotion. """

    def __init__(self, name):
        super().__init__(name)


    def apply_promotion(self, product, quantity):
        """
        Calculates the total price after applying a "third one free" promotion.

        :param product: The Product instance.
        :param quantity: Quantity of products purchased.
        :return: Adjusted total price.
        """

        free_items = quantity // 3
        price = product.price
        return (quantity - free_items) * price


class PercentDiscount(Promotion):
    """Applies a discount based on a percentage off the total price."""

    def __init__(self, name, percent):
        self.percent = percent / 100
        super().__init__(name)


    def apply_promotion(self, product, quantity):
        """Applies a discount based on a percentage off the total price."""

        discount = product.price * self.percent
        return quantity * (product.price - discount)

