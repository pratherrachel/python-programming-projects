"""A command-line cafe ordering exercise with validated user input."""

MENU = {
    "cappuccino": 5.00,
    "latte": 4.50,
    "coffee": 3.50,
    "croissant": 3.00,
}


def get_menu_item() -> str:
    """Ask for an available item until the response is valid."""
    while True:
        item = input("Enter the menu item: ").strip().lower()
        if item in MENU:
            return item
        print(f"Sorry, {item!r} is not on the menu. Please try again.")


def get_quantity() -> int:
    """Ask for a positive whole-number quantity."""
    while True:
        try:
            quantity = int(input("Enter the quantity: "))
        except ValueError:
            print("Please enter a whole number.")
            continue
        if quantity > 0:
            return quantity
        print("Quantity must be at least 1.")


def main() -> None:
    name = input("Please enter your name: ").strip() or "Customer"
    print(f"\nWelcome to our cafe, {name}! What would you like to order?")
    print("Menu:")
    for item, price in MENU.items():
        print(f"  {item.capitalize()}: ${price:.2f}")

    item = get_menu_item()
    quantity = get_quantity()
    total = MENU[item] * quantity
    print(f"\nCustomer {name} is buying {quantity} {item}(s). Total cost: ${total:.2f}")


if __name__ == "__main__":
    main()
