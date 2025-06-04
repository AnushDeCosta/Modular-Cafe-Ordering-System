"""
File: order.py
Description: Represents an order with item list and price methods.
Author: Anush Shirantha De Costa
ID: 110454712
Username: deyay064
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from item import Item


class Order:
    """
    Represents a customer order containing multiple food and drink items.
    """

    def __init__(self):
        """
        Initialise an empty Order with no items and zero cost.

        This constructor sets up the internal item list and the running total cost,
        which will be updated as items are added or removed.
        """
        self.__items = []
        self.__cost = 0.0

    def add_item_to_order(self, item):
        """
        Adds a menu item to the order and updates the running cost.

        :param item: An instance of Item (or subclass such as Tea, Coffee, Sweet, etc.)
        :raises ValueError: if the object is not an Item subclass
        """
        if not isinstance(item, Item):
            raise ValueError("Only Item subclasses can be added to an order.")
        self.__items.append(item)
        self.__cost += item.calculate_price()

    def remove_item_from_order(self, item):
        """
        Removes a menu item from the order if it exists, and updates the cost.

        :param item: An instance of Item to remove from the order
        :raises ValueError: if the item is not found in the order list
        """
        if not isinstance(item, Item):
            raise ValueError("Only Item subclasses can be removed from an order.")
        if item not in self.__items:
            raise ValueError("Item not found in the order.")
        self.__items.remove(item)
        self.__cost -= item.calculate_price()

    def calculate_price(self):
        """
        Returns the current total price of the order.

        This reflects the sum of all item prices currently in the order.
        :return: Float – total order price
        """
        return round(self.__cost, 2)

    def get_items(self):
        """
        Returns a copy of the items in the order for external inspection or testing.
        :return: list[Item]
        """
        return list(self.__items)

    def get_total_price(self):
        """
        Returns the total price of the order.
        Alias for calculate_price(), added for semantic clarity in usage.

        :return: float – total price of the order
        """
        return self.calculate_price()

    def __str__(self):
        """
        Returns a readable summary of the order, listing each item and the total price.
        :return: str
        """
        if not self.__items:
            return "Order is empty."

        lines = [str(item) for item in self.__items]
        summary = "\n  ".join(lines)
        return f"Order:\n  {summary}\nTotal: ${self.calculate_price():.2f}"
