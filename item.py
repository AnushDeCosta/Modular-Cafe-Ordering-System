"""
File: item.py
Description: Abstract base class for all café items.
             Stores core item attributes (name and price) and enforces implementation of calculate_price().
Author: Anush Shirantha De Costa
ID: 110454712
Username: deyay064
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from abc import ABC, abstractmethod


class Item(ABC):
    """
    Abstract base class representing a menu item in the café.
    """

    def __init__(self, name, price):
        """
        Initialise an Item with a name and price.

        :param name: The name of the item (must be a non-empty string)
        :param price: The base price of the item (must be >= 0)
        :raises ValueError: if name is empty or price is negative
        """
        if not name or not isinstance(name, str):
            raise ValueError("Item name must be a non-empty string.")
        if price < 0:
            raise ValueError("Item price must be a non-negative number.")

        self.__name = name
        self.__price = price

    @abstractmethod
    def calculate_price(self):
        """
        Abstract method that forces subclasses to define their own price calculation logic.
        This ensures consistent pricing behaviour across all item types.
        """
        pass

    def get_name(self):
        """
        Returns the name of the item.

        :return: The name of the item as a string.
        """
        return self.__name

    def get_price(self):
        """
        Returns the base price of the item.

        :return: The price of the item as a float.
        """
        return self.__price

    @abstractmethod
    def __str__(self):
        """
        Return a human-readable string representation of the item.
        Must be implemented by subclasses.
        """
        pass


