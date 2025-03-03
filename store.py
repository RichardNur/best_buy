from products import Product


class Store:
    """Represents a store containing a list of products."""

    def __init__(self, products):
        if not isinstance(products, list):
            raise TypeError(f"Found wrong data type in {products}")

        for product in products:
            if not isinstance(product, Product):
                raise TypeError(f"Found wrong Product Type in {product}.")

        self._products = products if products else []

    @property
    def products(self):
        """Returns all products in the store."""
        return self._products

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

    @property
    def get_total_quantity(self):
        """ Returns the total quantity of a given product. """
        return sum(product.get_quantity() for product in self.products)

    @property
    def get_all_products(self):
        """ returns each product available in the Store."""
        return [product for product in self.products if product.is_active]


    def order(self, shopping_list: list[tuple[Product, int]]):
        """
        Lets the user place an order when given a list of tuples.
        Returns total Price of the placed order and adjusts the quantity in the store when successfully placed.
        """

        total_price = 0.0

        for product, quant in shopping_list:
            # handle input:
            if quant <= 0 or not isinstance(quant, int):
                print(f"Error in quantity for {product.name}.")
            elif product not in self.products:
                print(f"'{product}' is not available. Skipping this request.")

            else:
                # total_price += product.price * quant
                # product.set_quantity(product.get_quantity() - quant)
                # print(f"{quant} x '{product.name}' (${product.price * quant}) ordered.")

                total_price += product.buy(quant)
                print(f"{quant} x '{product.name}' (${product.price * quant}) ordered.")

        return total_price
