from products import Product
import products

class Store:
    """Represents a store containing a list of products."""

    def __init__(self, products :list):
        for product in products:
            self.products = products if products else []

    def add_product(self, product: Product):
        """Adds a new product to the store."""
        if not isinstance(product, Product):
            raise TypeError("Only Product instances can be added.")
        self.products.append(product)
        return f"'{product.name}' successfully added to Store."

    def remove_product(self, product: Product):
        """Removes a product from the store."""
        if not isinstance(product, Product):
            raise TypeError("Only Product instances can be added.")
        self.products.remove(product)

    def get_total_quantity(self):
        return len(self.products)

    def get_all_products(self):
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: list[tuple[Product, int]]):
        """Gets a list of Tuples: (Product, Quantity)"""

        total_price = 0.0

        for request in shopping_list:
            product, quant = request

            # handle input:
            if quant <= 0:
                raise ValueError("You have to order at least 1 product.")
            if product not in self.products:
                print(f"'{product}' is not available. Skipping this request.")
            if product.quantity <= quant:
                print(f"Only {product.quantity} '{product}' left. Skipping this request.")

            else:
                total_price += product.price
        return total_price




if __name__ == "__main__":

    #TESTS
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    ]

    store = Store(product_list)
    products = store.get_all_products()

    print(store.get_total_quantity())

    print(store.order([(products[0], 1), (products[1], 2)]))