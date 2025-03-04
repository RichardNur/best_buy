import promotions


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
        self.promotion = None


    def set_promotion(self, promotion):
        """
        Assigns a promotion to the product.

        :param promotion: Instance of the Promotion class applied to the product.
        :raises TypeError: If the promotion is not an instance of the Promotion class.
        """

        if not isinstance(promotion, promotions.Promotion):
            raise TypeError("Invalid Promotion Type.")
        self.promotion = promotion

    @property
    def get_quantity(self):
        """ returns the quantity of the given Product. """
        return self.quantity

    def set_quantity(self, quantity):
        """
        Updates the stock quantity of the product.

        :param quantity: New stock quantity (int; must be >= 0).
        """

        if not isinstance(quantity, int):
            raise TypeError(f"ERROR: Wrong datatype in input.")
        if quantity < 0:
            raise ValueError("Quantity must be 0 or higher.")

        self.quantity = quantity
        if quantity == 0:
            self.deactivate()

    @property
    def is_active(self):
        """returns True if Product is active in the store, otherwise False. """
        return self.active


    def deactivate(self):
        """ Deactivates the availability of the Product in the store."""
        self.active = False


    def show(self):
        """ Returns an f-string to show infos about the Product (quantity left and if its active in the store). """

        promo_text = f"( Promotion: {self.promotion.name})" if self.promotion else ""
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}{promo_text}"


    def buy(self, quantity):
        """
        :param quantity: Number of products the user wants to buy.
        :return: The total price after applying any promotion., if quantity is valid. """

        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer.")
        if quantity <= 0:
            raise ValueError("You have to buy at least 1 product.")
        if quantity > self.quantity:
            raise ValueError(f"Sorry, only {self.quantity} products left.")
        # Calculate & Return total price
        total_price = self.promotion.apply_promotion(self, quantity) if self.promotion else self.price * quantity
        self.set_quantity(self.quantity - quantity)
        return total_price


class NonStockedProduct(Product):
    """ Specialized Product class for items that are always available and do not track stock levels. """

    def __init__(self, name, price):
        super().__init__(name, price, 0)
        self.__quantity = 0


    def show(self):
        """ Displays the product details, including promotions, noting that this is a non-stocked product. """

        promo_text = f" (Promotion: {self.promotion.name})" if self.promotion else ""
        return f"{self.name}, Price: ${self.price}. {promo_text} Non-Stocked Product"


    def set_quantity(self, quantity):
        """ Overrides set_quantity, as stock updates are not allowed for non-stocked products. Deactivates the Product in the store, if 0 or less. """

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
            return self.promotion.apply_promotion(self, quantity) if self.promotion else total_price


class LimitedProduct(Product):
    """ Specialized Product class for items with a purchase limit per order. """

    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum


    def show(self):
        """ Displays the product details, including the maximum purchase limit. """
        return f"{self.name}, Price: ${self.price}. Maximum in order: {self.maximum}"


    def buy(self, quantity):
        """
        :param: quantity: Number of products the user wants to buy.
        :param: maximum: Number of max. purchasable products.
        :return: The total price, if quantity is valid. """

        if quantity > self.maximum:
            raise ValueError(f"{self.name} can only be added {self.maximum} times to cart.")
        return super().buy(quantity)
