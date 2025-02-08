from products import Product
from store import Store

# setup initial stock of inventory
product_list = [ Product("MacBook Air M2", price=1450, quantity=100),
                 Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = Store(product_list)

def start(storage):
    """
    Gets the store and shows the menu. Returns the operation to be executed.
    """
    print("\n   Store Menu   -------\n1. List all products in store\n2. Show total amount in store\n3. Make an order\n4. Quit\n")
    try:
        operation = int(input("Please choose a number: "))
        return operation
    except ValueError as e:
        print(e)

def list_products(storage):
    for n, product in enumerate(storage.get_all_products()):
        print(f"{n+1}. {product.name}, Prize: ${product.price}, Quantity: {product.quantity}")

def show_total_amount(storage):
    total_amount = sum(product.quantity for product in storage.get_all_products())
    print(f"Total of {total_amount} items in store.")

def make_order(storage):
    """let user place an order in the storage."""
    list_products(storage)
    shopping_list = []

    # Take Order:
    while True:
        products = storage.get_all_products()
        try:
            item = int(input(f"\nWhat item do you want to purchase (1 - {len(products)})?\n(Enter '0' for Shopping Cart): "))

            if item == 0:
                break
            else:
                item += -1

            amount = int(input(f"Enter the amount of '{products[item].name}' you want to purchase: "))
            shopping_list.append((products[item], amount))
            print(f"\n{amount} x {products[item].name} added to Shopping List.")

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
            input(f"Order placed! Total Price: ${total_price}\n\nPress Enter to continue.")
        else:
            input("\nNo items ordered. Press Enter to continue.")
    except ValueError as v:
        print(v)
    except IndexError as e:
        print(e)

def main():
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