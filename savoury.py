"""
File: savoury.py
Description: Savoury food subclass with type and flour.
Author: Anush Shirantha De Costa
ID: 110454712
Username: deyay064
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from food import Food
from enums import Flour, Type


class Savoury(Food):
    """
    Represents a savoury food item sold in the café.
    Inherits from the Food class and includes types and flour.
    """
    BASE_PRICE = 2.00

    def __init__(self, size, type, flour):
        """
        Initialise a Savoury food object.

        :param size: Size enum (SMALL / MEDIUM / LARGE)
        :param type: Type enum (LOAF / MUFFIN / SLICE)
        :param flour: Flour enum (WHOLE / WHITE / SLICE)
        """
        super().__init__("Savoury", 0.00, size)

        if not isinstance(type, Type):
            raise ValueError("food_type must be a member of the Type enum")
        if not isinstance(flour, Flour):
            raise ValueError("flour_type must be a member of the Flour enum")

        self.__type = type
        self.__flour = flour

    def calculate_price(self):
        """
        Calculates the total price of the savoury food item based on type and flour.

        :return: Float – final price
        """
        if self.__type == Type.LOAF:
            type_multiplier = 3
        elif self.__type == Type.MUFFIN:
            type_multiplier = 1
        elif self.__type == Type.SLICE:
            type_multiplier = 0.5
        else:
            type_multiplier = 1

        if self.__flour == Flour.WHOLE:
            flour_multiplier = 2
        elif self.__flour == Flour.WHITE:
            flour_multiplier = 1
        else:
            flour_multiplier = 1

        price = self.BASE_PRICE * type_multiplier * flour_multiplier
        return round(price, 2)

    def get_type(self):
        """
        Returns the selected Type enum used in this savoury food item.

        :return: Type
        """
        return self.__type

    def get_flour(self):
        """
        Returns the selected Flour enum used in this savoury food item.

        :return: Flour
        """
        return self.__flour

    def get_price(self):
        """
        Returns the total calculated price of the food item.
        This delegates to calculate_price() for consistency.

        :return: float – final price of the item
        """
        return self.calculate_price()

    def __str__(self):
        """
        Returns a readable string describing the Savoury item, including type,
        size, flour, and calculated price.

        :return: str
        """
        size_text = self.get_size().value
        type_text = self.__type.value
        flour_text = self.__flour.value
        price = self.calculate_price()

        return f"Savoury {size_text} {type_text} made with {flour_text} flour at price - ${price:.2f}"
