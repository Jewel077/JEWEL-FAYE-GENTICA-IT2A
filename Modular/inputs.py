"""inputs.py - validated user input helpers."""


def ask_yes_no(question):
    while True:
        answer = input(question + " (yes/no): ").strip().lower()
        if answer in ("yes", "y"):
            return True
        elif answer in ("no", "n"):
            return False
        else:
            print(">> Invalid input. Please type 'yes' or 'no'.\n")


def get_menu_item(menu_dict):
    while True:
        typed = input("Enter the menu item you want to order: ").strip().lower()
        for item_name in menu_dict:          # case-insensitive match
            if item_name.lower() == typed:
                return item_name
        print(">> Sorry, that item is not on the menu. Please try again.\n")


def get_quantity(item_name):
    while True:
        qty_input = input(f"Enter quantity for {item_name}: ").strip()
        if qty_input.isdigit() and int(qty_input) > 0:
            return int(qty_input)
        else:
            print(">> Invalid quantity. Please enter a positive whole number.\n")
