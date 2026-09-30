"""main.py - Jewel Grilling Restaurant Ordering System (Modular version)."""

from menu import menu, display_menu
from inputs import ask_yes_no
from order import take_order, calculate_order
from discount import apply_discount
from receipt import print_receipt


def main():
    print("Welcome to Jewel Grilling Restaurant Ordering System!\n")

    display_menu(menu)

    print()
    if not ask_yes_no("Would you like to place an order?"):
        print("\nThank you for visiting Jewel Grilling Restaurant. Come back soon!")
        return

    print()
    customer_order = take_order(menu)

    item_subtotals, order_total = calculate_order(menu, customer_order)

    print()
    discount_amount, discount_label = apply_discount(order_total)

    print_receipt(menu, customer_order, item_subtotals, order_total,
                  discount_amount, discount_label)


if __name__ == "__main__":
    main()
