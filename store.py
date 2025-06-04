"""
File: store.py
Description: Cafe system tracking earnings and orders.
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
        Initialise the café with no earnings and an empty order history.
        """
        self.__earnings = 0.0
        self.__order_history = []

    def report_profit(self):
        """
        Recalculates and returns the total earnings made by the café
        based on recorded order history.

        :return: Float – total revenue from all placed orders
        """
        self.__earnings = sum(order.calculate_price() for order in self.__order_history)
        return round(self.__earnings, 2)

    def create_order(self):
        """
        Creates a new order, adds it to the order history internally,
        and returns it for use.

        :return: Order – a new blank order object
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
        return round(self.__earnings, 2)

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
