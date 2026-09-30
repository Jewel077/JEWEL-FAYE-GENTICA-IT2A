"""order.py - Order class (items, totals, discount)."""


class Order:
    def __init__(self, menu):
        self.menu = menu
        self.items = {}            # {item name: quantity}
        self.discount_amount = 0.00
        self.discount_label = "None"

    # ---- ordering ----
    def add_item(self, item_name, quantity):
        self.items[item_name] = self.items.get(item_name, 0) + quantity

    # ---- calculations ----
    def get_subtotal(self, item_name):
        return self.menu.get_price(item_name) * self.items[item_name]

    def get_total(self):
        return sum(self.get_subtotal(name) for name in self.items)

    def apply_discount(self, is_senior_or_pwd):
        total = self.get_total()
        if is_senior_or_pwd:
            self.discount_amount = total * 0.20
            self.discount_label = "Senior Citizen / PWD Discount (20%)"
        elif total >= 500:
            self.discount_amount = total * 0.10
            self.discount_label = "Loyalty Discount for orders >= PHP 500 (10%)"

    def get_final_total(self):
        return self.get_total() - self.discount_amount
