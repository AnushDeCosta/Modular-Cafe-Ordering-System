"""
File: main.py
Description: This script demonstrates and validates all key class interactions in the Campus Café system,
             including item creation, order management, price calculation, method invocation, and store reporting.
Author: Anush Shirantha De Costa
ID: 110454712
Username: deyay064
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from enums import Size, Flavour, TeaFlavour, Bean, Type, Flour
from tea import Tea
from coffee import Coffee
from other import Other
from sweet import Sweet
from savoury import Savoury
from order import Order
from store import Cafe


def main():
    print("\n" + "="*40)
    print("WELCOME TO CAMPUS CAFÉ SYSTEM")
    print("="*40 + "\n")

    # Create a new store
    cafe = Cafe()

    # === Drinks Section ===
    print("-" * 25)
    print("Creating drinks...")
    print("-" * 25)

    tea = Tea(
        size=Size.MEDIUM,
        cold=False,
        flavours=[TeaFlavour.CHAI, TeaFlavour.PEPPERMINT],
        sugar=2,
        milk=True
    )
    print(f"Tea: {tea}")

    coffee = Coffee(
        size=Size.LARGE,
        cold=True,
        beans=[Bean.EXCELSA],
        sugar=1,
        milk=False
    )
    print(f"Coffee: {coffee}")

    other = Other(
        size=Size.SMALL,
        cold=True,
        flavour=[Flavour.COLA],
        soda=True
    )
    print(f"Other drink: {other}")

    # === Food Section ===
    print("\n" + "-" * 25)
    print("Creating food items...")
    print("-" * 25)

    sweet = Sweet(
        size=Size.SMALL,
        type=Type.SLICE
    )
    print(f"Sweet: {sweet}")

    savoury = Savoury(
        size=Size.MEDIUM,
        type=Type.LOAF,
        flour=Flour.WHITE
    )
    print(f"Savoury: {savoury}")

    print("\nManually preparing food items:")
    sweet.order()
    savoury.order()

    # === Order Section ===
    print("\n" + "-" * 25)
    print("Creating and populating an order...")
    print("-" * 25)
    order = Order()
    order.add_item_to_order(tea)
    order.add_item_to_order(coffee)
    order.add_item_to_order(other)
    order.add_item_to_order(sweet)
    order.add_item_to_order(savoury)

    print("\nOrder details:")
    print(order)
    print(f"Total (via get_total_price): ${order.get_total_price():.2f}")

    print("\nRemoving sweet item from the order...")
    order.remove_item_from_order(sweet)
    print("Updated order after removal:")
    print(order)
    print(f"Total (via get_total_price): ${order.get_total_price():.2f}")

    # === Brewing Section ===
    print("\n" + "-" * 25)
    print("Brewing drinks...")
    print("-" * 25)
    tea.brew()
    coffee.brew()

    print("\nUpdated order details after brewing:")
    print(order)
    print(f"Total (via get_total_price): ${order.get_total_price():.2f}")

    # === Getter Demonstration ===
    print("\n" + "-" * 25)
    print("Inspecting individual drink states...")
    print("-" * 25)
    print(f"Coffee has milk? {coffee.has_milk()}")
    print(f"Tea sugar: {tea.get_sugar()}")
    print(f"Other includes soda? {other.has_soda()}")

    # === Store Reporting ===
    print("\n" + "-" * 25)
    print("Submitting order to the store...")
    print("-" * 25)
    cafe_order = cafe.create_order()
    for item in order.get_items():
        cafe_order.add_item_to_order(item)

    print("\nStore summary:")
    cafe.report_profit()
    print(f"Total earnings (read from state): ${cafe.get_earnings():.2f}")
    print(f"Number of orders: {len(cafe.get_order_history())}")

    print("\n" + "="*40)
    print("TEST COMPLETE")
    print("="*40)


if __name__ == "__main__":
    main()