
class Product:
    """The Product class represents a specific type of product available in the store"""

    def __init__(self, name: str, price: float, quantity: int):
        if price < 0:
            raise ValueError("Price must be positive!")
        if quantity < 0:
            raise ValueError("Quantity must be 0 or higher")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity: int):
        if quantity < 0:
            raise ValueError("Quantity must be 0 or higher.")

        self.quantity = quantity
        if quantity == 0:
            self.deactivate()

    def is_active(self):
        return self.active

    def deactivate(self):
        self.active = False
        return False

    def show(self):
        return f"{self.name}, Price: {self.price},\
                Quantity: {self.quantity}, active={self.active}"

    def buy(self, quantity: int):
        """
        :param quantity: Number of products the user wants to buy.
        :return: The total price, if quantity is valid.
        """

        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer.")
        if quantity <= 0:
            raise ValueError("You have to buy at least 1 product.")
        if quantity > self.quantity:
            raise ValueError(f"Sorry, only {self.quantity} products left.")

        # Calculate total price
        total_price = quantity * self.price
        self.set_quantity(self.quantity - quantity)

        return total_price


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