"""menu.py - Menu class."""


class Menu:
    def __init__(self, items):
        self.items = items  # {item name: price}

    def display(self):
        print("=" * 46)
        print("          JEWEL GRILLING RESTAURANT - MENU")
        print("=" * 46)
        print(f"{'MENU ITEM':<25}{'PRICE (PHP)':>18}")
        print("-" * 46)
        for item, price in self.items.items():
            print(f"{item:<25}{price:>15.2f}")
        print("=" * 46)

    def find_item(self, typed):
        """Return the official item name matching typed text (case-insensitive), else None."""
        for item_name in self.items:
            if item_name.lower() == typed.strip().lower():
                return item_name
        return None

    def get_price(self, item_name):
        return self.items[item_name]
