import products
import promotions
from store import Store


# setup initial stock of inventory
product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250),
                 products.NonStockedProduct("Windows License", price=125),
                 products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
               ]

best_buy = Store(product_list)

# Create promotion catalog
second_half_price = promotions.SecondHalfPrice("Second Half price!")
third_one_free = promotions.ThirdOneFree("Third One Free!")
thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

# Add promotions to products
product_list[0].set_promotion(second_half_price)
product_list[1].set_promotion(third_one_free)
product_list[3].set_promotion(thirty_percent)


def start(storage):
    """
    Displays the store menu and takes user input to choose an operation.

    :param storage: Store instance containing the available products.
    :return: Selected operation (int).
    """

    print("\n   Store Menu   -------\n1. List all products in store\n2. Show total amount in store\n3. Make an order\n4. Quit\n")
    try:
        operation = int(input("Please choose a number: "))
        return operation
    except ValueError as e:
        print(e)


def list_products(storage):
    """
    Lists all available products in the store.

    :param storage: Store instance containing the available products.
    """

    for n, product in enumerate(storage.get_all_products):
        print(f"{n + 1}. {product.show()}")
        # print(f"{n+1}. {product.name}, Prize: ${product.price}, Quantity: {product.quantity}")


def show_total_amount(storage):
    """
    Displays the total number of items in the store.

    :param storage: Store instance containing the available products.
    """

    total_amount = sum(product.quantity for product in storage.get_all_products)
    print(f"Total of {total_amount} items in store.")


def make_order(storage):
    """
    Allows the user to create an order and processes it.

    :param storage: Store instance containing the available products.
    :raises ValueError: If invalid input is provided during the process.
    """

    list_products(storage)
    shopping_list = []

    while True:
        # Take Order:
        all_products = storage.get_all_products
        try:
            item = int(input(f"\nWhat item do you want to purchase (1 - {len(all_products)})?\n(Enter '0' for Shopping Cart): "))

            if item == 0: # Go to Cart if '0' is entered for an item:
                break
            else:
                item += -1

            amount = int(input(f"Enter the amount of '{all_products[item].name}' you want to purchase: "))
            shopping_list.append((all_products[item], amount))
            print(f"\n{amount} x {all_products[item].name} added to Shopping List.")

        except ValueError as v:
            print(v)
        except TypeError as t:
            print(t)
        except IndexError as i:
            print(f"Error in product choice. Choose a valid item! {i}")

        # Place Order:
        print("Shopping List:")
        for item, amount in shopping_list:
            print(f"{item.name} ({amount})")

    try:
        if shopping_list:
            total_price = storage.order(shopping_list)
            input(f"Order placed! Total Price: ${total_price} (with Promotions)\n\nPress Enter to continue.")
        else:
            input("\nNo items ordered. Press Enter to continue.")
    except ValueError as v:
        print(v)
    except IndexError as e:
        print(e)


def main():
    """
    Main program loop for interacting with the store.

    Prompts users to select operations and handles their execution, including listing products,
    showing total quantities, and making orders. Exits on user request.
    """

    func_dic = {
        1: list_products,
        2: show_total_amount,
        3: make_order,
    }

    while True:
        operation = start(best_buy)

        if operation == 4:  # Quit option
            print("\nGoodbye!")
            exit()

        action = func_dic.get(operation)
        if action:
            action(best_buy)
        else:
            print("\nInvalid option. Please choose a number between 1 and 4.")


if __name__ == "__main__":
    main()