"""
File: drink.py
Description: Abstract base class for drinks sold in the café. Adds size and temperature attributes,
             and defines a prepare() method for optional subclass override.
Author: Anush Shirantha De Costa
ID: 110454712
Username: deyay064
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from item import Item
from enums import Size
from abc import abstractmethod


class Drink(Item):
    """
    Base class for all drinks in the café.
    Adds size, cold attributes and a prepare() method.
    """

    def __init__(self, name, price, size, cold=False):
        """
        Initialise a Drink item with size and temperature.

        :param name: Name of the drink (inherited from Item)
        :param price: Base price of the drink
        :param size: A value from the Size enum
        :param cold: Boolean indicating if the drink is cold (default: False)
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
        Prepares the drink by printing a basic message.
        Subclasses may override this for custom preparation steps.
        """
        print(f"Preparing your {self.get_size().value} {self.get_name()}...")

    @abstractmethod
    def calculate_price(self):
        """
        Abstract method to calculate the total price of the drink.
        Must be implemented by subclasses (e.g., Tea, Coffee, Other).
        """
        pass
