"""receipt.py - Receipt class."""

import datetime


class Receipt:
    def __init__(self, order):
        self.order = order

    def print(self):
        order = self.order
        now = datetime.datetime.now().strftime("%B %d, %Y  %I:%M %p")

        print("\n")
        print("=" * 46)
        print("            JEWEL GRILLING RESTAURANT".center(46))
        print("             Grill, Eat, Enjoy!".center(46))
        print("=" * 46)
        print(f" Date: {now}")
        print("-" * 46)
        print(f"{'ITEM':<16}{'QTY':>5}{'PRICE':>10}{'SUBTOTAL':>15}")
        print("-" * 46)

        for item_name, quantity in order.items.items():
            price = order.menu.get_price(item_name)
            print(f"{item_name:<16}{quantity:>5}{price:>10.2f}{order.get_subtotal(item_name):>15.2f}")

        print("-" * 46)
        print(f"{'SUBTOTAL':<31}{order.get_total():>15.2f}")

        if order.discount_amount > 0:
            print(f"{order.discount_label:<31}{'-' + format(order.discount_amount, '.2f'):>15}")

        print("-" * 46)
        print(f"{'TOTAL AMOUNT DUE':<31}{order.get_final_total():>15.2f}")
        print("=" * 46)
        print("      Thank you for dining with us!".center(46))
        print("          Salamat po at Kain Tayo!".center(46))
        print("=" * 46)
