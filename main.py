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
    print("==== Welcome to Campus Café System ====\n")

    # Create a new store
    cafe = Cafe()

    # === Create drinks ===
    print("Creating drinks...")

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

    # === Create food items ===
    print("\nCreating food items...")

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

    # === Create and use Order ===
    print("\nCreating and populating an order...")
    order = Order()
    order.add_item_to_order(tea)
    order.add_item_to_order(coffee)
    order.add_item_to_order(other)
    order.add_item_to_order(sweet)
    order.add_item_to_order(savoury)

    print("\nOrder details:")
    print(order)

    print("\nRemoving sweet item from the order...")
    order.remove_item_from_order(sweet)
    print("Updated order after removal:")
    print(order)

    # Brew tea and coffee
    print("\nBrewing drinks...")
    tea.brew()
    coffee.brew()

    print("\nUpdated order details after brewing:")
    print(order)

    # === Submit order to store ===
    print("\nSubmitting order to the store...")
    cafe_order = cafe.create_order()
    for item in order.get_items():
        cafe_order.add_item_to_order(item)

    print("\nStore summary:")
    print(f"Total earnings: ${cafe.report_profit():.2f}")
    print(f"Number of orders: {len(cafe.get_order_history())}")

    print("\n==== Test Complete ====")


if __name__ == "__main__":
    main()
