"""
File: drink.py
Description: Base class for drinks. Adds size, cold, and prepare().
Author: Anush Shirantha De Costa
ID: 110454712
Username: deyay064
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from item import Item
from enums import Size


class Drink(Item):
    """
    Base class for all drinks in the café.
    Adds size, cold attributes and a prepare() method.
    """

    def __init__(self, name, price, size, cold=True):
        """
        Initialise a Drink item with size and temperature.

        :param name: Name of the drink (inherited from Item)
        :param price: Base price of the drink
        :param size: A value from the Size enum
        :param cold: Boolean indicating if the drink is cold (default: True)
        :raises ValueError: if size or cold are invalid types
        """
        super().__init__(name, price)

        if not isinstance(size, Size):
            raise ValueError("Size must be a member of the Size enum.")
        if not isinstance(cold, bool):
            raise ValueError("Cold must be a boolean.")

        self.__size = size
        self.__cold = cold

    def get_size(self):
        """
        Returns the size of the drink.
        """
        return self.__size

    def is_cold(self):
        """
        Returns True if the drink is cold, False if hot.
        """
        return self.__cold

    def prepare(self):
        """
        Basic preparation method for a drink.
        Can be overridden by subclasses.
        """
        print(f"Preparing your {self.get_size().value} {self.get_name()}...")
