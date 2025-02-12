from products import Product

class Store:
    """Represents a store containing a list of products."""

    def __init__(self, products):
        """Initializes products in the Store, checks if data types are correct. """

        if not isinstance(products, list):
            raise TypeError(f"Found wrong data type in {products}")

        for product in products:
            if not isinstance(product, Product):
                raise TypeError(f"Found wrong Product Type in {product}.")

        self.products = products if products else []


    def add_product(self, product):
        """Adds a new product to the store."""
        if not isinstance(product, Product):
            raise TypeError("Only Product instances can be added.")

        self.products.append(product)
        return f"'{product.name}' successfully added to Store."


    def remove_product(self, product):
        """Removes a product from the store if it exists."""
        if not isinstance(product, Product):
            raise TypeError(f"Found wrong data type in {product}")
        if product not in Store.get_all_products():
            print(f"{product} is not existing in the store. Cannot remove.")

        else:
            self.products.remove(product)


    def get_total_quantity(self):
        """ Returns the total quantity of a given product. """
        return sum(product.get_quantity() for product in self.products)


    def get_all_products(self):
        """ returns each product available in the Store."""
        return [product for product in self.products if product.is_active()]


    def order(self, shopping_list: list[tuple[Product, int]]):
        """
        Lets the user place an order when given a list of tuples.
        Returns total Price of the placed order and adjusts the quantity in the store when successfully placed.
        """

        total_price = 0.0

        for product, quant in shopping_list:
            # handle input:
            if quant <= 0:
                print("You have to order at least 1 product.")
            elif product not in self.products:
                print(f"'{product}' is not available. Skipping this request.")
            elif product.get_quantity() < quant:
                print(f"Only {product.quantity} '{product.name}' left. Skipping this request.")
                # alt: adjust quant to available stock:     -->     quant = product.get_quantity()

            else:
                total_price += product.price * quant
                product.set_quantity(product.get_quantity() - quant)
                print(f"{quant} x '{product.name}' (${product.price * quant}) ordered.")

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