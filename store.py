"""
File: store.py
Description: Defines the Cafe class, which manages customer orders,
             tracks total earnings, and prints summaries of all transactions.
Author: Anush Shirantha De Costa
ID: 110454712
Username: deyay064
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from order import Order


class Cafe:
    """
    Represents a café system that tracks all orders and total earnings.
    """

    def __init__(self):
        """
        Initialises the café with no earnings and an empty order history.
        Orders are tracked for reporting, summaries, and testing purposes.
        """
        self.__earnings = 0.0
        self.__order_history = []

    def report_profit(self):
        """
        Recalculates and returns total earnings based on current order history.
        This ensures up-to-date totals even if items are added/removed from existing orders.

        :return: total revenue from all orders
        """
        self.__earnings = sum(order.calculate_price() for order in self.__order_history)
        return round(self.__earnings, 2) # Rounds to 2 decimals to match café pricing format

    def create_order(self):
        """
        Creates a new blank order, stores it in the internal order history,
        and returns the instance for further population and processing.

        :return: Order – newly created empty Order object
        """
        new_order = Order()
        self.__order_history.append(new_order)
        return new_order

    def get_order_history(self):
        """
        Returns a copy of the café's full order history.

        :return: list[Order] – list of all orders placed in the café
        """
        return list(self.__order_history)

    def get_earnings(self):
        """
        Returns the most recently calculated total earnings.

        :return: float – current earnings value
        """
        return round(self.__earnings, 2) # Rounds to 2 decimals to match café pricing format

    def __str__(self):
        """
        Returns a string summary of the café's total earnings and order history.
        :return: str
        """
        if not self.__order_history:
            return "Cafe has no orders yet."

        lines = [str(order) for order in self.__order_history]
        orders_text = "\n\n".join(lines)
        return f"{orders_text}\n\nTotal Earnings: ${self.report_profit():.2f}"
