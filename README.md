# Store Inventory Management

## 📌  Overview

This Python-based **Store Inventory Management System** allows users to:

- List all available products in the store.
- Display the total quantity of all products.
- Place an order by selecting products and specifying quantities.
- Exit the system when finished.

The program is structured using three main components:

1. **`main.py`** - Handles user interaction and menu navigation.
2. **`store.py`** - Defines the `Store` class to manage product operations.
3. **`products.py`** - Defines the `Product` class representing individual store items.

---

## 📂  Structure

```
store-management/
│── main.py         # Entry point of the application
│── store.py        # Store class implementation
│── products.py     # Product class implementation
│── README.md       # Project documentation
```

---

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```sh
   git clone https://github.com/your-repo/store-management.git
   cd store-management
   ```
2. **Run the program:**
   ```sh
   python main.py
   ```

---

## 🛠️ How It Works

### 1️⃣ Menu Options

When you run `main.py`, you will see the following menu:

```
   Store Menu   -------
   1. List all products in store
   2. Show total amount in store
   3. Make an order
   4. Quit
```

Users can enter a number to select an action.

### 2️⃣ Listing Products

Selecting **Option 1** displays all available products with their name, price, and quantity.

### 3️⃣ Showing Total Inventory

Selecting **Option 2** shows the total quantity of all items in the store.

### 4️⃣ Placing an Order

- Selecting **Option 3** allows users to choose products and specify the quantity to purchase.
- The system confirms the order and displays the total price.
- If an invalid selection is made, the program prompts the user again.

### 5️⃣ Exiting the System

Selecting **Option 4** exits the program.

---

## 🏗️ Code Overview

### 🔹 `Product` Class (products.py)

```python
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
```

Each product has a **name**, **price**, and **quantity**.

### 🔹 `Store` Class (store.py)

```python
class Store:
    def __init__(self, products):
        self.products = products

    def get_all_products(self):
        return self.products

    def order(self, shopping_list):
        total_price = sum(item.price * quantity for item, quantity in shopping_list)
        return total_price
```

The `Store` class manages products and processes customer orders.

### 🔹 `main.py` (Program Entry Point)

The main script initializes the store, displays a menu, and processes user selections.

---

## 🚀 Future Enhancements

🔹 Improve error handling for incorrect inputs.
🔹 Add functionality for adding/removing products.
🔹 Implement a database for persistent storage.

---

## 📜 License

This project is open-source and free to use.

---

## 🤝 Contributing

Feel free to submit **issues** and **pull requests** to improve the project! 🚀

