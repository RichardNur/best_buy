from typing import List
from products import Product

class Store:
    """Represents a store containing a list of products."""

    def __init__(self, products: List[Product]):
        self.products = products if products else []

    def add_product(self, product: Product):
        """Adds a new product to the store."""
        if not isinstance(product, Product):
            raise TypeError("Only Product instances can be added.")
        self.products.append(product)
        return f"'{product.name}' successfully added to Store."

    def remove_product(self, product: Product):
        """Removes a product from the store if it exists."""
        try:
            self.products.remove(product)
        except ValueError:
            print(f"'{product.name}' is not in the store.")

    def get_total_quantity(self):
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self):
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: list[tuple[Product, int]]):
        """Gets a list of Tuples: (Product, Quantity)"""

        total_price = 0.0

        for product, quant in shopping_list:
            # handle input:
            if quant <= 0:
                raise ValueError("You have to order at least 1 product.")
            if product not in self.products:
                print(f"'{product}' is not available. Skipping this request.")
            if product.get_quantity() <= quant:
                print(f"Only {product.quantity} '{product}' left. Skipping this request.")
                # alt: adjust quant to available stock:     -->     quant = product.get_quantity()

            total_price += product.price * quant
            product.set_quantity(product.get_quantity() - quant)

        return total_price




if __name__ == "__main__":

    #TESTS
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250),
                    ]

    store = Store(product_list)
    products = store.get_all_products()

    print(store.get_total_quantity())
    print(store.order([(products[0], 1), (products[1], 2)]))

    print()
    print(products[1].show())