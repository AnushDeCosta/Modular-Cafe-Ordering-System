"""
File: food.py
Description: Abstract base class for café food items. Stores size attribute and defines a generic order() method.
             Requires subclasses to implement calculate_price().
Author: Anush Shirantha De Costa
ID: 110454712
Username: deyay064
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from item import Item
from enums import Size
from abc import abstractmethod


class Food(Item):
    """
    Base class for all Food items in the café.
    Adds size attribute and an order() method.
    """

    def __init__(self, name, price, size):
        """
        Initialise a Food item with size.

        :param name: Name of the food (inherited from Item)
        :param price: Base price of the food
        :param size: A value from the Size enum
        :raises ValueError: for invalid enum values
        """
        super().__init__(name, price)

        if not isinstance(size, Size):
            raise ValueError("Size must be a member of the Size enum.")

        self.__size = size

    def get_size(self):
        """
        Returns the size of the food.
        """
        return self.__size

    def order(self):
        """
        Basic preparation method for a food item.
        Can be overridden by subclasses.
        """
        print(f"Preparing your {self.get_size().value} {self.get_name()}...")

    @abstractmethod
    def calculate_price(self):
        """
        Abstract method to calculate the total price of the food.
        Must be implemented by subclasses (e.g., Savoury or Sweet).
        """
        pass

    def __str__(self):
        """
        Return a string representation of the food item, including size, name, and total price.

        :return: Formatted string like "Medium Muffin - $3.50"
        """
        return f"{self.get_size().value} {self.get_name()} - ${self.calculate_price():.2f}"

