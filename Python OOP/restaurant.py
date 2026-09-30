"""restaurant.py - Restaurant class: runs the customer interaction."""

from menu import Menu
from order import Order
from receipt import Receipt


class Restaurant:
    def __init__(self):
        self.menu = Menu({
            "Grilled Chicken": 130.00,
            "Pork BBQ": 100.00,
            "Grilled Liempo": 150.00,
            "Grilled Bangus": 140.00,
            "Grilled Squid": 160.00
        })

    # ---- input helpers ----
    def ask_yes_no(self, question):
        while True:
            answer = input(question + " (yes/no): ").strip().lower()
            if answer in ("yes", "y"):
                return True
            elif answer in ("no", "n"):
                return False
            else:
                print(">> Invalid input. Please type 'yes' or 'no'.\n")

    def get_menu_item(self):
        while True:
            typed = input("Enter the menu item you want to order: ")
            item_name = self.menu.find_item(typed)
            if item_name:
                return item_name
            print(">> Sorry, that item is not on the menu. Please try again.\n")

    def get_quantity(self, item_name):
        while True:
            qty_input = input(f"Enter quantity for {item_name}: ").strip()
            if qty_input.isdigit() and int(qty_input) > 0:
                return int(qty_input)
            else:
                print(">> Invalid quantity. Please enter a positive whole number.\n")

    # ---- order flow ----
    def take_order(self):
        order = Order(self.menu)

        while True:
            item_name = self.get_menu_item()
            quantity = self.get_quantity(item_name)
            order.add_item(item_name, quantity)
            print(f">> Added {quantity} x {item_name} to your order.\n")

            if not self.ask_yes_no("Would you like to order another item?"):
                break

        return order

    def run(self):
        print("Welcome to Jewel Grilling Restaurant Ordering System!\n")

        self.menu.display()

        print()
        if not self.ask_yes_no("Would you like to place an order?"):
            print("\nThank you for visiting Jewel Grilling Restaurant. Come back soon!")
            return

        print()
        order = self.take_order()

        print()
        order.apply_discount(self.ask_yes_no("Are you a Senior Citizen or PWD?"))

        Receipt(order).print()
