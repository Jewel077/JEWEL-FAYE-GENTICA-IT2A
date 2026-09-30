"""menu.py - menu data and menu display."""

menu = {
    "Grilled Chicken": 130.00,
    "Pork BBQ": 100.00,
    "Grilled Liempo": 150.00,
    "Grilled Bangus": 140.00,
    "Grilled Squid": 160.00
}


def display_menu(menu_dict):
    print("=" * 46)
    print("          JEWEL GRILLING RESTAURANT - MENU")
    print("=" * 46)
    print(f"{'MENU ITEM':<25}{'PRICE (PHP)':>18}")
    print("-" * 46)
    for item, price in menu_dict.items():
        print(f"{item:<25}{price:>15.2f}")
    print("=" * 46)
